# finally - in this block we mention the code which has no relation with 
# exception, meaning the code mentioned in finally block will get executed 
# whether exception has occured or not

# try:
#     div = 10/0
#     print("Division is successful!")
# except Exception as ex:
#     print(ex)
# finally:
#     print("Finally block code")


file = open("demo.txt","w")
try:
    file.write("hii")
    file.close()
except Exception as ex:
    print(ex)
finally:
    print("Finally block : ",file.close())