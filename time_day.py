# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

from datetime import datetime


def current_datetime():
    datetime_now = datetime.now()

    formatted_date = datetime_now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = datetime_now.strftime('%A')
    week_number = datetime_now.isocalendar()[1]

    print(f'Текущие день и время: {formatted_date}')
    print(f'День недели: {day_of_week}')
    print(f'Номер недели: {week_number}')


if __name__ == '__main__':
    current_datetime()


