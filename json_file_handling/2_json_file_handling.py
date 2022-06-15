import json

file = open("DS290422-Python-Bharati\\json_file_handling\\json_demo.json")

# return the json object as a dictionary
data = json.load(file)
print(data)

for k,v in data.items():
    print(k,"   ",v)