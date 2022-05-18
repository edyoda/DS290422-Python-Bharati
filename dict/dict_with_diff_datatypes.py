dict1 = {
    "name":"Bharati",
    "address":"Navi Mumbai",
    "languages":["C","C++","Java","Python",[1,1,2,3,4]],
    "abc":(1,2,3,4)
}
# print(dict1)
# print(type(dict1))
# print(type(dict1["name"]))
# print(type(dict1["languages"]))
print(dict1["languages"][4][2])

# lst = dict1["languages"].copy()
# print(lst)