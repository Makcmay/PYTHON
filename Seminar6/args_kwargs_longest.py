# def multiply(x, y):
#     print(x * y)


# multiply(5, 4)


# def multiply(*nums): #  args kwargs  когда не знаем точное количество данных
#     z = 1
#     for num in nums:
#         z *= num
#     print(z)


# multiply(4, 5)
# multiply(10, 9)
# multiply(2, 3, 4)
# multiply(3, 5, 10, 6, 10)


# def print_values(**kwargs):
#     for key, value in kwargs.items():
#         print("Значение для {} является {}".format(key, value))


# print_values(
#     name_1="Alex",
#     name_2="Gray",
#     name_3="Harper",
#     name_4="Phoenix",
#     name_5="Remy",
# #     name_6="Val"
# )




# def func(required_arg, *args, **kwargs):
#     print('r_a: ', required_arg)

#     if args:
#         print('args: ', args)

#     if kwargs:
#         print('kwargs: ', kwargs)

# # func()

# func("required argument")

# func("required argument", 1, 2, '3')

# func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")



from itertools import zip_longest
#
# out_dict = {}
# with open('users_hobby.txt', 'w', encoding='utf-8') as f:
#     with open('users.txt', encoding='utf-8') as users:
#         with open('hobby.txt', encoding='utf-8') as hobby:
#             for line_user, line_user_hobby in zip_longest(users, hobby):
#                 f.writelines(f'{line_user.strip()}: {line_user_hobby}\n')




import json

out_dict = {}
with open('users.txt', encoding='utf-8') as users:
    with open('hobby.txt', encoding='utf-8') as hobby:
        for line_user, line_user_hobby in zip_longest(users, hobby):
            out_dict[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby



with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f, ensure_ascii=False)
print(out_dict)