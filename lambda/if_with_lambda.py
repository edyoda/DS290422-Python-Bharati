str1 = "Bharati"

start = lambda x : True if x.startswith('B') else False
print(start(str1))

lst = [4,5,6,7,3,8,9,5]

data = list(map(lambda lst : "Even num" if lst % 2 == 0 else "odd number",lst))
print(data)
