# Задача 2:
# Найдите сумму цифр трехзначного числа
# Пример:
# 123 -> 6 (1 + 2 + 3) 
# 100 -> 1 (1 + 0 + 0)

print('Введите трехзначеое число: ')
num = int(input())


if 100 <= num <= 999: # Проверяем, что число является трехзначным
    num_str = str(num) # Преобразуем число в строку, чтобы можно было работать с каждой цифрой
    hundreds = int(num_str[0])
    tens = int(num_str[1])
    units = int(num_str[2])
    result = hundreds + tens + units
    print(f"{num} -> {result} ({hundreds} + {tens} + {units})")
else:
    print('Число должно быть трехзначным')