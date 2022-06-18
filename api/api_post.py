from sre_constants import SUCCESS
import requests

url = "https://jsonplaceholder.typicode.com/todos"

request_data = {"userId": 1, "title": "Buy milk", "completed": False}
# response = requests.post(url, json=request_data)
response = requests.request("POST",url,json=request_data)
print(response.json())
print(response.status_code)

# 202/201 - SUCCESS
# 404 - Not Found
# 500 - Server Error
# the apis which uses json - Rest API
# the apis which uses xml - Soap API