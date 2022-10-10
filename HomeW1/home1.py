# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет
print()
print('Напишите программу, которая принимает на вход цифру,' 
+'обозначающую день недели, и проверяет, является ли этот день выходным.')
print()
week_num = int(input('Введите номер дня недели :'))

if week_num > 0 and week_num <= 5:
    print(f'День неделя {week_num} является рабочим')

elif week_num > 5 and week_num <=7:
    print(f'День неделя {week_num} является выходным')

else:
    print(f'Число {week_num} не является номером дня недели')


# 7. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print()
print('Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')
predic = [True,False]
for x in predic:
    for y in predic:
        for z in predic:
            res = not (x or y or z) == (not x) and (not y) and (not z)
            print('X=', x,'Y=', y,'Z=', z, ':' '¬(X v Y v Z) = ¬X ⋀ ¬Y ⋀ ¬Z' '=', res)

# 8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

print()
print('Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и' 
+'выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).')

x = int(input("Введите X: ")) 
y = int(input("Введите Y: "))
print(f'координаты точки [{x}, {y}]')
 
if x != 0 and y != 0:
    if x > 0 and y > 0:
        print('Точка находится в 1 четверти')
    elif x < 0 and y > 0:
        print('Точка находится в 2 четверти')
    elif x < 0 and y < 0: 
        print('Точка находится в 3 четверти')
    elif x > 0 and y < 0: 
        print('Точка находится в 4 четверти')
else:
    print('Введены не верные дынные')  

# 9. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print()
quarter = int(input("Введите номер четверти (от 1 до 4): ")) 

if 0 < quarter < 5:
    if quarter == 1:
        print('Интервал координат точки [x, y] = x > 0 и y > 0')
    elif quarter == 2: 
        print('Интервал координат точки [x, y] = x < 0 и y > 0')            
    elif quarter == 3: 
        print('Интервал координат точки [x, y] = x < 0 и y < 0')
    elif quarter == 4: 
        print('Интервал координат точки [x, y] = x > 0 и y > 0')
else:
    print('Введены не верные дынные')         
# 10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
print()
print('Напишите программу, которая принимает на вход координаты двух точек и находит' 
+'расстояние между ними в 2D пространстве.')

print("Введите координаты точки А")
pointA = [int(input()), int(input())]
print("Введите координаты точки В")
pointB = [int(input()), int(input())]

lengthSegment = ((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2) ** (0.5)
print(f"Длина отрезка: {format(lengthSegment, '.2f')}")