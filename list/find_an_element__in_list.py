size = int(input("Enter the size of your list : ")) 

lst = []
for i in range(size): 
    data = int(input("Enter your element : "))
    lst.append(data)

print("List : ",lst)


element = int(input("Enter the element you want to search inside list : "))

for i in lst:
    if i == element:
        status = True 
        break
    else:
        status = False

if status:
    print("Element exist!!!")
else:
    print("Element doesnot exist!!!")

