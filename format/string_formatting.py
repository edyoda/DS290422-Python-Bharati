name = input("Enter your name : ")
qualification = input("Enter your qualification : ")

# # Your name is ..... and your qualification is .....
# print("Your name is ",name, "and your qualification is ",qualification)

# format() # inbuilt function
# Default Order
# str1 = "Your name is {} and your qualification is {}".format(name,qualification)
# print(str1)

# Positional Formatting
# str1 = "{3} {0} {1} {2}".format("Zero","One","Two","Three")
# print(str1)

# Keyword Formatting
# str1 = "{a} {b} {c}".format(c="cat",a="apple",b="ball")
# print(str1)

# String alignment
# str1 = "|{:<10}|{:^10}|{:>10}|".format("left","center","right")
# print(str1)

# F string
# str1 = f"Your name is {name} and your qualification is {qualification}"
# print(str1)