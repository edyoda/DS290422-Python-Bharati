# Type Conversion (inbuilt functions)
# 1. int()
# 2. float()
# 3. bool()
# 4. str()
# 5. complex()
# 6. list()
# 7. tuple()
# 8. set()
# 9. dict()

num ="10.90" 
print(type(num))

int_conversion = int(num)
print("Converted into int : ",type(int_conversion),int_conversion)

float_conversion = float(num)
print("Converted into float : ",type(float_conversion),float_conversion)

str_conversion = str(num)
print("Converted into str : ",type(str_conversion),str_conversion)

bool_conversion = bool(num)
print("Converted into bool : ",type(bool_conversion),bool_conversion)


"""
lst = [1,1,1,2,2,4,5,7,3,2,2,5]
print(lst)

# conversion of list (lst) to set to get only unique values
lst1 = set(lst)
print(lst1)

# conversion of set to list to get the unique values in list
lst2 = list(lst1)
print(lst2)
"""


# num = 1
# print(type(num))

# converting to str
# num = str(num)
# print(type(num))

# converting to bool
# num = bool(num)
# print(type(num))

