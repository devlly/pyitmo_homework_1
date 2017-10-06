'''Задача №1.
Напишите функцию get_days_to_new_year, которая возвращает количество дней, оставшихся до нового года.
Датой наступления нового года считается 1 января.
Функция должна корректно работать при запуске в любом году, т. е. грядущий год должен вычисляться программно.
Для решения задачи понадобится стандартный модуль datetime
https://docs.python.org/3/library/datetime.html
Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
Имя файла: task_03_01.py
Имя функции: get_days_to_new_year
Возвращаемое значение: int'''

def get_days_to_new_year():
    import time
    from datetime import date
    today == date.fromtimestamp(time.time())
    new_year = date(today.year, 1, 1)
    if new_year < today:
        new_year = new_year.replace(year=today.year + 1)

    return int(time_to_new_year.days)

