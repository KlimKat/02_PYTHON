# Задача 30: 
# Заполните массив элементами арифметической 
# прогрессии. Её первый элемент, разность и 
# количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d. Каждое число вводится с новой строки.
# Пример:
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
# Ввод:
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# Вывод:
# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

for i in range(len(list_1)):
  if min_number <= list_1[i] <= max_number:
    print(i)


