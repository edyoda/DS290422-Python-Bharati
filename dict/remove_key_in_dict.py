dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# dict1.pop(3)
# print(dict1)

# for i in list(dict1):
# 	dict1.pop(i)

# print(dict1)

dict = {'name': 'foo', 'age': 28}
k = list(dict.keys())
for key in k:
  del dict[key]
print(dict)
