"""
a = 5.12345
b = 6.12345
#print(a*b) #будет длинное число, с большим кол-вом знаков после запятой
print(round(a*b, 3)) #будет оставаться 3 знака после запятой
"""
"""
#операции с данными какие бывают в Питоне
iter = 2
iter += 3 #iter = iter + 3
iter -= 4 #iter - 4
iter *= 5 #iter *  5
iter /=5 #iter / 5
iter //= 5 #iter // 5
iter %= 5 #iter % 5
iter **= 5 #iter ** 5
"""
#логические операции в Питоне
a = 1 > 4
print(a)

a = 1 < 4 and 5 > 4
print(a)

a = 1 == 2 #это знак равенства
print(a)

a = 1 != 2 #это знак неравенства
print(a)

a = 'hello'
b = 'hello'
print(a == b)

a = 1 < 3 < 5 < 10
print (a)
