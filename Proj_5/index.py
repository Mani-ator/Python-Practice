import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='7093786161'
)

cur = conn.cursor()

cur.execute('''CREATE DATABASE IF NOT EXISTS Proj_5_Inv''')
conn.database='Proj_5_Inv'
cur.execute("use Proj_5_Inv")
cur.execute('''CREATE TABLE IF NOT EXISTS PTable(
            pno varchar(4) Primary Key,
            Name varchar(100) Not Null,
            Price float Not Null,
            Qty int,
            Status enum('Active','Closed'));''')
cur.execute('''CREATE TABLE IF NOT EXISTS TTable(
            tid int AUTO_INCREMENT PRIMARY KEY,
            Date datetime,
            pno varchar(4),
            Action Varchar(256),
            Qty int,
            Foreign key (pno) references PTable(pno));''')

class Inventory:

    def show(self):
        print("-----------Inventory Table-----------")
        cur.execute("Select* from PTable")
        ptable=cur.fetchall()
        data=[]
        for i in ptable:
            data.append([i[0],i[1],i[2],i[3],i[4]])
        df=pd.DataFrame(data=data,columns=["PID","Name","Price","Stock Qty","Status"])
        print(df)

    def addProduct(self):
        print("-----------Adding Product-----------")
        while True:
            pid=input("Enter Product ID: ")
            name=input("Enter Product Name: ")
            try:
                price=float(input("Enter Price Of Product: "))
                stock=int(input("Enter Amount Of Qty In Stock: "))
            except ValueError:
                print("Value Of Price And Stock Is A Proper DataType")
                continue
            status="Active"
            try:
                query="insert into PTable(pno,Name,Price,Qty,Status) values (%s,%s,%s,%s,%s);"
                values=(pid.upper(),name,price,stock,status)
                cur.execute(query,values)
                conn.commit()
                print(f"Successfully Added item id {pid} {name}")
            except mysql.connector.errors.IntegrityError:
                print("PID Has Been Re-entered Reinput Product Data Again")
                conn.rollback()
                continue
            opt=input("Do You Want To Enter Another Product (y/n): ")
            if opt.lower() == "n":
                break
    
    def sellProduct(self):
        # pid.upper(),name,price,stock,status
        print("-----------Sell Product-----------")
        pid=input("Enter Product ID: ")
        query="select * from PTable where pno=%s;"
        cur.execute(query,(pid.upper(),))
        pvalues=cur.fetchall()
        try:
            if pvalues[0][4] == "Closed":
                print("Product Not Available")
            else:
                try:
                    units=int(input("Enter Number Of Products: "))
                    price=pvalues[0][2]
                    tPrice= price*units
                    if units > pvalues[0][3]:
                        print("Enter Valid Amount Of Products")
                        print(f"Number Of Units for {pvalues[0][1]} is {pvalues[0][3]}")
                    else:
                        uQty = pvalues[0][3]-units
                        query2="update PTable set Qty=%s where pno=%s;"
                        cur.execute(query2,(uQty,pid))
                        query3 = "insert into TTable(Date,pno,Action,Qty) values (Now(),%s,%s,%s);"
                        values=(pid,"Sale",units)
                        cur.execute(query3,values)
                        conn.commit()
                        print("----------------------")
                        return (f"Name:{pvalues[0][1]} Units:{units} \nNet Price {tPrice}")
                except ValueError:
                    print("Enter Integer Value For Amount Of Products")
        except IndexError:
            print("Product ID Not Found")

    def reStock(self):
        print("-----------Restocking-----------")
        pid=input("Enter Product ID: ")
        units=int(input("Enter Amount Of Stock Added: "))
        try:
            query="select * from PTable where pno=%s;"
            cur.execute(query,(pid.upper(),))
            pvalues=cur.fetchall()
            opt=input("Confirm (y/n): ")
            if opt.lower() == 'y':
                UQty= pvalues[0][3]+units
                query2="update PTable set Qty=%s where pno=%s;"
                cur.execute(query2,(UQty,pid))
                query3 = "insert into TTable(Date,pno,Action,Qty) values (Now(),%s,%s,%s);"
                values=(pid,"Restock",units)
                cur.execute(query3,values)
                conn.commit()
                print(f"Updated stock Value of {pvalues[0][1]} to {UQty}")
            else:
                conn.rollback()
        except ValueError:
            print("Enter An Integer Value For Amount Of Stock Added")
    
    def searchProduct(self):
        print("-----------Search Product-----------")
        opt=input("Enter Product Name/ID: ")
        term = f"%{opt}%"
        query = "select * from PTable where Name like %s or pno like %s;"
        cur.execute(query,(term,term))
        pValue=cur.fetchall()
        if not pValue:
            print("No Records Found")
        else:
            print(pValue)

    def lowStockReport(self):
        print("-----------Low Stock Report-----------")
        query = "select * from PTable where Qty <=5;"
        cur.execute(query)
        PValue=cur.fetchall()
        data=[]
        for i in PValue:
            data.append([i[0],i[1],i[2],i[3],i[4]])
        df=pd.DataFrame(data=data,columns=["PID","Name","Price","Stock Qty","Status"])
        print(df)
    
    def transactionHist(self):
        print("-----------Transaction History-----------")
        query = "select* from TTable;"
        cur.execute(query)
        values=cur.fetchall()
        data=[]
        for i in values:
            data.append([i[0],i[1],i[2],i[3],i[4]])
        df=pd.DataFrame(data=data,columns=["Tid","Date","Pno","Action","Qty"])
        print(df)

    def inverntoryValue(self):
        cur.execute("Select* from PTable")
        val=cur.fetchall()
        value=0
        for i in val:
            print(f"{i[1]} - {i[2]*i[3]}")
            value += i[2]*i[3]
        print("Total Inventory Worth:",value)
    
    def lowProducts(self):
        print("-----------Top 5 Products-----------")
        query = "select* from TTable;"
        cur.execute(query)
        values=cur.fetchall()
        data=[]
        for i in values:
            data.append([i[0],i[1],i[2],i[3],i[4]])
        df=pd.DataFrame(data=data,columns=["Tid","Date","Pno","Action","Qty"])
        dftp=df.sort_values(by="Qty")
        print(dftp.tail(5))
        

inv = Inventory()
while True:
    print("-----------Main Menu-----------")
    print('''1. Add Product
2. View Inventory
3. Sell Product
4. Restock Product
5. Search Product
6. Low Stock Report
7. Transaction History
8. Inventory Value
9. Less Sale Products
10. Exit''')
    opt=input("Enter Choice")
    if opt =="1":
        inv.addProduct()
    elif opt == "2":
        inv.show()
    elif opt == "3":
        inv.sellProduct()
    elif opt == "4":
        inv.reStock()
    elif opt =="6":
        inv.lowStockReport()
    elif opt == "5":
        inv.searchProduct()
    elif opt == "7":
        inv.transactionHist()
    elif opt == "8":
        inv.inverntoryValue()
    elif opt == "9":
        inv.lowProducts()
    else:
        break