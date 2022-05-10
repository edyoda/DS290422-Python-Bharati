
# we have to find the greatest value between below two values

no_1 = int(input("Enter your first number : "))
no_2 = int(input("Enter your second number : "))

if no_1 > no_2:
    print(no_1," meaning no1 is greater than no2 i.e ",no_2)
elif no_2 > no_1: 
    print(no_2," meaning no2 is greater than no1 i.e ",no_1)
elif no_1 == no_2:
    print("Both the values are same")
else:
    print("As all the above conditions are not satisfied. Hence I am getting printed")

