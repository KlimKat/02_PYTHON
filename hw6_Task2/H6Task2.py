# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Пример:
# a1 = 2
# d = 3
# n = 4
# На выходе:
# 2
# 5
# 8
# 11

a1 = 2
d = 3
n = 4

for i in range(n):
  print(a1 + i * d)
