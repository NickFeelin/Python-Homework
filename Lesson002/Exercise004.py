# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Введите число: '))
element_list = list(range(-num, num+1))
path = 'file.txt'
data = open(path, 'r')
element_sum = 1
for position in data:
    element_sum *= element_list[int(position)]
data.close()
print(element_list)
print(element_sum)
