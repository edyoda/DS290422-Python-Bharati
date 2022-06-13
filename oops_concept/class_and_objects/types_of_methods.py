# instance method : methods which have first parameter as self are known as instance method

class methods:
    college_name = "Edyoda"                  #class/static variable

    def __init__(self,name):                 #instance method
        self.name = name

    def display(self):                       #instance method
        print(f"Hello {self.name}")

    @classmethod
    def set_college_name(cls,college_name):  #class method
        cls.college_name = college_name

    @classmethod
    def get_college_name(cls):               #class method
        return cls.college_name

    @staticmethod
    def age_eligibility():                   #static method
        age = int(input("Enter you age :"))
        if age >= 18:
            print("Eligible to vote!")
        else:
            print("Not eligible to vote")

print(methods.get_college_name())
methods.set_college_name("Coder")
print(methods.get_college_name())
methods.age_eligibility()



    