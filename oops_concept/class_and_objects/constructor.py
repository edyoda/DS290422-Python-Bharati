# Constructor
# are methods which have same name as class name
# this is defined using __init__()
# it is used to initialise instance variables
# it is also used to create object
# you don't have to explicity call constructor, it gets called when you create an object

# NOTE : It is note recommended to write business logic inside constructor.

# Types of Constructor
# 1. Default Constructor - this is provided by compiler when you don't create a constructor in your class
# 2. Zero Constructor - are constructors without any parameter
# 3. Parameterized Constructor - are constructors with parameters


# instance - another name for object

# instance variable 
# - variable which are define with self keyword as prefix are known as instance variable
# - for eg. self.<variable_name>
# - this variable can be called using object
# - it is defined inside a constructor / method
# - throughout the class
# - for every instance variable a seperate memory is allocated

class constructor:
    def __init__(self,name,rno): #constructor
        self.name = name # instance variable
        self.rno = rno

    def display(self):
        print(f"Hi {self.name}, your roll no is {self.rno}")

constructor_obj = constructor("Bharati",14)
constructor_obj.display()
print(constructor_obj.name)
# constructor_obj1 = constructor()
# constructor_obj2 = constructor()
