with open("demo1.txt","w") as file: #file = open("demo1.txt","w")
    file.write("Here we don't have to close the file explicitly!")
    

print(file.closed)



file = open("demo1.txt","w")
file.close()
print(file.closed)