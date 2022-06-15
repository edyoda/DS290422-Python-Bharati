# Generators
# generators are functions
# It is memory efficient
# Do not allocate memory to all the results at the same time
# It yields the data and return the elements of data when it is demanded

def fun(n):
    yield n*2

res = fun(10)
print(f"Result : {next(res)}")

gen = (2*i for i in range(1,11)) # 2,4,6,8,10,12,14,16,18,20
print(next(gen))
print(next(gen))
print(next(gen))
