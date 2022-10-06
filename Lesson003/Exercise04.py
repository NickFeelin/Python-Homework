# Напишите программу, которая будет преобразовывать десятичное число в двоичное

# def is_int(number):
#     return number.isdigit()

# def convert(number):
#     result = ''
#     term = int(number/2)
#     if term > 0:
#         result = convert(term) + str(number - term * 2)
#     else:
#         result = str(number)
#     return result

# number = None

# while not is_int(str(number)):
#     number = input('Введите число: ')
    
# number = int(number)

# print(number, '->', convert(number))

number = int(input('Введите целое число: '))
print(bin(number))