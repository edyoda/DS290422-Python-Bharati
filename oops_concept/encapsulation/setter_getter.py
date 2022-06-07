from encapsulation import car

car_obj = car("diesel engine","12000 cc","BMW","35km per liter")
car_obj.display() 

car_obj.set_engine("petrol engine")
engine = car_obj.get_engine()
print(engine)