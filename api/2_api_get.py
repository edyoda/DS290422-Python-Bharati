import requests

# url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"
url = "http://api.zippopotam.us/us/90210"

# response = requests.request('GET',url=url).json()
# print(response)
# print(response.text)

response = requests.get(url).json()
print(response)

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

# print(type(response))
# print(response[3]['city'])
# print(response[-1]['city'])


