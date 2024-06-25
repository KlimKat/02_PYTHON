# Задача 38: 
# Дополнить телефонный справочник возможностью 
# изменения и удаления данных. Пользователь также 
# может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных.

from logger import input_data, print_data, edit_data, delete_data

def interface():
    print("Добрый день! Вы попали на специальный бот-справочник от GB! \n 1 - запись данных \n 2 - вывод данных \n 3 - редактирование данных \n 4 - удаление данных")
    command = int(input('Введите 1, 2, 3 или 4 и выберете действие'))

    while command not in [1, 2, 3, 4]:
        print('Такой команды не существует, введите 1, 2, 3 или 4')
        command = int(input('Введите 1, 2, 3 или 4 и выберете действие'))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        edit_data()
    elif command == 4:
        delete_data()
    
    

