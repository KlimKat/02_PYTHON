#Задача
#В списке хранятся числа. Нужно выбрать только чётные числа 
#и составить список пар (число; квадрат числа).
# Пример: 
# 1 2 3 5 8 15 23 38 
# Получить: 
# [(2, 4), (8, 64), (38, 1444)]

#Решение 1
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# result = list()

# for i in data:
#      if i % 2 == 0:
#           result.append((i, i**2))

# print(result)


#Решение 2: другой способ
# def select(f, col):
#      return [f(x) for x in col]

# def where(f, col):
#      return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# result = select(int, data)
# print(result)

# result = where(lambda x: x % 2 == 0, result)
# print(result)
# #теперь нужно возвести в квадрат
# result = list(select(lambda x: (x, x**2), result))
# print(result)

#Решение 3: способ без select но с map
# def where(f, col):
#      return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# result = map(int, data)
# print(result)

# result = where(lambda x: x % 2 == 0, result)
# print(result)

# result = list(map(lambda x: (x, x**2), result)) #теперь нужно возвести в квадрат
# print(result)

#Решение 4: без where но с filter 
data = [1, 2, 3, 5, 8, 15, 23, 38]
result = map(int, data)
result = filter(lambda x: x % 2 == 0, result)
result = list(map(lambda x: (x, x ** 2), result))
print(result)


