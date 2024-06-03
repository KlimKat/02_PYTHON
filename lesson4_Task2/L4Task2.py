# Задача: 
# C клавиатуры вводится некий набор чисел, 
# в качестве разделителя используется пробел. 
# Этот набор чисел будет считан в качестве строки. 
# Как превратить list строк в list чисел?


#Решение из презентации
# def where(f, col):
#      return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

#Решение из видео
data = '1 2 3 5 8 15 23 38'
data = list(map(int, data.split()))
print(data)
