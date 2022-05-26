# seek() ---> helps to change the position of the cursor in file
# seek(offset,from_what)
# offset - no. of positions to move forward
# from_what - point of reference

# from_what accepts below 3 values
# 0 - beginning of the file
# 1 - current position of cursor
# 2 - end of the file
# bydefault from_what is 0

# -ve ----> it will move towards left
# +ve ----> it will move towards right

# Seek()function with negative offset only works when file is opened in binary mode. 

file = open("seek_demo.txt","rb")
# file.write("Hello Programmers!!!!!!!")
cur_pos = file.tell()
print("Before changing the position : ",cur_pos)
file.seek(-10,2) 
cur_pos = file.tell()
print("After changing the position : ",cur_pos)



