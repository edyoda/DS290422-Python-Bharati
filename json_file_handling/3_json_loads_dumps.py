import json

# string json obj
json_obj = """{
    "name":"Bharati",
    "female":true,
    "qualification":null,
    "habbit":["writing","reading","coding"]
}"""

# return the json object as a dictionary object
dict_obj = json.loads(json_obj)
print(dict_obj)

# return the dictionary object as a json object
json_obj = json.dumps(dict_obj)
print(json_obj)
