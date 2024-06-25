from time import time

def deco(func):
    def wrapper(*args):
        t1 = time()
        res = func(args[0], args[1])
        t2 = time()
        return res, t2 - t1
    return wrapper

def calc(a, b):
    return a + b

print(calc(2, 3))
print (deco(calc)(2, 3))