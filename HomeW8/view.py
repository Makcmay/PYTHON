
# def get_phone():
#     return input('Введите номер телефона : ')

# def get_user():
#     return input('Введите ваш Login : ')

# def get_name():
#     return input('Введите Имя : ')

# def get_surname():
#     return input('Введите Фамилию : ')

# def get_second_name():
#     return input('Введите Отчество : ')

def correct_name(text):
    name = input(f'{text} ')
    while True:
        if name.isalpha():
            return name.capitalize()
        print('не корректный ввод')
        name = input(f'{text} ')


def correct_number():
    number = input('Введите номер телефона +7 код номер без пробелов -> ')
    while True:
        if number[0] == '+' and number[1:].isdigit(): #and len(number) == 12:
            return number
        print('не корректный ввод')
        number = input('Введите номер телефона +7 код номер без пробелов -> ')

def get_choice():
    flag = False
    while not flag:
        try:
            number = int(input('Выберите действие:\n'
                     'Ввод данных - 1\n'
                     'Вывод данных - 2\n'
                     'Изменение данных - 3\n'
                     'Поиск по Фамилии - 4\n'
                     'Выход из программы  5: '))
            if 0 < number < 6:
                flag = True
        except ValueError:
            print("Ошибка, попробуйте еще раз!")
    return number