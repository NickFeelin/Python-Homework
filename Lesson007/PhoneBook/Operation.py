from UI import get_data as gd

info = gd()
def create_txt():
    file = '/Users/NickFilin/Desktop/Programming/GB/Python/Python Homework/Lesson007/PhoneBook/PhoneBook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n\n')
        
def create_txt_line():
    file = '/Users/NickFilin/Desktop/Programming/GB/Python/Python Homework/Lesson007/PhoneBook/PhoneLine.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]}   {info[1]}   {info[2]}   {info[3]}\n')
    
# /Users/NickFilin/Desktop/Programming/GB/Python/Python Homework/Lesson007/PhoneBook/Operation.py