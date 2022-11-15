'''
Так делать плохо
'''
# def say_hello():
#    print(name)
#
# name = 'Иван'
# say_hello()


'''
Что будет?
'''
# def say_hello():
#     print(name)
#
#
# say_hello()


'''
Что будет выведено?
'''

# def say_hello():
#     name = 'Петр'
#     print(name)
#
#
# name = 'Иван'
# say_hello()

'''
А тут?
'''

# def say_hello_wrapper():
#     name = 'Петр'
#
#     def say_hello():
#         print(name)
#
#     say_hello()
#
#
# name = 'Иван'
# say_hello_wrapper()

'''
Тут?
Можно ли изменить значение глобальной переменной из локальной области?
'''

# def say_hello():
#     name = 'Петр'
#     print(name)
#
#
# name = 'Иван'
# say_hello()
# print(name)

'''
Из локальной области видите глобальную, а из глобальной области посмотреть в локальную невозможно
'''


# def say_hello():
#     name = 'Петр'
#     print(name)
#
#
# say_hello()
# print(name)

'''
Глобальные переменные
'''

def say_hello():
    global name
    name = 'Петр'
    print(name)


name = 'Иван'
print(name)  # Иван
say_hello()  # Петр
print(name)  # Петр
name = 'Иван'
print(name)  # Иван
