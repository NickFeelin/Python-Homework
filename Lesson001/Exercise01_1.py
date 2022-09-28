# Напишите программу для проверки истинности утверждения
# для всех значений предикат

def inputNumpers(x):
    xyz = ['X', 'Y', 'Z']
    a = []
    for i in range(x):
        a.append(input(f'Введите значение {xyz[i]}: '))
    return a

def predicate(x):
    first = not (x[0] or x[1] or x[2])
    second = not x[0] and not x[1] and not x[2]
    result = first == second
    return result

finding = inputNumpers(3)

if predicate(finding) == True:
    print(f'Утверждение истинно')
else:
    print(f'Утверждение ложно')