# Задайте список из нескольких чисел. Напишите программу,
# которая найдет сумму элементов списка, стоящих на нечетной позиции

# my_list = [2, 3, 5, 9, 3, 4, 34]
# num_sum = 0
# for item in range(1, len(my_list), 2):
#     num_sum += my_list[item]
# print(num_sum)

import random
num = int(input('Введите число: '))
num_list = []
for i in range(num):
    num_list.append(random.randint(1, 10))
print(num_list)
print(sum(num_list[::2]))