no_1 = int(input("Enter a value : "))

# 1 2 3 4 5 6 7 
status = False
if no_1 != 2:
    for i in range(2,no_1): # 2,4
        if no_1 % i == 0:
            status = False
            break
        else:
            status = True
            
    if status:
        print("It is a prime number")
    else:
        print("It is not a prime number")
else:
    print("It is a prime number")



