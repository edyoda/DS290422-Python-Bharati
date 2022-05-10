age = int(input("Enter your age : "))
experience = int(input("Enter your experience : "))
qualification = int(input("Enter your qualification : "))
# if age >= 18:
#     if experience >= 2:
#         print("You are eligible to work in our organisation!")
#     else:
#         print("You still got to learn alot. Better luck next time!")
# else:
#     print("You are still a bacchu!")

if age >= 18 and experience >= 2 or qualification >= 12:
    print("You are eligible to work in our organisation!")
else:
    print("You are not eligible to work in our organisation!")