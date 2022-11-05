import time
import unittest

from HW_5.client import create_presence
from HW_5.common.variables import RESPONSE

"""Unit-тесты клиента"""


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

    def test_create_presence(self):
        """Тест функции генерации запроса о присутствии клиента"""
        self.assertEqual(create_presence(self.acc_name), self.ask)


if __name__ == '__main__':
    unittest.main()
