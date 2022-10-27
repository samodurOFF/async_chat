import time
import unittest
from socket import socket

from HW_5.common.variables import RESPONSE, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from HW_5.server import answer, init_socket

"""Unit-тесты сервера"""


class TestServer(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
