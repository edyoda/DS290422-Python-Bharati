no_1 = int(input("Enter a value to find it's length : "))

# 654 = 3 | 784563 = 6 

# length = len(no_1) # inbuilt function
# print("Length : ",length)

# 654 = 3

# mod = no_1 % 10 # 4
# print("Modulus : ", mod)
# no_1 = no_1//10
# print("Division : ",no_1)
# mod = no_1 % 10 # 4
# print("Modulus : ", mod)
# no_1 = no_1//10
# print("Division : ",no_1)
# mod = no_1 % 10 # 4
# print("Modulus : ", mod)
# no_1 = no_1//10
# print("Division : ",no_1)
count = 0
while no_1!=0:
    mod = no_1 % 10 # to get the last digit
    no_1 //= 10 # to get the values left once the last digit is removed
    count += 1 #3

print("Count : ",count)


