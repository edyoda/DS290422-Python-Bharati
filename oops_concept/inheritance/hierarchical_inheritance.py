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