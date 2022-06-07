# Single Inheritance - means where we have single parent class and single child class

class dad:   # parent class
    def flat(self):
        print("Flat")

    def car(self):
        print("Car")

class son(dad):   # child class
    def bike(self):
        print("Bike")

    def mobile(self):
        print("Mobile")

son_obj = son()
son_obj.bike()
son_obj.mobile()
son_obj.flat()
son_obj.car()