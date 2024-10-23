# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.

import argparse


def parser(choices_num, choices_text):
    parsers = argparse.ArgumentParser(description='Процессинг числа и строки с дополнительными опциями.')

    parsers.add_argument('number', type=int, help='Число для вывода')
    parsers.add_argument('text', type=int, help='Строка для вывода')

    parsers.add_argument('--verbose', action='store_true', help='Вывод дополнительной информации')
    parsers.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')

    args = parsers.parse_args()

    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text = "{args.text}", repeat = {args.repeat}')

    print(f'Число: {args.number}, Строка: {args.text * args.repeat}')


if __name__ == '__main__':
    parser()




