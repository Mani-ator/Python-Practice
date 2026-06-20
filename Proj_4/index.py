import random
from datetime import date
class Account:
    def __init__(self):
        self.accounts = {
                4829105437: {
                    "Name": "Alex Rivera",
                    "Password": "SecurePass123",
                    "Balance": 1250
                },
                8930124576: {
                    "Name": "Sam Jordan",
                    "Password": "Password987",
                    "Balance": 0
                }
            }
        self.accountNum = 0
        self.transHist= []
        self.login=False
    def createAccount(self):
        print("-----------Account Creation-----------")
        name=input("Enter Name: ")
        password=input("Enter A Password: ")
        accNum=int(random.randint(0,10**10-1))
        print(f"Your Account Number is {accNum}")
        self.accounts[accNum]={"Name":name,"Password":password,"Balance":0}
        self.accountNum = accNum
        self.login=True
        self.showMenu()

    def loginAccount(self):
        print("-----------Account Login-----------")
        accNum=int(input("Enter Account Number: "))
        password=input("Enter Password: ")
        if accNum in self.accounts:
            if self.accounts[accNum]["Password"] == password :
                print("Login Successfully")
                print(f'Welcome {self.accounts[accNum]["Name"]}')
                self.accountNum = accNum
                self.login=True
                self.showMenu()
            else:
                print("Incorrect Credentials")
                self.login=False
        else:
            print("Account Not Found")
    
    def showMenu(self):
        while self.login==True:
            print("1.Deposit")
            print("2.Withdrawal")
            print("3.Transfer")
            print("4.View Balance")
            print("5.Transaction History")
            print("6.Exit")
            opt=input("Enter Choice: ")
            if opt == "1":
                self.deposit()
            elif opt == "2":
                self.withdraw()
            elif opt == "3":
                self.transfer()
            elif opt =="4":
                self.viewBalance()
            elif opt == "5":
                self.transactionHist()
            else:
                self.login = False
                break
                

    def deposit(self):
        amt=int(input("Enter Amount To Deposit: "))
        if amt >=0:
            if self.accountNum in self.accounts:
                self.accounts[self.accountNum]["Balance"] += amt
                print(f"Deposit of Amount {amt} Is Successfull!")
                self.transHist.append([date.today(),self.accountNum,amt,"Deposit"])
            else:
                print("Account Details Not Found")
        else:
            print("Invalid Deposit Amount Entry")

    def withdraw(self):
        amt=int(input("Enter Amount To Withdraw: "))
        if amt >=0 :
            if self.accountNum in self.accounts:
                if self.accounts[self.accountNum]["Balance"] >= amt:
                    self.accounts[self.accountNum]["Balance"] -= amt
                    print(f"Withdrawal Of amount {amt} Successfull!")
                    self.transHist.append([date.today(),self.accountNum,amt,"Withdrawal"])
                else:
                    print("Insufficient Funds")
            else:
                print("Account Details Not Found")
        else:
            print("Invalid Withdrawal Amount Entry")

    def transfer(self):
        amt=int(input("Enter Amount To Transfer: "))
        if amt >=0:
            tranAcc=int(input("Enter Account Number Of Tranfer Receipient: "))
            if self.accountNum in self.accounts:
                if self.accounts[self.accountNum]["Balance"] >= amt:
                    if tranAcc in self.accounts:
                        self.accounts[tranAcc]["Balance"] += amt
                        self.accounts[self.accountNum]["Balance"] -= amt
                        print(f'Successfully Tranferred {amt} To {tranAcc} Receipient Name-{self.accounts[tranAcc]["Name"]}')
                        self.transHist.append([date.today(),self.accountNum,amt,f'Transfer to {self.accounts[tranAcc]["Name"]}'])
                        self.transHist.append([date.today(),tranAcc,amt,f'Recieved {amt} from {self.accounts[self.accountNum]["Name"]}'])
                    else:
                        print("Receipient Account Not Found")
                else:
                    print("Insufficient Funds")
            else:
                print("Account Details Not Found")
        else:
            print("Invalid Transfer Amount Entry")
    
    def viewBalance(self):
        bal=self.accounts[self.accountNum]["Balance"]
        print(f'Account Balance Of Account Number {self.accountNum} is {bal}')
    
    def transactionHist(self):
        found=False
        for i in self.transHist:
            
            if self.accountNum == i[1]:
                found = True
                print("----------------------")
                print(f"Date: {i[0]} \nAmount: {i[2]} \nRemark: {i[3]}")
                print("----------------------")
            
        if not found:
            print("Bank Account Transaction Not Found")
        else:
            self.viewBalance()

account=Account()

while True:
    print("ATM/Banking System")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    accopt=input("Enter Choice: ")
    if accopt == "1":
        account.createAccount()
    elif accopt == "2":
        account.loginAccount()
    elif accopt == "3":
        break
    else:
        print("Invalid Option")