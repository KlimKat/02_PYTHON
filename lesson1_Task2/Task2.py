"""
#если написать просто input(), то консоль попросит ввести значение, но не сохранит его, чтобы сохранила, нужно присвоить переменную
#в нашем случае переменная а; чтобы было понятно пользователю, что нужно делать, выведем запрос на ввод значения с консоли
print('Введите первое число: ')
a = input()
#print(a) #если уберем эту сстроку, то вводимое число никуда не будет выведено на экран после введения с консоли

#можно еще так
b = input('Введите второе число: ')

#выводим сумму строк (т.е. если введешь 12 и 34, то выведется 12  +  34  =  1234)
print(a, ' + ', b, ' = ', a + b)
"""

"""
#переводим число с точкой в целое значение
c = 5.89
print(c)
print(type(c)) #это просто чтобы на консоли было видно, как меняется тип числа с float на int

c = int(c)
print(c)
print(type(c))
"""

"""
#теперь мы можем складывать между собой строки одного типа str допустим: было 5.89 стало 5.8989
c = 5.89
print(c)
print(type(c)) #это просто чтобы на консоли было видно, как меняется тип числа с float на int

c = str(c)
print(c + '89') #строчный тип пишем с апострофами
print(type(c))
"""

#теперь можем исправить изначальный код, чтобы получилось сложить числа, в не строки
print('Введите первое число: ')
a = int(input())
b = int(input('Введите второе число: '))


print(a, ' + ', b, ' = ', a + b)