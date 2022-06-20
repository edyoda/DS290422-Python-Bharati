import requests

url = "http://ip.jsontest.com/"

response = requests.request('GET',url=url).json()
print(response)

print(type(response))


