# Deque
# it is open from both the ends
# you can add the element from both the ends
# you can delete the element from both the ends

from collections import deque

deque_demo = deque([1,2,3,4,5])

print(deque_demo)

print(deque_demo[3])

# deque_demo.append(10)
# print(deque_demo)

# deque_demo.appendleft(70)
# print(deque_demo)

deque_demo.pop()
print(deque_demo)

deque_demo.popleft()
print(deque_demo)

