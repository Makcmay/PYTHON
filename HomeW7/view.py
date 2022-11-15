def view_data(data, titel):
    print(f'{titel} = {data}')

def get_float_value():
    return float(input('value = '))

def get_complex_value():
    return complex(input('value = '))

def get_action():
    return str(input('Введите действие +-*/  = '))

def get_number_info():
    return int(input('Введите тип данных, комплексные = 1, рациональные = 2  :'))

mode = {'+': 'сумма', '-': 'разность', '*': 'произведение', '/': 'деление'}
info = {1: 'комплексные', 2: 'рациональные'}