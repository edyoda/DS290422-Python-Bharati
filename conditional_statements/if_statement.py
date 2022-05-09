# Conditional Statement (Decision Maker, Decision Statement)

"""
1. if statement
2. else if statement
3. elif statement
4. ladder statement
5. nested if statement
"""

age = int(input("Please tell us your age to understand whether you are eligible to vote or not : "))

# indentation -> 4 spaces / 1 tab
print(age >= 18)

# if statement
if age >= 18:
    # this body will get executed if the condition returns True
    print("You are eligible to Vote")


print("End of the program...")

