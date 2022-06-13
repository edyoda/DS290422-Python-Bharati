import pdb

def addition(no1,no2):
    return no1 + no2

pdb.set_trace()
no1 = int(input("Enter 1st number : "))
no2 = input("Enter 2nd number : ")
add = addition(no1,no2)
print("Addition : ",add)