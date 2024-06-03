#Задача: сделать небольшой калькулятор
def calkulator1(a, b):
    return a + b

def calkulator2(a, b):
    return a * b

def math (operation, x, y): #складываем в эту функцию наши операции
        print(operation(x, y))

math(calkulator2, 4, 45)
###################################
# применение lambda
calkulator1 = lambda a, b: a + b

math(calkulator1, 4, 45)
# применение lambda
math(lambda a, b: a + b, 4, 45)
###################################
# применение filter 
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)
###################################
# применение map
list_1 = [x for x in range (1,20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1 ))
print(list_1)
##################################
# применение zip
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)
# применение zip
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)
##################################
# применение enumerate
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)