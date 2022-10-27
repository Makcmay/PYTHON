# 35. Есть N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 == A[i-1]. Найдите это число.
# 	my_str = ‘1 2 3 5 6’ => 4

my_str = list(map(int, '1 2 3 5 6'.split()))
print(my_str)
# num = [my_str[x]+1 for x in range(len(my_str) -1) if my_str[x+1] - my_str[x] > 1]
print([my_str[x]+1 for x in range(len(my_str) -1) if my_str[x+1] - my_str[x] > 1])

# 36. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]

# lst1 = [1, 5, 2, 3, 4, 6, 1, 7]
# new_lst = [lst1[0]]
# for i in lst1:
#     if i > new_lst[-1]:
#         new_lst.append(i)
# print(new_lst)


# x_list = [1, 5, 2, 3, 4, 6, 1, 7]
# num = [x_list[0]]
# [num.append(x_list[x]) for x in x_list if x_list[x] > num[-1]]
# print(num)
# 37. Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = 'Напиабвшите программу, удалабвяющую из текста вабвсе слова, содержащие "абв"'

f_str = ' '.join(filter(lambda i: 'абв' not in i, my_str.split(' ')))
print(f_str)
print(my_str.split(' '))