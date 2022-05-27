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

# The from_where argument is set to 0 by default. 
# Therefore, the reference point cannot be set to the current position or end position, 
# in the text mode, except when the offset is equal to 0.

file = open("seek_demo.txt","wb")
# file.write("Hello Programmers!!!!!!!")
cur_pos = file.tell()
print("Before changing the position : ",cur_pos)
file.seek(4,1) 
cur_pos = file.tell()
print("After changing the position : ",cur_pos)
file.close()



