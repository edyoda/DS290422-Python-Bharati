file = open("demo1.txt","w") 
# data = file.read()   # reads the whole data
# print("Read Function:", data)

# data = file.readline() # reads only the first line
# print("Readline Function :",data)

# data = file.readlines() # returns list of lines
# print("Readlines Function : ",data)

# for i in file:
#     print(i)

# data = file.read(6) #starts with 1
# print(data)

# file.write("Python is programming language")
# file.write("Today is Friday!")

data = ["Python is programming language","Today is Friday!","Tomorrow is weekend"]
file.writelines(data) # used to write list of lines in the file
file.close()