# Hierarchical Inheritance 
# meaning single parent class and multiple child classes

class country:
    def region(self):
        print("It is a region")

class india(country):
    def language(self):
        print("hindi")

    def game(self):
        print("hockey")

class usa(country):
    def language(self):
        print("english")

    def game(self):
        print("baseball")

india_obj = india()
india_obj.region()
india_obj.language()
india_obj.game()

usa_obj = usa()
usa_obj.region()
usa_obj.language()
usa_obj.game()

#multiple heritance
class Name:
    def Nam_age( self, name, age ):
        print("Under Parent Class 1")
        print("Name : ", name," Age : ", age  )
class Address:
    def add(self, city, district):
        print("Under parent class 2")
        print("City :", city, "district:", district )
class Married (Name, Address):
    def married(self, yes_no ):
        print("inside Maarried Class")
        print( "Married :", yes_no)

emp = Married()
emp.Nam_age( 'suresh', 54)
emp.add ("Mumbai", "Mah")
emp.married("Yes")