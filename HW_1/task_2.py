# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

for b_string in b'class', b'function', b'method':
    print(b_string, type(b_string), len(b_string), sep=': ')
