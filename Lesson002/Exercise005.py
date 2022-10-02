# Реализуйте алгоритм перемешивания списка.

from random import random, randrange

def mix_list(old_list):
    new_list = old_list
    list_lenght = len(new_list)
    for i in range(list_lenght):
        index = random.randrange(list_lenght - 1)
        new_list[i], new_list[index] = new_list[index], new_list[i]
    return new_list

old_list = [1, 7, 9, 5, 8, 4, 3, 2]
print(old_list)
print(mix_list(old_list))
