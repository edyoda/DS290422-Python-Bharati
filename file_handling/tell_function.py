# tell() ---> it will return the current position of the cursor in the file

# file = open("test1.txt","w")
# file.write("Hey All!!!")
# cur_pos = file.tell()
# print("Current Position of Cursor in Write Mode : ",cur_pos)

# file = open("test1.txt","r")
# data = file.read()
# cur_pos = file.tell()
# print("Current Position of Cursor in Read Mode : ",cur_pos)

# file = open("test1.txt","a")
# cur_pos = file.tell()
# print("Current Position of Cursor in Append Mode : ",cur_pos)

file = open("test1.txt","r+")
data = file.read()
cur_pos = file.tell()
print("Current Position of Cursor in r+ Mode : ",cur_pos)

file = open("test1.txt","w+")
cur_pos = file.tell()
print("Current Position of Cursor in w+ Mode : ",cur_pos)

file = open("test1.txt","a+")
cur_pos = file.tell()
print("Current Position of Cursor in a+ Mode : ",cur_pos)