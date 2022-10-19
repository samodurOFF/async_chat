from socket import *
import time, json
from variables import *


def create_presence(account_name):
    """
    Функция генерации запроса о присутствии клиента
    """

    out = {
        ACTION: PRESENCE,
        TIME: int(time.time()),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }

    return out


def connect_to_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
    account_name = input('Имя пользователя: ')
    presence_msg = create_presence(account_name)
    s.send(json.dumps(presence_msg, sort_keys=True, indent=4).encode(ENCODING))
    recp = json.loads(s.recv(MAX_PACKAGE_LENGTH))
    print('Сообщение от сервера: ', recp[RESPONSE])



if __name__ == '__main__':
    command = input('Начать взаимодействие с сервером? (y/n)?: ')
    if command == 'y':
        connect_to_server()
    else:
        print('Подключение отменено!')
