import time
import unittest
from socket import socket

from HW_4.client import create_presence
from HW_4.server import answer, init_socket
from HW_4.variables import RESPONSE, DEFAULT_PORT, DEFAULT_IP_ADDRESS

"""Unit-тесты сервера"""


class TestServer(unittest.TestCase):
    '''
    В сервере только 1 функция для тестирования
    '''
    acc_name = 'acc_name'

    ok_dict = {
        RESPONSE: 200
    }

    ask = {
        'action': 'presence',
        'time': int(time.time()),
        'user': {
            'account_name': acc_name
        }
    }

    def test_answer(self):
        """Тест корректности ответа"""

        self.assertEqual(
            answer(self.ask), self.ok_dict)

    def test_init_socket(self):
        """Тест инициализации сокета"""

        self.assertEqual(socket.getsockname(init_socket()), (DEFAULT_IP_ADDRESS, DEFAULT_PORT))

    def test_create_presence(self):
        """Тест функции генерации запроса о присутствии клиента"""
        self.assertEqual(create_presence(self.acc_name), self.ask)


if __name__ == '__main__':
    unittest.main()
