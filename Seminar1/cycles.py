# i = 0
# while i < 10:
#     i += 1  # i = i +1
#     if i == 3:
#         continue #прерывает все ниже и переходит обратно в цикл
#     print(i)
#     if i == 6:
#         break





# Цикл for применяется для обхода последовательности
# my_list = [0, 1, 2, 'zsfg', 3, 4, 5]
# for element in my_list:
#     print(element)



# my_str = 'qwerty'
# for el in my_str:
#     print(el)

# a = range(3, 10, 3)
# print(type(a))

# for i in range(5, 10, 2): # (start, stop, step)
#      print(i)



# numbers = list(range(2, 10, 5))
# print(numbers)



# Оборачитваем в enumerate
my_str = 'qwerty'
my_list = []
for i, letter in enumerate(my_str, start=1):
    print(i, letter)
    my_list.append(str(i) + '.' + letter)
print(my_list)













































# for i in range(5):
#     print(i)
#     if i == 3:
#         break
# else:
#     print('End') 


# for i in range(5):
#     print(i)
#     if i == 3:
#         break
# print('End') 