# num1 = (1,2,3)
# num2 = (1,2,3)
# print(num1 is num2)


# num1 = [1,2,3]
# num2 = [1,2,3]
# print(num1 is num2)


# num1 = {1,2,3}
# num2 = {1,2,3}
# print(num1 is num2)

a = (1,2,3)

b = (1,2,3)

print(id(a[0]) == id(b[0]))
