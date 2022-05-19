size = int(input("Enter the size of your list : ")) 

lst = []
for i in range(size): 
    data = int(input("Enter your element : "))
    lst.append(data)

print("List : ",lst)

new_lst = []
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] == lst[j] and lst[i] not in new_lst:
            new_lst.append(lst[i])

print(new_lst)
