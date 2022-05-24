# types of variables
# 1. local variable 
#   - the variables which are define inside the function are know as local variable 
#   - it's scope is within that function itself
# 2. global variable
#   - the variables which are define outside the function are know as global variable 
#   - it's scope is throughout the python file

# # local variable
# def addition():
#     no1 = 10            #local variable
#     no2 = 20            #local variable
#     add = no1 + no2     #local variable
#     return add

# result = addition()
# print("Addition : ",result)

# global variable

from reprlib import aRepr


name = "Bharati"        #global variable

def addition():
    no1 = 10            #local variable
    no2 = 20            #local variable
    add = no1 + no2     #local variable
    print(name)
    return add

result = addition()
print("Addition : ",result)

print("end : ",name)

def fun():
    size = int(input("Enter the size of your list : ")) 

    lst = []
    for i in range(size): 
        data = int(input("Enter your element : "))
        lst.append(data)

    print("List : ",lst)

    new_lst = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] == lst[j] and lst[i] not in new_lst:
                new_lst.append(lst[i])

    return new_lst

lst = fun()
print(lst)


