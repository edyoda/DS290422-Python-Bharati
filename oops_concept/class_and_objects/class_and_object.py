# syntax
# class <class_name> 

# Method - function created inside a class is known as method.

# self keyword - represent 'this' meaning object of current class.

# static / class variable 
# - variable which is define inside the class but outside the method/constructor are known as static/class variable.
# - the scope is within the class.
# - the class/static variables can be called using class name. 
# - for eg. <class_name>.<static/class_variable_name> 
# - all the static variables shares the same memory
# - hence it is used for memory management

kg_of_cemet = 700 # global variable
class building:

    coloring = "sky_blue" # static / class variable

    def rooms(self,no_of_rooms): # passing self keyword is mandatory when creating a method
        print(f"{no_of_rooms} rooms! with {building.coloring} color")

    def doors(self,no_of_doors=20):  # local variable
        print(f"{no_of_doors} doors!")

    def bricks(self):
        no_of_bricks = 100      # local variable
        print(f"{no_of_bricks} Bricks! with {building.coloring} color")

    def cemet(self):
        print(self.windows)
        print(f"{kg_of_cemet} kgs of Cemet")


building_obj = building() # creating object 
building_obj.doors(no_of_doors=30)
building_obj.cemet()
building_obj.rooms(10)
building_obj.bricks()

# when you have not created any constructor in your class , then compiler gives you
# an default constructor


