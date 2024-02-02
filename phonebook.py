import os

def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    with open(filename, 'r+t', encoding='utf-8') as wrtbl:
        lines_count = len(wrtbl.readlines()) # подсчет количества записей
        wrtbl.write(f'{lines_count + 1};{name};{phone}\n')
    
def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, 'r', encoding='utf-8') as data:
        result = data.read()
    return result

def search_user(data: str, filename: str) -> str:
    """
    Поиск записи по критерию content.
    """
    with open(filename, 'r', encoding='utf-8') as content:
        text = content.readlines()
        res = ([item for item in text if data.lower() in item.lower()])
    return (''.join(res)).replace(';', ' ') if res else 'Совпадений не найдено'

def check_directory(filename: str): # функция для создания нового файла, если в DATA_SOURCE несуществующий файл
    if filename not in os.listdir():
        with open(filename, 'w', encoding='utf-8') as data:
            data.write('')

def copy_string(filename: str, data: str):
    """
    Копирование строки
    """
    with open('copy.txt', 'w', encoding='utf-8') as copy:
            copy.writelines(search_user(number_string, DATA_SOURCE))
       
INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - копирование данных
"""

DATA_SOURCE = 'phone.txt'

check_directory(DATA_SOURCE)

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATA_SOURCE))
        exit()
    elif mode == 2:
        user =input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        add_new_user(name = user, phone = phone, filename = DATA_SOURCE)
    elif mode == 3:
        search = input("Введите строку для поиска: ")
        print(search_user(search, DATA_SOURCE))
        exit()
    elif mode == 4:
        read_all(DATA_SOURCE)
        number_string = input('Введите номер строки для копирования: ')
        copy_string('copy.txt', search_user(number_string, DATA_SOURCE))
        exit()