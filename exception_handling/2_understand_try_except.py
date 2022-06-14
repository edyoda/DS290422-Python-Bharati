from __future__ import division


class exception:
    def division(self):
        div = 0
        no1 = int(input("Enter 1st value : "))
        no2 = int(input("Enter 2nd value : "))
        try:
            div = no1/no2
        except Exception as e: 
            print(e)

        print(f"Division : {div}")
        print("End of program")

    def divide(self):
        self.division()



exception_obj = exception()
exception_obj.divide()

# pvm will call it's Default Exception Handler