from ticketbooking import *
class ticketbook:

    def __init__(self,bookmyshow_obj):
        self.bookmyshow_obj = bookmyshow_obj

    def execute(self,choice):
        
        if choice == 1:
            print("*******************Show the seats*******************\n")
            self.bookmyshow_obj.show_seats()

        elif choice == 2:
            print("*******************Buy a ticket*******************")
            self.bookmyshow_obj.buy_ticket()

        elif choice == 3:
            print("*******************Statistics*******************")
            self.bookmyshow_obj.statictics()

        elif choice == 4:
            print("*******************Show booked Tickets User Info*******************")
            self.bookmyshow_obj.user_info()

        elif choice == 5:
            print("*******************Exit*******************")

        else:
            print("Invalid Input!")

if __name__ == "__main__":
    rows = int(input("Enter the number of rows : "))
    columns = int(input("Enter the number of seats in each row : "))
    bookmyshow_obj = bookmyshow(rows=rows,columns=columns)
    ticketbook_obj = ticketbook(bookmyshow_obj)
    while True:
        choice = int(input("Enter \n1.Show the seats \n2.Buy a ticket \n3.Statistics \n4.Show booked Tickets User Info \n0.Exit \n"))
        ticketbook_obj.execute(choice=choice)
