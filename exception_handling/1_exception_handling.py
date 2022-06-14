# Exception - it is an unwanted event
# Exception Handling - which will not repair the code, instead it is an
# alternate way to gracefully terminate the program

# Exception Handling have blocks:
# 1. try block - is used to store the code in a try block which are suspicious 
# 2. except block - is used to handle the exception

class exception:
    def division(self):
        div = 0
        no1 = int(input("Enter 1st value : "))
        no2 = int(input("Enter 2nd value : "))
        try:
            div = no1/no2
        except Exception as e: # Exception is an in-built class
            print(e)

        print(f"Division : {div}")
        print("End of program")

exception_obj = exception()
exception_obj.division()






# class exception:
#     def division(self):
#         div = 0
#         no1 = int(input("Enter 1st value : "))
#         no2 = int(input("Enter 2nd value : "))
       
#         div = no1/no2
       
#         print(f"Division : {div}")
#         print("End of program")

# exception_obj = exception()
# exception_obj.division()

# # ZeroDivisionError: division by zero
# # ZeroDivisionError this is an inbuilt python class
# # that it is the child class of Exception class