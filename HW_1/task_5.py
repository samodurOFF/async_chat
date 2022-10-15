# Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице.

from subprocess import PIPE, Popen

hosts = ('yandex.ru', 'youtube.com')
result = ''
for host in hosts:
    resp = Popen(['ping', host], stdout=PIPE)

    for line in resp.stdout:
        print(line.decode('cp866'))
