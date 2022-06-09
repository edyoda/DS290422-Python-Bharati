from book import *

class book_project:
    book_list = []
    def execute(self,choice):
        
        if choice == 1:
            print("---------------Add Book------------------")
            book_id = int(input("Enter Book ID : "))
            book_name = input("Enter Book Name : ")
            book_author = input("Enter Book Author : ")
            book_publisher = input("Enter Book Publisher : ")
            book_price = float(input("Enter Book Price : "))
            book_obj = book(book_id,book_name,book_author,book_publisher,book_price)
            self.book_list.append(book_obj)
            
        elif choice == 2:
            print("---------------Search Book------------------")
            found=False
            book_id = int(input("Enter the book ID of the book you want : "))
            for books in self.book_list:
                if books.book_id==book_id:
                    print(books)
                    found=True
                    break
            if found==False:
                print("book not found")

        elif choice == 3:
            print("---------------Update Book------------------")
            # found=False
            # book_id = int(input("Enter the book ID of the book you want : "))
            # for i in range(len(self.book_list)):
            #     if self.book_list[i].book_id==book_id:
                    
            #         book_name = input("Enter Book Name : ")
            #         book_author = input("Enter Book Author : ")
            #         book_publisher = input("Enter Book Publisher : ")
            #         book_price = float(input("Enter Book Price : "))

            #         self.book_list[i].set_book_name(book_name)
            #         self.book_list[i].set_book_author(book_author)
            #         self.book_list[i].set_book_publisher(book_publisher)
            #         self.book_list[i].set_book_price(book_price)

            #         found=True
            #         break
            # if found==False:
            #     print("book not found")

            # refer this one by Basit
            book_id=int(input("Enter Book id: "))
            for books in self.book_list:
                if books.book_id==book_id:
                    books.set_book_name(input("Enter Book Name: "))
                    books.set_book_author(input("Enter Book Author: "))
                    books.set_book_publisher=input("Enter Book Publsher: ")
                    books.set_book_price(float(input("Enter Book price: ")))

        elif choice == 4:
            print("---------------Delete Book------------------")
            found=False
            book_id = int(input("Enter the book ID of the book you want : "))
            for books in self.book_list:
                if books.book_id==book_id:
                    self.book_list.remove(books)
                    found=True
                    break
            if found==False:
                print("book not found")

        elif choice == 5:
            print("---------------Display Book------------------")
            for i in range(len(self.book_list)):
                print(self.book_list[i])
        else:
            print("Invalid Input")

while(True):
    print("Enter \n1.Add Book \n2.Search Book \n3.Update Book \n4.Delete Book \n5.Display Book")
    choice = int(input("Enter your choice : "))
    book_project_obj = book_project()
    book_project_obj.execute(choice)

book_id=int(input("Enter Book id: "))
for books in self.book_list:
    if books.book_id==book_id:
        books.set_book_name(input("Enter Book Name: "))
        books.set_book_author(input("Enter Book Author: "))
        books.set_book_publisher=input("Enter Book Publsher: ")
        books.set_book_price(float(input("Enter Book price: ")))
