# Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N.

# num = input('Введите число: ')
# while not num.isdigit():
#     num = input('Введите корректное число: ')
# num = int(num)
# res = list()
# element = 1
# for i in range(num):
#     element = (i + 1) * element
#     res.append(element)
# print(res)

my_list = [2, 3, 4, 5, 6]
print_list = []
for i in range((len(my_list) + 1) // 2):
    print_list.append(my_list[i] * my_list[len(my_list) - 1 - i])
print(print_list)