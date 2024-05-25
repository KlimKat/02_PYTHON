colors = {'red', 'green', 'blue'} #множество
colors = set() #множество
print(colors) # {'red', 'green', 'blue'} или вообще в рандомном порядке выдает

######################
colors = {'red', 'green', 'blue'} #множество

colors.add('red')
print(colors) # {'red', 'green', 'blue'}  значение не добавилось потому что такое уже есть а множество содержит набор уникальных значений

colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'} или вообще в рандомном порядке выдает все слова каждый раз при запуске программы

colors.remove('red')
print(colors) # {'green', 'blue','gray'} 
colors.remove('red') # KeyError: 'red' так как уже нет этого значения 
colors.discard('red') # ok  так как эта функция проверяет есть ли это значение 
#и если есть удаляет его если нет то пропускает эту строку кода и не выдает ошибку

colors.clear() #{} очищает полностью все множество
print(colors) #set() выводит пустое множество

#######################
#Операции со множествами в Python:
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                                #c = {1, 2, 3, 5, 8}
u = a.union(b)                              #u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)                       #i = {8, 2, 5}
dl = a.difference(b)                        #dl = {1, 3}
dr = b.difference(a)                        #dr = {13, 21}
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

########################
a = {1, 2, 3, 5, 8}
b = frozenset(a) #замороженное множество (неизменяемое)
print(b) # frozenset({1, 2, 3, 5, 8})

