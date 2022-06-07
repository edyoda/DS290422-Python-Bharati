# Encapsulation
# - it is used to bind the attributes and behaviour together into a single unit
# - using setter and getter

class car:

    def __init__(self,engine,power,brand,mileage):
        self.engine = engine
        self.power = power
        self.brand = brand
        self.mileage = mileage

    def set_engine(self,engine): #setter
        self.engine = engine
    
    def set_power(self,power): #setter
        self.power = power
    
    def set_brand(self,brand): #setter
        self.brand = brand
    
    def set_mileage(self,mileage): #setter
        self.mileage = mileage

    def get_engine(self):   #getter
        return self.engine
    
    def get_power(self):
        return self.power

    def get_brand(self):
        return self.brand

    def get_mileage(self):
        return self.mileage

    def __str__(self):
        return f"Engine : {self.engine} \nPower : {self.power} \nBrand : {self.brand} \nMileage : {self.mileage} "

if __name__ == "__main__":

    car_obj = car("diesel engine","12000 cc","BMW","35km per liter") 
    print(car_obj)

    print("\n")

    car_obj.set_engine("petrol engine")
    car_obj.set_brand("Ferrari")
    car_obj.set_power("10000 cc")
    car_obj.set_mileage("50km")
    print(car_obj)

    print("\n")

    engine = car_obj.get_engine()
    print(f"Engine : {engine}")