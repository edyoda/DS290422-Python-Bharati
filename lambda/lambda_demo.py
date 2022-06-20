# Lambda Expression / Function - it is a anonymous function 
# it is a function without a name
# it can have any number of arguments but can have only one expression (condition)

# Function
# here we need to define the name for the function
# here we need to define the return statement
# cannot be define it as a parameter in any inbuilt function
# complex

# Lambda Function
# no name is required
# here no need of return statement
# can be define it as a parameter in any inbuilt function
# it is single line code
# simple

def myfunction(a,b):
    return a+b

# data = myfunction(4,5)
# print(data)

# syntax :-   lamda <argument1,argument2> : <expression>
data = lambda a,b : a + b
print(data(4,5))
