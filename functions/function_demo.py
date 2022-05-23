# function

# 1. Reuse the set of code at various places
# 2. to get the output by change a little bot based on different inputs
# 3. to develop clean and maintainable code

# syntax for function

# def fun(): # this is how you define your function
#     # function body
#     #
#     #

# fun() - call your function

def input_for_list():
    size = int(input("Enter the size of your list : ")) 
    lst = []
    for i in range(size): 
        data = input("Enter your element : ")
        lst.append(data)

    print("List : ",lst)

    lst.reverse()
    print(lst)

# input_for_list()

def name_input():
    name = input("Enter your name : ")
    print("Hello ",name)

name_input()

