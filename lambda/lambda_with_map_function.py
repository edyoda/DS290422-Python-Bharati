num_list = [5,4,6,7,3,7,8]

# def square(num_list):
#     lst1 = []
#     for i in num_list:
#         i = i ** 2
#         lst1.append(i)
#     return lst1

# data = square(num_list)
# print(data)

# def square(lst):
#     return lst ** 2

# data = list(map(square,num_list))
# print(data)

data = list(map(lambda lst:lst**2, num_list))
print(data)
