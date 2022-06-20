file = open("test.txt","w")
file.close()  #! VERY VERY IMPORTANT TO CLOSE THE FILE

mode = file.mode
print("Mode : ",mode)

file_name = file.name
print("File name : ",file_name)

is_close = file.closed
print("Closed : ",is_close)