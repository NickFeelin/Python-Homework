from UI import get_data as gd

info = gd()
def create_txt():
    file = '/Users/NickFilin/Desktop/Programming/GB/Python/Python Homework/Lesson008/Students_data/Students_list.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nОтчество: {info[2]}\nВозраст: {info[3]} лет\nКурс: {info[4]}\nГруппа: {info[5]}\nПометки: {info[6]}\n\n')