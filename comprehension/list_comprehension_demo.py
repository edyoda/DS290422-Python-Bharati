# List Comprehension - it is used for creating new list from another list. 

# for i in lst:
#     if condition:
#         expression

# syntax
# new_lst = [expression for i in lst if condition]

# nums = [1,3,4,5,6]

# lst = []
# for i in nums:
#     lst.append(i)
# print(lst)

# lst = [i for i in nums]
# print(lst)


nums = [10,4,2,6,8,3,2,4,7,8]

even = []
for i in nums:
    if i%2 == 0 :
        even.append(i)

print(even)

even = [i for i in nums if i%2 == 0]
print(even)



# Python
# ['P','y','t','h','o','n']
string="Python"
lst=[i for i in string]
print(lst)

str1 = ["Bharati","Deepshika","Basit","Vashu","Ram","Savita","Bharat"]
lst = [i for i in str1 if i.startswith('B') and len(i)>5]
print(lst)
