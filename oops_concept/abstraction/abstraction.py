# Abstraction 
# Abstract Class - a class which has one or more abstract method within it.
# Abstract Method - a method that has declaration but doesnot have any implementation inside it.

from abc import ABC,abstractmethod

class car(ABC): # abstract class
    @abstractmethod #decorator
    def engine(self): # abstract method
        pass
    
    @abstractmethod
    def motor(self):
        pass

    def accelator(self):
        print("Accelator")

# car_obj = car() #TypeError: Can't instantiate abstract class car with abstract methods engine

class maruti(car):
    def engine(self): # override the abstract method , and it will give the implementation to it
        print("Engine")

    def motor(self):
        print("Motor")

    

maruti_obj = maruti()
maruti_obj.engine()
maruti_obj.motor()
maruti_obj.accelator()