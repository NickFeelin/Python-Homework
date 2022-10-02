# Задайте список из n чисел последовательности 
# "(1 + 1/n) ** n" и выведите на экран их сумму.

def input_filtation(num):
    while True:
        try:
            res = int(input(num))
        except ValueError:
            print('Введите корректное значение: ')
        else:
            return res

def list_create(n):
    result = []
    for i in range(1, n + 1):
        result.append(round((1 + 1 / i) ** i))
    return result

n = input_filtation("Введите целое число: ")
num_list = list_create(n)

print(f'Для n = {n}: {num_list} -> {sum(num_list)}')