# def name_input():
#     name = input("Enter your name : ")
#     return name

# naam = name_input()
# print("Got my data : ",naam)
# naam = naam.upper()
# print(naam)

def add(): #non-parameterized function - a function which doesnot expect parameter/argument
    a=int(input("Enter no1 : "))
    b=int(input("Enter no2 : "))
    c=a+b
    print(c)
    return c
    
value = add()
print(value)
