# Counter
# is a sub-class of dict class
# it will consider key as element
# and values as count of that element

# ["C","A","B","B","A","A","A"]
# A = 4
# B = 2
# C = 1

import code
from collections import Counter

counter_demo = Counter(["C","A","B","B","A","A","A"])
print(counter_demo)

counter_demo1 = Counter(A=4, B=2, C=1)
print(counter_demo1)

counter_demo1 = Counter({"A":4,"B":2,"C":1})
print(counter_demo1)