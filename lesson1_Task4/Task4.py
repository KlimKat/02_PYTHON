"""
if condition:
     # operator 1
     # operator 2
     # ...
     # operator n
 else:
     # operator n + 1
     # operator n + 2
     # ...
     # operator n + m
"""

"""
#Ещё один вариант использования операторов else-if → в связке с elif (else if)
#Проверяем первое условие, если оно не выполняется, проверяем второе и так далее. 
#Как только будет найдено верное условие, все остальные будут игнорироваться.
 if condition1:
     # operator
 elif condition2:
     # operator
 elif condition3:
     # operator
 else:
     # operator
"""

"""
#Сложные условия создаются с помощью логических операторов, таких как: and, or, not
#if condition1 and condition2: # выполнится, когда оба условия окажутся верными # operator
#if condition3 or condition4: # выполнится, когда хотя бы одно из условий окажется верным # operator
#пример ниже:

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждал Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - ТОП :)')
else:
    print('Привет, ', username)
"""

"""
#while condition:
    # operator 1
    # operator 2
      # ...
      # operator n

n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa) # 9
"""

"""
#while-else
 #while condition:
      # operator 1
      # operator 2
# ...
       # operator n
 #else:
       # operator n + 1
       # operator n + 2
       # ...
       # operator n + m
#Блок else выполняется, когда основное тело цикла перестает работать самостоятельно. 
#А разве кто-то может прекратить работу цикла? Если мы вспомним C#, то да и это конструкция break.

i = 0
while i < 5:
    if i == 3: # если убрать условие
        break # то выведется только Пожалуй хватит 5
     i = i +1
else:
     print('Пожалуй')
     print('хватит )')
print(i)
"""

"""
#break лучше не использовать, вместо него ставят обычно флажки flag
#Задача: Пользователь вводит число, необходимо найти минимальный делитель данного числа
#Решение: 
n = int(input())
flag = True
i = 2 
while flag:
    if n % i == 0:# если остаток при делении числа n на i равен 0 
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1
"""

