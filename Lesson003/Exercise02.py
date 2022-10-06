# Напишите программу, которая найдет произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.

def input_int(number=""):
    while True:
        try:
            result = int(input(number))
        except ValueError:
            print('Введите корректное значение')
        else:
            return result
        
def input_array():
    count = input_int('Введите количество элементов списка: ')
    result = []
    for i in range(count):
        result.append(input_int(f'Введите число {i+1}: '))
    return result

def double_multiplication(number_list):
    size = len(number_list)
    short_size = size//2
    result = list()
    for i in range(short_size):
        result.append(number_list[i] * number_list[size - i - 1])
    if short_size * 2 != size:
        result.append(number_list[short_size]**2)
    return result

print(double_multiplication(input_array()))