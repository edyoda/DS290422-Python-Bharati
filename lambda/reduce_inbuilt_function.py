from functools import reduce

num_list = [4,3,5,10,3,2]

# def sum(lst):
#     add = 0
#     for i in lst:
#         add += i
#     return add

# data = sum(num_list)
# print(data)

def sum(lst,lst1):
    return lst + lst1

data = reduce(sum,num_list)
print(data)