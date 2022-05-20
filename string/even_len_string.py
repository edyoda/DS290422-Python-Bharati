str1 = "Python is a high level programming language"
str2 = str1.split()
oddsum = ""
evensum = ""
for index in str2:
    if len(index) % 2 == 0:
        evensum += index + " "
    else:
        oddsum += index + " "

print("even length : {}".format(evensum))
print("odd length : {}".format(oddsum))
