# задайте последовательность чисел. Напишите программу, которая выведет сисок
# неповторяющихся элементов исходной последовательности

first_list = [1, 3, 4, 6, 6, 7, 2, 8, 9, 3, 5, 5]
new_list = list(set(first_list))
print(new_list)