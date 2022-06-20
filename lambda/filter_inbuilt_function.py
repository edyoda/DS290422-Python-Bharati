num_list = [3,4,1,6,8,3,9]

# def even(lst):
#     lst1 = []
#     for i in lst:
#         if i %2 == 0:
#             lst1.append(i)
#     return lst1

# data = even(num_list)
# print(data)

def even(lst):
    return lst % 2 == 0

data = list(filter(even,num_list))
print(data)