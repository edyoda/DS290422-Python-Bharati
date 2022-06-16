import json

file = open("DS290422-Python-Bharati\\json_file_handling\\json_demo.json")

# return the json object as a dictionary object (w.r.t file)
data = json.load(file)
print(data)

# for k,v in data.items():
#     print(k,"   ",v)

# return the dictionary object as a json object (w.r.t file)
file1 = open("DS290422-Python-Bharati\\json_file_handling\\dump.json","w")
result = json.dump(data,file1)


