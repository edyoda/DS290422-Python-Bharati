from exception_class_9 import InvalidAgeError

class Voting:
    def vote(self,age):
        try:
            if age>=18:
                print("Voting successful!")
            else:
                raise InvalidAgeError()
        except Exception as ex:
            print("Exception : ",ex)

voting = Voting()
age = int(input("Enter your age : "))
voting.vote(age=age)