# ChainMap
# it is used to combine number of dictionary together.
# it returns list of dictionary

from collections import ChainMap

dict1 = {"a":"A","b":"B"}
dict2 = {"c":"C","d":"D"}
dict3 = {"e":"E","f":"F"}

chain_map = ChainMap(dict1,dict2,dict3)

print(chain_map)

print(chain_map['c'])

print(chain_map.values())

print(chain_map.keys())

dict4 = {"g":"G","h":"G"}

chain_map1 = chain_map.new_child(dict4)

print(chain_map1)




