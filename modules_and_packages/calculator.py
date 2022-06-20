# Module 
# - A module is a file (.py file) consisting of Python code. It can define functions,methods,classes,variables.
# - A module allows you to logically organize your python code.
# - It also helps in resusing the code
# - Grouping related code into module makes the code easier and more understandable


# import addition_calculation
import addition_calculation as add
# from addition_calculation import *
# from addition_calculation import addition,division

def subtraction():
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    add = no1 - no2
    return add

def multiplication():
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    add = no1 * no2
    return add

print("Name in Calculator : ",__name__)


if __name__ == "__main__":
    print("*****************Subraction**************")
    result = subtraction()
    print("Subtraction : ",result)

    print("\n*****************Multiplication**************")
    result = multiplication()
    print("Multiplication : ",result)

    print("\n*****************Additon**************")
    result = add.addition()
    print("Addition : ",result)

    print("\n*****************Division**************")
    result = add.division()
    print("Dvision : ",result)

