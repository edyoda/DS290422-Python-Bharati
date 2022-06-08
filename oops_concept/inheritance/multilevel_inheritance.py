class grandpa():
    def fields(self):
        print("Fields!")

class dad(grandpa):   
    def flat(self):
        print("Flat")

    def car(self):
        print("Car")

class son(dad):   
    def bike(self):
        print("Bike")

    def mobile(self):
        print("Mobile")

son_obj = son()
son_obj.bike()
son_obj.mobile()
son_obj.flat()
son_obj.car()
son_obj.fields()