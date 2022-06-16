import requests

url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"

response = requests.request('GET',url=url).json()
print(response)
# print(response.text)

"""
[
  {
    'name': 'Harry Potter',
    'city': 'London'
  },
  {
    'name': 'Don Quixote',
    'city': 'Madrid'
  },
  {
    'name': 'Joan of Arc',
    'city': 'Paris'
  },
  {
    'name': 'Rosa Park',
    'city': 'Alabama'
  }
]
"""

print(type(response))
print(response[3]['city'])
print(response[-1]['city'])


