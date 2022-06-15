import memory_profiler as mem

def gen(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

print(f"Before calling function : {mem.memory_usage()} MB.")
gen(100000000)
print(f"After calling function : {mem.memory_usage()} MB.")




def gen(n):
    lst = []
    for i in range(n):
        yield i

print(f"Before calling function : {mem.memory_usage()} MB.")
gen(100000000)
print(f"After calling function : {mem.memory_usage()} MB.")