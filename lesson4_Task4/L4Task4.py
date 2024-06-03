# Файлы (примеры использования различных режимов в коде)
#режим a
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')# здесь указываем режим, в котором будем работать 
data.writelines(colors)# разделителей не будет
data.close()
# режим a
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
# режим r
path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()
# режим w
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w') 
data.writelines(colors)# разделителей не будет 
data.close()