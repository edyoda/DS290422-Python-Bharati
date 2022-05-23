size = int(input("Enter the size of your list : ")) 

lst = []
for i in range(size): 
    data = input("Enter your element : ")
    lst.append(data)

print("List : ",lst)

lst.reverse()
print(lst)
