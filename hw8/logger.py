from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"Какой вид отображения данных записать?\n\n"
                    f"Вариант 1: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"Вариант 2: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Введите в консоль 1 или 2 для выбора варианта: "))
    
    while var != 1 and var != 2:
        print('Такой команды не существует, введите 1 или 2')
        var = int(input('Введите 1 или 2 и выберете действие'))

    if var == 1:
        with open('/Users/kit/Desktop/02_PYTHON/hw8/data_first_variant.csv', 'a', encoding= 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n")
    elif var == 2:
        with open('/Users/kit/Desktop/02_PYTHON/hw8/data_second_variant.csv', 'a', encoding= 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('/Users/kit/Desktop/02_PYTHON/hw8/data_first_variant.csv', 'r', encoding= 'utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = 1
        print(''.join(data_first_list))


    print('Вывожу данные из 2 файла: \n')
    with open('/Users/kit/Desktop/02_PYTHON/hw8/data_second_variant.csv', 'r', encoding= 'utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def edit_data():
    filename = input('Введите имя файла для редактирования (data_first_variant.csv или data_second_variant.csv): ')
    with open(f'/Users/kit/Desktop/02_PYTHON/hw8/{filename}', 'r', encoding='utf-8') as f:
        data = f.readlines()

    print('Текущие данные:')
    for i, line in enumerate(data):
        print(f"{i + 1}. {line.strip()}")

    line_num = int(input('Введите номер строки для редактирования: ')) - 1
    if 0 <= line_num < len(data):
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data[line_num] = f"{name};{surname};{phone};{address}\n"

        with open(f'/Users/kit/Desktop/02_PYTHON/hw8/{filename}', 'w', encoding='utf-8') as f:
            f.writelines(data)
        print('Данные обновлены.')
    else:
        print('Неправильный номер строки.')

def delete_data():
    filename = input('Введите имя файла для удаления данных (data_first_variant.csv или data_second_variant.csv): ')
    with open(f'/Users/kit/Desktop/02_PYTHON/hw8/{filename}', 'r', encoding='utf-8') as f:
        data = f.readlines()

    print('Текущие данные:')
    for i, line in enumerate(data):
        print(f"{i + 1}. {line.strip()}")

    line_num = int(input('Введите номер строки для удаления: ')) - 1
    if 0 <= line_num < len(data):
        data.pop(line_num)
        with open(f'/Users/kit/Desktop/02_PYTHON/hw8/{filename}', 'w', encoding='utf-8') as f:
            f.writelines(data)
        print('Данные удалены.')
    else:
        print('Неправильный номер строки.')
    
# print_data()



