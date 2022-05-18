size = int(input("Enter the size of your list : ")) 

lst = []
for i in range(size): 
    data = int(input("Enter your element : "))
    lst.append(data)

print("List : ",lst)

# sum = 0
# for i in lst:
#     sum += i #sum = sum + i

sum = 0
for i in range(len(lst)): #3 - 0,1,2
    sum += lst[i]

print(sum)