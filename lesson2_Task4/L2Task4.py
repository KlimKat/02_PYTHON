d = {} #пустой словарь
d = dict() #пустой словарь

####################
d['q'] = 'hello'
print(d) #выведет {'q' : 'hello'} это значит, что в нашем словаре есть ключ 'q', -->
#--> по которому если мы обратимся, то будем получать 'hello'

####################
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 

print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'} 
print(dictionary['left']) # ← типы ключей могут отличаться 
print(dictionary['up']) # ↑ типы ключей могут отличаться 
dictionary['left'] = '⇐'
print(dictionary['left'])# ⇐
print(dictionary['type'])# KeyError: 'type'
del dictionary['left']# удаление элемента

#####################
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 

del dictionary['left']# удаление элемента
for item in dictionary: 
    print(item) #выведется в столбик up   down   right

#####################
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 

del dictionary['left']# удаление элемента
for item in dictionary:
    print('{}: {}'.format(item. dictionary[item])) #выведется в столбик  up: ↑     down: ↓       right: →

#####################
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 

del dictionary['left']# удаление элемента
for (k, v) in dictionary.items():
    print(k, v) #выведется в столбик  up: ↑     down: ↓       right: →   то есть ключ и значение - k ключ  v значение

#####################
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 

print(dictionary.items())#выводится список, где каждый элемент является кортежем из 2х значений, где первое это ключ, а второе это само значение
