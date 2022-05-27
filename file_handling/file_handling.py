# File Handling
# It is used to store data permanently in the file.

# Types of File
# Text file - for storing text data
# Binary file - for storing images,videos,etc

# Modes for Text file
# r -> read mode ---> bydefault mode, used to read the data from file
# w -> write mode ---> overrides existing file or creates the file if it doesn't exist and then open it in write mode
# a -> append mode ---> creates the files and append the data to the existing data
# r+ -> read/write ---> it will allow you to read/write the data, but it will not override the existing file and not gonna create a new file
# w+ -> write/read ---> it allows to read/write the data and it also overrides the file and creates the file 
# a+ -> append/read ---> it allows to read/append the data and also creates the file if it doesn't exist

# Modes for Binary file
# rb
# wb
# ab
# rb+
# wb+
# ab+

# write mode
# open(file_name,mode)
# file = open("demo.txt",'w') #bydefault mode value is 'r'
# file.write("This is my first file!")
# file.write("End of File")
# file.write("Writing something")

# read mode
# file = open("demo.txt",'r')
# data = file.read()
# print(data)

# append mode
# file = open("demo1.txt","a") 
# file.write("Hii all!")
# file.write("How you'll are doing?")

# r+ mode
# file = open("demo2.txt","r+") 
# file.write("Hello")

# w+ mode
# file = open("demo2.txt","w+") 
# file.write("Hello")
# file.write("Hiii")
# data = file.read()
# print(data)

# a+ mode
# file = open("demo2.txt","a+") 
# #file.write("Hii")
# #file.write("Hello")
# data = file.read()
# print(data)

file = open("demo2.txt","w+") 
file.write("Hello")
file.write(" I am keshav ")
cur_position = file.tell()
print("current curser position is : ",cur_position)
file.seek(0)
new_position = file.tell()
print("curser position : ",new_position)
data = file.read()
print(data)
