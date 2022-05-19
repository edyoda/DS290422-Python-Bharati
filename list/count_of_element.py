
# lst=[1,2,2,4,5,6,6,7,8,9,4]
# dup=[]

# for i in lst:
#     dup.append(i)
        
# print(lst)
# print(dup)


size= int(input("Enter the size of your list:"))

lst=[]
for i in range(1,size+1):
    data=int(input("Enter your value:"))
    lst.append(data)

print("List:",lst)
lst2=lst
print(lst2)


