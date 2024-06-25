from time import time

def deco(func):
    def wrapper(*args):
        t1 = time()
        res = func(args[0], args[1])
        t2 = time()
        return res, t2 - t1
    return wrapper

@deco  #синтаксический сахар - можно оборачивать без него (в след файле пример как можно без него)
def calc(a, b):
    return a + b

print(calc(2, 3))



# t1 = time()
# print(calc(2, 3))

# t2 = time()
# print(t2 - t1)


