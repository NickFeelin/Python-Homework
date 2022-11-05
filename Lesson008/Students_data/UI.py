def get_data():
    data = []
    last_name = input('Введите фамилию: ')
    data.append(last_name)
    first_name = input('Введите имя: ')
    data.append(first_name)
    father_name = input('Введите отчество: ')
    data.append(father_name)
    age = input('Введите возраст: ')
    data.append(age)
    year_of_studying = input('Введите курс студента: ')
    data.append(year_of_studying)
    group_number = input('Введите номер группы студента: ')
    data.append(group_number)
    title = input('Пометки: ')
    data.append(title)
    return data