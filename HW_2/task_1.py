import os
import re
import csv


def get_data(files):
    main_data = {
        'Изготовитель системы': [],
        'Название ОС': [],
        'Код продукта': [],
        'Тип системы': [],
    }  # подумал, что словарем будет удобней
    for file in files:
        with open(file, encoding='windows-1251') as content:
            for line in content:
                # к черту регулярку
                list_line = line.split(':')  # делим строку по двоеточию
                key = list_line[0]  # первый элемент
                if key in main_data:  # если первый элемент есть в словаре как ключ, то это нужная строка
                    value = ' '.join(word for word in list_line[1].split() if word)  # делим пробелами и собираем
                    main_data[key].append(value)

    return main_data


def write_to_csv(csv_file, files):
    data = get_data(files)
    with open(csv_file, 'w', encoding='utf-8') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(data.keys())
        for line in zip(*data.values()):
            csv_writer.writerow(line)


if __name__ == '__main__':
    folder = 'data'
    txt_files = (f'{folder}\\{file}' for file in os.listdir(folder) if file.endswith(".txt"))  # список всех .txt файлов
    csv_file = 'report.csv'
    write_to_csv(f'{folder}\\{csv_file}', txt_files)
