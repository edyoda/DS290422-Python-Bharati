# Set Comprehension - it is used for creating new set from another list,set,tuple.


nums = [19,3,5,63,2,4,6,7,2,1]
even = {i for i in nums if i%2==0}
print(even)