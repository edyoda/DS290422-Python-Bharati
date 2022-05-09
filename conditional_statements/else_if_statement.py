age = int(input("Please tell us your age to understand whether you are eligible to vote or not : "))

print(age >= 18)

if age >= 18:
    # this body will get executed if the condition returns True
    print("You are eligible to Vote")
else:
    # this body will get executed if the condition returns False
    print("You are not eligible to Vote")


print("End of the program...")