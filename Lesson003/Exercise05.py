# Задайте число. Создайте список чисел Фибоначчи, в том числе для отрицательных индексов

from operator import ne, neg


number = int(input('Введите число: '))
negative_number = [1, -1]
fibon_number = [1, 1]
for i in range(2, number):
    new_number = fibon_number[i - 1] + fibon_number[i - 2]
    fibon_number.append(new_number)
for j, element in enumerate(fibon_number, 2):
    if j % 2 != 0:
        new_number = element * -1
        negative_number.append(new_number)
    else:
        negative_number.append(element)
negative_number.reverse()
negative_number.append(0)
print(negative_number + fibon_number)