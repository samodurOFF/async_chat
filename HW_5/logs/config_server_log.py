import sys
import os
from logging import Formatter, StreamHandler, ERROR, getLogger, handlers

sys.path.append('..')
from common.variables import ENCODING, LOGGING_LEVEL

# формировщик логов:
SERVER_FORMATTER = Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'chat.log')

# создаём потоки вывода логов
STREAM_HANDLER = StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(ERROR)
LOG_FILE = handlers.TimedRotatingFileHandler(PATH, encoding=ENCODING, interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)

# регистратор
LOGGER = getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    LOGGER.critical('Critical error')
    LOGGER.error('An error occurred')
    LOGGER.debug('Debugging')
    LOGGER.info('Message')
    LOGGER.warning('Warning')
