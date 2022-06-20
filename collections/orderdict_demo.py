# OrderedDict
# it is subclass of dict class
# it remembers the order in which the keys were inserted


from collections import OrderedDict

# dict1 = {}
# dict1 = dict()
# dict1["a"] = "A"
# dict1["d"] = "D"
# dict1["c"] = "C"
# dict1["b"] = "B"
# dict1["e"] = "E"

# for key,value in dict1.items():
#     print(key,"  ",value)

# dict1.pop("b")

# dict1["b"] = "B"

# print()

# for key,value in dict1.items():
#     print(key,"  ",value)
# print()

ordered_dict = OrderedDict()
ordered_dict["a"] = "A"
ordered_dict["d"] = "D"
ordered_dict["c"] = "C"
ordered_dict["b"] = "B"
ordered_dict["e"] = "E"

for key,value in ordered_dict.items():
    print(key,"  ",value)

ordered_dict.pop("b")

ordered_dict["b"] = "B"

print()

for key,value in ordered_dict.items():
    print(key,"  ",value)

dict1 = {"c":1}
dict2 = {
    "a":"B",
    "b":"A",
    "d":dict1

}