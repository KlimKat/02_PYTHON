# Задача 18: 
# Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих строках 
# записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6 # 5

list_1 = [1, 2, 3, 4, 5]
k = 6

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
