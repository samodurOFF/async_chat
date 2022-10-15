# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

data = ('attribute', 'класс', 'функция', 'type')

for word in data:
    try:
        result = bytes(word, encoding='ASCII')
        print(result)
    except UnicodeEncodeError:
        print(f'Вероятно, слово {word} невозможно записать в байтовом типе')
