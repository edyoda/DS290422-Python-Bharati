lst = [5,1,6,10,8,9]

for i in range(len(lst)): #0
    for j in range(i+1,len(lst)): #1

        if lst[i] > lst[j]:

            temp = lst[i] 

            lst[i] = lst[j] 

            lst[j] = temp 

print("Sorted List : ",lst)
print("Smallest Value : ",lst[0])
print("Largest Value : ",lst[-1])
