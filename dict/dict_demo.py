# dict

# {key:value} -> item
# dict()
# mutable (key-immutable and value is mutable)
# non-indexed based
# iterable
# duplicates are allowed (key- no duplicates allowed and value- duplicates are allowed)

dict_demo = {1:"Divya",2:"Pankaj",3:"Deep"}
print(dict_demo)

for key,value in dict_demo.items():
    print(key," ",value)

for key in dict_demo:
    print(key)