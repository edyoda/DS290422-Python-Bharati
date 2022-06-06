# str1 = "Python"
# dict_comp = {i.upper():i.lower()  for i in str1}
# print(dict_comp)

# keys=[1,2,3,4]
# values=[7,3,5,7]
# dictionary={k:v for k,v in zip(keys,values)}
# print(dictionary)

# given =  [5,6,7,3,2,4,7]
# new_dict = {i:i**3 for i in given}
# print(new_dict)

numbers=[1,2,3,4,5,6,7,8]
dictionary={i:[i*j for j in range(1,11)] for i in numbers}
print(dictionary)

lst = [1,3,5,7,8,43,6,8]
lst1 = [8,5,3,2,2,4,6,8]
lst = [3,5,8]

# lst1={1,3,5,7,8,43,6,8}
# lst=[1,2,3,4,6,72,24,56,7,4]
# lst1=[1,4,6,8,0,8,4,99,45,33]
# common=set(filter(lambda lst:True if lst in lst1 else False,lst))
# print(common)

# lst1 = [1,3,5,7,8,49,6,8]
# lst2 = [8,5,3,2,2,4,6,8]
# result = list(filter(lambda i:i in lst1,lst2))
# print("new value",result)

# lst=[1,3,5,7,8,43,6,8]
# lst1=[8,5,3,2,2,4,6,8]
# lst={i for i in lst if i in lst1}
# print(lst)

# lst=[4,6,8,1,2]
# lst1=[9,7,8,5,3,4,2]
# set1={i for i in lst}
# set2={i for i in lst1}
# data=lambda l1,l2:l1.intersection(l2)
# print(data(set1,set2))
