class exception:
    def division(self):
        div = 0
        try:
            no1 = int(input("Enter 1st value : "))
            no2 = int(input("Enter 2nd value : "))
            div = no1/no2
        except Exception as e:
            print(e)

        print(f"Division : {div}")
        print("End of program")

exception_obj = exception()
exception_obj.division()

# ValueError: invalid literal for int() with base 10: 'abc'