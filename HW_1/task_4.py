# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).


data = ('разработка', 'администрирование', 'protocol', 'standard')

for word in data:
    to_bytes = word.encode('utf-8')
    print(to_bytes, type(to_bytes), len(to_bytes), sep=': ')
    to_str = to_bytes.decode('utf-8')
    print(to_str, type(to_str), len(to_str), sep=': ')
