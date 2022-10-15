# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

content = ('сетевое программирование', 'сокет', 'декоратор')
with open('file.txt', 'w') as file:
    file.writelines('\n'.join(content))

print(f'Кодировка по умолчанию {file.encoding}')

with open('file.txt', encoding='utf-8') as file:
    try:
        for line in file:
            print(line)
    except UnicodeDecodeError:
        print('Невозможно прочесть данные в указанной кодировке' )