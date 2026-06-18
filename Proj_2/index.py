from datetime import date
class Restaurant:
    def __init__(self):
        self.ord=[]
        self.menu = {
            "1": {"name": "Burger", "price": 5.00},
            "2": {"name": "Pizza", "price": 8.50},
            "3": {"name": "Pasta", "price": 7.00},
            "4": {"name": "Tacos", "price": 3.50},
            "5": {"name": "Fries", "price": 2.00},
            "6": {"name": "Salad", "price": 4.50},
            "7": {"name": "Ice Cream", "price": 3.00},
            "8": {"name": "Soda", "price": 1.50},
            "9": {"name": "Milkshake", "price": 3.50}
                }

    def order(self):
        print("--------------Menu--------------")
        for i in self.menu:
            print(f"{i} {self.menu[i]["name"]} - {self.menu[i]["price"]}")
        print("--------------------------------")
        print("To Place an order type in id followed by qty. Example type 1*10 for 10 burgers. Type end to exit")
        while True:
            opt=input("Enter: ")
            if opt.lower() == "end":
                break
            if "*" in opt:
                itemid,qty=opt.split("*")
                if itemid in self.menu:
                    cst=(self.menu[itemid]["price"])*(int(qty))
                    self.ord.append([date.today(),self.menu[itemid]['name'],qty,self.menu[itemid]['price']])
                    print(f"Added {qty} {self.menu[itemid]["name"]} cost {cst}")
                else:
                    print("Invalid Product ID")
            else:
                print("Invalid Format.type 1*10 for 10 burgers. Type end to exit")
    
    def bill(self):
        print("--------------Final Invoice--------------")
        total=0
        for i in self.ord:
            if i[0] == date.today():
                print(f"{i[1]} {i[2]} - {float(i[3])*float(i[2])}")
                total += float(i[3])*float(i[2])
            else:
                print("No Orders Made Today")
                break
        print(f"Grand Total {total}")
        print("-----------------------------------------")

    def orderHist(self):
        print("--------------Order History--------------")
        for i in self.ord:
            print(f"{i[0]} \n {i[1]} {i[2]} - {float(i[3])*float(i[2])}")
        print("-----------------------------------------")

restaurant=Restaurant()
while True:
    print("--------------Welcome To Restaurant--------------")
    print("1. Place Order")
    print("2. Order History")
    print("3. Exit")
    choice=input("Enter Choice: ")
    if choice == "1":
        restaurant.order()
        restaurant.bill()
    elif choice == "2":
        restaurant.orderHist()
    else:
        break
    print("-------------------------------------------------")