# Задача No1. 
# За день машина проезжает n километров. 
# Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 
# Output: 2

n = int(input())
m = int(input())

print((m + n - 1) / n) #+n чтобы числа, не кратные друг другу, считались корректно, а -1, чтобы при этом условии еще и числа кратные считались корректно