# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))
numb_list = list([randint(0, 100) for i in range(k+1)])
print(numb_list)

def multi_numbers(k, numb_list):
    str1 = ['x^']*(k-1) + ['x']
    multi_num = [[a, b, c] for a, b, c in itertools.zip_longest(numb_list, str1, range(k, 1, -1), fillvalue = '')]
    print(multi_num)
    for x in multi_num:
        x.append(' + ')
    multi_num = list(itertools.chain(*multi_num))
    print(multi_num)
    multi_num[-1] = ' = 0'
    print(multi_num)
    return "".join(map(str, multi_num)).replace(' 1x', ' x')

s = multi_numbers(k, numb_list)
print(s)

with open('multi_number.txt', 'w') as data:
    data.write(s)