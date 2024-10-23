# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

info_debug_handler = logging.FileHandler('info_debug.log')
info_debug_handler.setLevel(logging.DEBUG)
info_debug_handler.setFormatter(formatter)
logger.addHandler(info_debug_handler)

errors_warnings_handler = logging.FileHandler('errors_warnings.log')
errors_warnings_handler.setLevel(logging.WARNING)
errors_warnings_handler.setFormatter(formatter)
logger.addHandler(errors_warnings_handler)

logger.debug('Сообщение уровня DEBUG.')
logger.info('Сообщение уровня INFO.')
logger.warning('Сообщение уровня WARNING.')
logger.error('Сообщение уровня ERROR.')
logger.critical('Сообщение уровня CRITICAL.')


