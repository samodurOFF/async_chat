import sys
from logging import getLogger

# определения модуля запуска
if 'client.py' in sys.argv[0]:
    logger = getLogger('client')
else:
    logger = getLogger('server')


def log(func_to_log):
    def log_saver(*args, **kwargs):
        modul_name = func_to_log.__code__.co_filename.split('\\')[-1]
        logger.debug(
            f'Была вызвана функция {func_to_log.__name__} c параметрами {args} , {kwargs}. Вызов из модуля {modul_name}')
        ret = func_to_log(*args, **kwargs)
        return ret

    return log_saver

