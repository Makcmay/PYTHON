'''3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.'''

with open('HomeW5\decoded.txt', 'r') as data:
    my_text = data.read() + ' ' # добавил пробел в конц строки для чтения последненго символа

def encode(sstr):
    str_code = ''
    prev_char = ''
    count = 1
    for char in sstr:             # прошлись по всем символам  
        if char != prev_char:     # сравниваем символ с предыдущим, чтобы отсекать новый символ
            if prev_char:
                str_code += str(count) + prev_char #записываем строку, счетчик и предыдуши символ
            count = 1        # сброс
            prev_char = char # сохраняем новый символ
        else:
            count += 1 # считаем одинаковые символы
    return str_code

            
str_code = encode(my_text)
print(str_code)

with open('HomeW5\encoded.txt', 'w', encoding='utf8') as data: # замисали
    data.write(str_code)

with open('HomeW5\encoded.txt', 'r') as data:   # считали
    my_text2 = data.read()

def decoding(sstr:str):   # восттанавливаем строку
    count = ''
    str_decode = ''
    for char in sstr:
        if char.isdigit():  # если элемент является числом, счетчик приравнивается к числу
            count += char 
        else:
            str_decode += char * int(count) # когда элемент буква, она умножаеся на счетчик (для этого строку заворачиваем в инт) -  получаем обратное действие и кладем в строку str_decode
            count = ''                      # очищаем счетчик
    return str_decode

str_decode = decoding(my_text2)
print(str_decode)