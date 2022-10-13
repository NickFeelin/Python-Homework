# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def encoding(module):
    code_module = ""
    count = 0
    iterations = 1
    while count < len(module):
        try:
            if module[count] == module[count+1]:
                iterations += 1
            elif iterations == 1:
                code_module += module[count]
            elif iterations > 1:
                code_module += str(iterations) + module[count]
                iterations = 1
        except IndexError:
            if iterations == 1:
                code_module += module[count]
            elif iterations > 1:
                code_module += str(iterations) + module[count]
        count += 1
    return code_module
def decoding(cipher):
    decoded_module = ""
    count = 0
    iterations = 0
    while count < len(cipher):
        if str(cipher[count]).isdigit():
            iterations = int(cipher[count])
        elif iterations > 0:
            for x in range(iterations):
                decoded_module += cipher[count]
                iterations = 0
        elif iterations == 0:
            decoded_module += cipher[count]
        count +=1
    return decoded_module
module = input("Введите название файла: ")
numbers_in_module = 0
for num in module:
    if num.isdigit():
        numbers_in_module += 1
if numbers_in_module > 0:
    print(f"Decoding: {decoding(module)}")
else:
    print(f"Encoding: {encoding(module)}")