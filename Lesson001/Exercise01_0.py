# Напишите программу, которая принимает на вход цифру, обозначающую
# день недели, и проверяет, является ли этот день выходным

d = int(input('Введите номер дня недели: '))

if 1 <= d <= 5:
    print('нет')
elif d == 6 or d == 7:
    print('да')
else:
    print('Такого дня недели не существует')