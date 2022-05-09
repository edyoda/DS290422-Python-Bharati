# Logical Operator
# 1. and - returns True if both statements are true
# 2. or - returns True if one of the statement is true
# 3. not - reverse the output, it returns False is the output is True

num1 = 10
num2 = 20
num3 = 30

# and operator
is_true = num1 is not num2 and num1 is not num3
print(is_true)

# or operator
is_true = num1 is num2 or num1 is not num3
print(is_true)

# not operator
is_true = not(num1 is num2 or num1 is not num3)
print(is_true)