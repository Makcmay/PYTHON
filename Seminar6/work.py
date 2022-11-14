# 42. Есть список чисел. Вывести – является ли последовательность строго убывающей, или строго возрастающей, или ни то, ни другое

# my_list = [1, 3, 3, 4, 5]
# countup = 0
# countdown = 0
# for i in range(len(my_list) - 1):
#     if my_list[i] < my_list[i + 1]:
#         countup += 1
#     elif my_list[i] > my_list[i + 1]:
#         countdown += 1
#     else:
#         print('NOT')
#         break
# if countup == len(my_list) - 1:
#     print('UP')
# elif countdown == len(my_list) - 1:
#     print('DOWN')

# def check_sorted(somelist):
#     if sorted(set(somelist)) == somelist: # sorted- отсортирует по возрастанию (set- уберет дубли
#         return 1
#     elif sorted(set(somelist), reverse = True) == somelist:
#         return -1
#     return 0
# s_dict = {
#     1: 'UP',
#     -1: 'DOWN',
#     0: 'NOT'
# }
# print(s_dict[check_sorted([1,2,4])])
# print(s_dict[check_sorted([3,2,3])])
# print(s_dict[check_sorted([3,2,1])])
# print(check_sorted([1,1,2,3]))

# 43. Дана последовательность чисел. Получить отсортированный по возрастанию список уникальных элементов заданной последовательности.
# 	Пример:
# my_list = [100, 1, 2, 3, 5, 1, 5, 3, 10] #=> [2, 10]

# def uniqList(my_list):

#     uniq = [i for i in sorted(my_list) if my_list.count(i) == 1]
#     print(uniq)
#     return uniq
# uniqList(my_list) 

# 44. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# 	Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# m_list = '1-2*3'
# array = list(m_list)
# print(array)

# print(eval(m_list)) # передает и считает eval
# **Добавьте возможность использования скобок, меняющих приоритет операций.
# 	Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;
string = '1+23*3-2*4'

def list_from_string(string:str):
    result = []
    temp = 0
    for i in range(0, len(string)):

        if not string[i].isalnum():
            result.append(string[temp:i])
            result.append(string[i])
            temp = i + 1

    result.append(string[temp:])
    print(result)

    return result

# list_from_string(string)

def simpl_math(operation:list):
    if operation[1] == '/':
        return [str(float(operation[0]) / float(operation[2]))]
    if operation[1] == '*':
        return [str(float(operation[0]) * float(operation[2]))]
    if operation[1] == '+':
        return [str(float(operation[0]) + float(operation[2]))]
    if operation[1] == '-':
        return [str(float(operation[0]) - float(operation[2]))]

def do_math(equation:list):

    while len(equation) != 1:

        for sign in '/*+-':
            if sign in equation:
                index = equation.index(sign)
                equation = equation[:index-1] + simpl_math(equation[index-1:index+2]) + equation[index+2:]

    return equation
print(do_math(list_from_string(string)))


# доп. Напишите функцию any_duplicates, которая принимает двумерный массив размера 3х3 (9 элементов). Двумерный массив заполнен числами от 1 до 9.
# Функция должна вернуть False, если в массиве все числа от 1 до 9 встречаются ровно один раз. В противном случае True.
# [[1, 3, 2], [9, 7, 8], [4, 5, 6]] ➞ False
# [[8, 9, 2], [5, 6, 1], [3, 7, 4]] ➞ False
# [[1, 1, 3], [6, 5, 4], [8, 7, 9]] ➞ True # 1 дублируется
# [[1, 2, 3], [3, 4, 5], [9, 8, 7]] ➞ True # 3 дублируется


# my_list = [[1, 3, 2], [9, 7, 8], [4, 5, 6]]

# matrix = [i for j in my_list for i in j] # распаковка матрицы
# print(matrix)
# print(sorted(matrix) != [1,2,3,4,5,6,7,8,9]) # решение

# def any_duplicates(matr):
#     perfect_array = [1,2,3,4,5,6,7,8,9]
#     array = []
#     for i in matr:
#         for j in i:
#             array.append(j)
#     sorted_array = sorted(array)
#     return sorted_array != perfect_array
# print(any_duplicates(my_list))
