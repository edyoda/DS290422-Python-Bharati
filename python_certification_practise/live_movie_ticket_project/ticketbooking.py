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
                        if self.is_seat_booked(i,j):
                            print("B",end=" ")
                        else:
                            print("S",end=" ")   
            print()


    def buy_ticket(self):
        row = int(input("Enter the row for which you want to book the ticket : "))
        column = int(input("Enter the column for which you want to book the ticket : "))
        total_seats = self.rows*self.columns
        half_row=self.rows//2
        if total_seats<=60:
            ticket_price=10
        else:
            if (row<=half_row):
                ticket_price=10 #front half
            else:
                ticket_price=8  #back half
        seat_ID = str(row)+str(column)
        option = int(input(f"Your opt row is {row} and column is {column}, so the price for your seat is {ticket_price}. If you still want to book please enter \n1.Yes \n2.No \n"))
        if option == 1:
            name = input("Enter your name : ")
            gender = input("Enter your gender : ")
            age = input("Enter your age : ")
            mobile_no = input("Enter your mobile no : ")
            self.ticket_details[seat_ID] = [name,gender,age,mobile_no,ticket_price]
            print(f"Booked Successfully : {self.ticket_details}")
        elif option == 2:
            print("No Problem! Thank You for connecting with Book My Show!!!")

    def statictics(self):
        no_of_tickets_booked = len(self.ticket_details)
        precentage = (no_of_tickets_booked/(self.rows * self.columns))*100
        price_lst = []
        for k,v in self.ticket_details.items():
            price_lst.append(v[4])
        current_income = sum(price_lst)
        if self.rows*self.columns<=60:
            total_income=self.rows*self.columns*10
        else:
            front_price=10
            back_price=8
            front_seats=(self.rows//2)*self.columns
            total_income=front_seats*front_price+(self.rows*self.columns-front_seats)*back_price

        print(f"Number of tickets purchased : {no_of_tickets_booked} \nPerecentage : {precentage}% \nCurrent Income : {current_income} \nTotal Income : {total_income}")

    def user_info(self):
        row = int(input("Enter the row for which you want to book the ticket : "))
        column = int(input("Enter the column for which you want to book the ticket : "))
        seat_ID = str(row)+str(column)
        user_data = self.ticket_details.get(seat_ID,00)
        if user_data:
            print(f"Name : {user_data[0]} \nGender : {user_data[1]} \nAge : {user_data[2]} \nMobile No : {user_data[3]} \nTicket Price : {user_data[4]}")
        else:
            print(f"No Ticket Booked w.r.t the row i.e {row} and column i.e {column} provided by you!")


    def is_seat_booked(self,row,column):
        seat_ID = str(row)+str(column)
        for i in self.ticket_details.keys():
            if i == seat_ID:
                return True
        return False



# total_income=(self.half_row*self.columns)*10+((self.rows-self.half_row)*self.columns*8)



