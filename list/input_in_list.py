size = int(input("Enter the size of your list : ")) #5

lst = []
for i in range(size): #3
    data = input("Enter your element : ")
    lst.append(data)

print("List : ",lst)

lst.reverse()
print(lst)
