import random
from datetime import date
class Trains:
    def __init__(self):
        self.trainBooked=[]
        self.trainPrice = {
            1010: {  # Mumbai - Delhi Superfast
                "1ac": 2500,
                "2ac": 1800,
                "3ac": 1200,
                "sl": 450
            },
            2013: {  # Delhi - Jaipur Intercity
                "cc": 650,
                "2s": 200
            },
            3045: {  # Prayagraj - Delhi Express
                "2ac": 1600,
                "3ac": 1100,
                "sl": 380
            },
            4099: {  # Rajdhani Express
                "1ac": 3500,
                "2ac": 2400,
                "3ac": 1700
            },
            5012: {  # Duronto Express
                "1ac": 3200,
                "2ac": 2200,
                "3ac": 1550,
                "sl": 550
            }
        }
        self.trainList=[
            [1010, "Mumbai - Delhi Superfast", "Mumbai", "Delhi", 50],
            [2013, "Delhi - Jaipur Intercity", "Delhi", "Jaipur", 42],
            [3045, "Prayagraj - Delhi Express", "Prayagraj", "Delhi", 12],
            [4099, "Rajdhani Express", "Sealdah", "Delhi", 8],
            [5012, "Duronto Express", "Howrah", "Mumbai", 25]]

    def viewTrain(self):
        print("--------------View Train--------------")
        for i in self.trainList:
            print(f"{i[0]} {i[1]} {i[2]} to {i[3]}. Number Of Tickets:{i[4]}")

    def bookTrain(self):
        print("--------------Book Train--------------")
        for i in self.trainList:
            print(f"{i[0]} {i[1]} {i[2]} to {i[3]}. Number Of Tickets:{i[4]}")
        print("Enter Train Number and number of tickets. Ex 1010,4 for 4 tickets in 1010 train. type End to exit")
        opt=input("Enter: ")
        if opt.lower() == "end":
            pass
        else:
            trainNo,tickets = opt.split(',')
            if int(trainNo) in self.trainPrice:
                print("Choose Your Coach")
                for coach,price in self.trainPrice[int(trainNo)].items():
                    print(f"{coach} - {price}")
                opCoach=input("Enter Coach: ")
                if opCoach in self.trainPrice[int(trainNo)]:
                    numTickets=int(tickets)
                    found=False
                    for i in self.trainList:
                        if i[0] == int(trainNo):
                            found=True
                            if i[4] >= numTickets:
                                i[4] -= numTickets
                                pnr=random.randint(0,(10**10)-1)
                                price=numTickets*self.trainPrice[int(trainNo)][opCoach]
                                self.trainBooked.append([date.today(),pnr,int(trainNo),numTickets,price])
                                print(f"Total Cost For Ticekts is {price}")
                                print(f"PNR for Train Journey is {pnr}")
                            else:
                                print("Tickets Unavailable")
                            break
                        if not found:
                            break
            else:
                print("\bInvalid Train Number")
    
    def cancelTrain(self):
        pnr=int(input("Enter PNR Number OF Ticket: "))
        found = False
        for i in self.trainBooked:
            if i[1] == pnr:
                found = True
                ticketsRestored=i[3]
                trainNum=i[2]
                self.trainBooked.remove(i)
                print(f"Cancelled Booking With PNR {pnr}")
                for i in self.trainList:
                    if i[0]==trainNum:
                        i[4] += ticketsRestored
                    
                break
                    
        if not found:
            print("Ticket Isnt Available")
    
    def bookingHist(self):
        for i in self.trainBooked:
            print("----------------------------")
            print(f'''Date: {i[0]}\nPNR: {i[1]}\nTrain No:{i[2]} Num Tickets:{i[3]} Net_Price:{i[4]}''')
            print("----------------------------")


train=Trains()
while True:
    print("--------------Railway Booking System--------------")
    print("1. View Trains")
    print("2. Book Train")
    print("3. Cancel Train")
    print("4. Previous Bookings")
    print("5. Exit")
    opt=input("Enter Choice: ")
    if opt == "1":
        train.viewTrain()
    elif opt == "2":
        train.bookTrain()
    elif opt =="3":
        train.cancelTrain()
    elif opt =="4":
        train.bookingHist()
    else:
        break
    print("--------------------------------------------------")