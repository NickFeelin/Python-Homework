# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N

num = int(input('Введите число N: '))
numbers = []
for i in range(2, num):
    if num % i == 0:
        count = 1
        for j in range(2, (i//2 + 1)):
            if (i % j == 0):
                count = 0
                break
        if (count == 1):
            numbers.append(i)
print(numbers)
