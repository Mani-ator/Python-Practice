bal = 100000
expense=[]
income=0
def addIncome():
    global bal
    global income
    inc=int(input("Enter Income Of The Month: "))
    bal += inc
    income += inc
    print(f"Your \bUpdated Balance is {bal}")

def addExpense():
    global expense
    global bal
    while True:
        print("Enter Your Expense along witht the cost Ex Reason,cost. To End type end")
        exp=input("Enter Here: ")
        if exp.lower() == "end":
            print("Total Expense Added:",bal)
            break
        else:
            l=exp.split(",")
            totalExp += int(l[1])
            expense.append(l)
            bal -= int(l[1])
            

def monthlyAnalysis():
    global expense
    print("Income: ", income)
    total_expense=0
    for i in expense:
        exp=int(expense[i][1])
        total_expense += exp
    print("Total Expense: ", total_expense)
    print("Top Categories")
    top=sorted(expense,key=lambda x:int(x[1]),reverse=True)[0:2:1]
    print(top)


while True:
    print("--------------------------------------------------")
    print("Current balance:",bal)
    print("1.Add Income")
    print("2.Add Expense")
    print("3.Monthly Analysis")
    print("4.Exit")
    opt=input("Enter Option: ")
    if opt == "1":
        addIncome()
    elif opt== "2":
        addExpense()
    elif opt =="3":
        monthlyAnalysis()
    else:
        break