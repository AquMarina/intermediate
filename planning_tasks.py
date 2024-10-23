# Задача 3. Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta


def return_date(days_from):
    datetime_now = datetime.now()

    return_dates = datetime_now + timedelta(days=days_from)

    formatted_return_dates = return_dates.strftime('%Y-%m-%d')
    return formatted_return_dates


if __name__ == '__main__':
    days = 30
    print(f'Дата спустя {days} дней с сегодняшней даты: {return_date(days)}')



