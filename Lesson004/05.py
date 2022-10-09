# Даны два файла, в каждом из которыз находится запись многочлена.
# задача - сформировать файл, содержащий сумму многочленов

path_one = '/Users/NickFilin/Desktop/Programming/GB/Python/Python Homework/Lesson004/1.txt'
data_one = open(path_one, 'r')
for line_one in data_one:
    print(line_one)
data_one.close()

path_two = '/Users/NickFilin/Desktop/Programming/GB/Python/Python Homework/Lesson004/2.txt'
data_two = open(path_two, 'r')
for line_two in data_two:
    print(line_two)
data_two.close()

data = open('/Users/NickFilin/Desktop/Programming/GB/Python/Python Homework/Lesson004/3.txt', 'w')
data.write(f'{line_one} + {line_two}')
data.close()