# original = 235
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)


'''
Выяснить, является ли число кратным заданному, если нет, вывести остаток
'''
# num1 = int(input('Введите 1 число: '))
# num2 = int(input('Введите 2 число: '))
#
#
# if num1 % num2:
#     print('Не кратно, остаток', num1 % num2)
# else:
#     print('Кратно')
'''
Показать последнюю цифру 3-значного числа
'''
# digit = input("Введите число: ")
# print(int(digit[-1]))

'''
11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
Пример:
Для N = 5: 1, -3, 9, -27, 81
'''


# def sequence(num: int) -> list:
#     """
#     Программа для создания новой последовательности
#     :param num: Берем число от пользователя
#     :return: list - список чисел по формуле
#     """
#     my_list = []
#     for i in range(num):
#         my_list.append((-3) ** i)
#     return my_list
#
#
# print(sequence(5))

# def sequence(num: int) -> list:
#     '''
#     Программа для создания новой последовательности
#     :param num: Число элементов последовательности
#     :type num: int
#     :return: list - Список..
#     '''
#     # for i in range(num):
#     #     my_list.append((-3)**i)
#
#     return [((-3)**i) for i in range(num)]
#
# print(sequence(5))
#
# my_list = [i for i in range(1, 10, 2)]
# print(my_list)


"""
12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
Пример:
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""
from random import randint

def get_dict(n):
    my_dict = {}
    for i in range(1, n+1):
        my_dict[i] = 3 * i + 1
    return my_dict

n = randint(1, 25)

print(n)
print(get_dict(n))


from random import randint

def get_dict(n):
    return {i: 3 * i + 1 for i in range(1, n+1)}

n = randint(5, 20)

print(n)
print(get_dict(n))


'''
13. Напишите программу, в которой пользователь будет задавать две строки, 
а программа - определять количество вхождений одной строки в другой.
'''

s1 = input('Введите большую строку: ')
s2 = input('Введите искомую строку: ')

#rqwerqwe
#qwe
def str_count(s1, s2):
    count = 0
    k = 1
    for i in range(0, len(s1) - len(s2) + 1, k):
        if s2 in s1[i:i+len(s2)]: #[0 : 3]
            count += 1
            k = len(s2)
        else:
            k = 1
    return count
print(f"Найдено вхождений - {str_count(s1, s2)}")


# def str_count(s1, s2):
#     # s1 = s1.lower()
#     # s2 = s2.lower()
#     return s1.count(s2)
#
#
# print(f'Найдено вхождений: {str_count(s1, s2)}')
