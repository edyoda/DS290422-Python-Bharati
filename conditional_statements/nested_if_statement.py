# nested if - one if inside another if

age = int(input("Enter your age : "))
experience = int(input("Enter your experience : "))

if age >= 18:
    if experience >= 2:
        print("You are eligible to work in our organisation!")
    else:
        print("You still got to learn alot. Better luck next time!")
else:
    print("You are still a bacchu!")



