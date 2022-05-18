size = int(input("Enter the size of your list : ")) 

lst = []
for i in range(size): 
    data = input("Enter your element : ")
    lst.append(data)

print("List : ",lst)

# lst1 = []
# for i in range(len(lst)): # []
#     lst1.insert(i,lst[-1]) # 0=3, 1=2, 2=1
#     lst.pop(-1)            # 1

lst1 = []
length = len(lst)
while length>0: #3
    lst1.append(lst[length-1])
    length -= 1

print(lst1)



