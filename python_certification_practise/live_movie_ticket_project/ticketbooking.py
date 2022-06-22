class bookmyshow:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.ticket_details = {}


    def show_seats(self):
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if i == 0:
                    if j == 0:
                        print(" ", end=" ")
                    else:
                        print(j, end=" ")
                else:
                    if j == 0:
                        print(i,end=" ")
                    else:
                        print("S",end=" ")   
            print()


    def buy_ticket(self):
        row = int(input("Enter the row for which you want to book the ticket : "))
        column = int(input("Enter the column for which you want to book the ticket : "))
        ticket_price = 400
        seat_ID = str(row)+str(column)
        option = int(input(f"Your opt row is {row} and column is {column}, so the price for your seat is {ticket_price}. If you still want to book please enter \n1.Yes \n2.No \n"))
        if option == 1:
            name = input("Enter your name : ")
            gender = input("Enter your gender : ")
            age = input("Enter your age : ")
            mobile_no = input("Enter your mobile no : ")
            self.ticket_details[seat_ID] = [name,gender,age,mobile_no,ticket_price]
            print("Booked Successfully")
        elif option == 2:
            print("No Problem! Thank You for connecting with Book My Show!!!")

    def statictics(self):
        pass

    def user_info(self):
        row = int(input("Enter the row for which you want to book the ticket : "))
        column = int(input("Enter the column for which you want to book the ticket : "))
        seat_ID = str(row)+str(column)
        user_data = self.ticket_details.get(seat_ID,00)
        if user_data:
            print(f"Name : {user_data[0]} \nGender : {user_data[1]} \nAge : {user_data[2]} \nMobile No : {user_data[3]} \nTicket Price : {user_data[4]}")
        else:
            print(f"No Ticket Booked w.r.t the row i.e {row} and column i.e {column} provided by you!")





    