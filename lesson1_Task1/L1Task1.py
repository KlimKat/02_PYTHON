#print(5, 6, 8)        коммитим через знак решетки одну строчку

"""
n = 1.89
print(n)

n = 'text'             коммитим через знак двойной ковычки область (в начале области ставим и в конце)
print(n)

n1 = "text"
print(n1)

n = 5
print(type(n))
"""

# n = 'text'           коммитим через выделение области и сочетание клавиш Command + k + c 
# print(type(n))       раскомитить можно через выделение области и сочетание клавиш Command + k + u

# n = 'te\'xt'
# print(n)

# n = 'te"eeeee"xt'
# print(n)

a = 5
b = 5.89
c = 'hello'
#несколько способов, как можно вывести значения переменных, разделенных каким-то знаком, к примеру, знаком девиса
print(a, ' - ', b, ' - ', c)
print(f"{a} - {b} - {c}") 
print("{} - {} - {}".format(a, b, c))