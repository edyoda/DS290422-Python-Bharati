try:
    print(10/0)
    str1 = None
    length = len(str1)
    print(length)
except ZeroDivisionError as ex:
    print(10/2)
except ValueError as  ex:
    print(ex)
except Exception as ex:
    print(ex)

print("End of program")