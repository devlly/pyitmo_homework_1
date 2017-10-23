from collections import OrderedDict, namedtuple
import os.path as Path
import sys
import datetime

from organazer_code import storage

get_connection = lambda : storage.connect('tasks.sqlite')


Action = namedtuple('Action', ['func', 'name'])
actions = OrderedDict()

def menu_action(cmd, name):
    def decorator(func):
        actions[cmd] = Action(func=func, name=name)
        return func
    return decorator



@menu_action('1', 'Добавить задачу')
def action_add():
    '''добавляем задачу'''
    tasks_name = input('write task name:\n')
    tasks_content = input('write task content\n')
    tasks_date = input('write date to start do\n')
    tasks_time = input('write time to start if exist\n')

    with get_connection() as conn:
        storage.add_task('''
        conn,
        tasks_name,
        tasks_content,
        tasks_date,
        tasks_time
        ''')
    print('task \n{}\n{} was added for \n{} \n{}'.format(tasks_name, tasks_content, tasks_date, tasks_time))


@menu_action('2', 'Показать задачи на выбранный день')
def action_show_tasks_by_day():
    tasks_date = input('Введите дату')
    with get_connection() as conn:
        rows = storage.find_task_by_day(conn, tasks_date)

    template = '{row[onetime_tasks_time]} - {row[onetime_tasks_name]} - {row[onetime_tasks_content]} - {row[onetime_tasks_status]}'

    for row in rows:
            print(template.format(row=row))


@menu_action('3', 'Показать актуальные задачи')
def action_show_acutal_tasks():
        rows = storage.show_acutal_tasks()
        template = '{row[onetime_tasks_date]} - {row[onetime_tasks_time]} - {row[onetime_tasks_name]} - {row[onetime_tasks_content]} - {row[onetime_tasks_status]}'
        for row in rows:
            print(template.format(row=row))


@menu_action('4', 'Найти задачу по имени')
def action_find_task():
    tasks_name = input('Введите имя задачи')
    with get_connection() as conn:
        rows = storage.find_task_by_name(conn, tasks_name)
        template = '{row[onetime_tasks_date]} - {row[onetime_tasks_time]} - {row[onetime_tasks_name]} - {row[onetime_tasks_content]} - {row[onetime_tasks_status]} '

        for row in rows:
            print(template.format(row=row))


@menu_action('5', 'Изменить задачу')
def action_change():
    '''функции изменений параметров задачи'''
    tasks_name = input('Введите имя задачи, которую хотите изменить')
    pk = storage.find_task_by_name(conn, tasks_name)
    y = input('Нажмите y, если задача найдена правильно')
    if y:
        tasks_name = input('Введите новое имя задачи\n')
        tasks_content = input('Введите новое содержание задачи\n')
        tasks_date = input('Введите новую дату задачи\n')
        tasks_time = input('Введите новое время начала задачи\n')
        storage.change_task()
        print('Задача изменена')
    else:
        return

@menu_action('6', 'Изменить статус задачи')
def action_change():
    '''функции изменения статуса задачи'''
    tasks_name = input('Введите имя задачи, которую хотите изменить')
    pk = storage.find_task_by_name(conn, tasks_name)
    y = input('Нажмите y, если задача найдена правильно')
    if y:
        tasks_status = input('Введите новый статус')
        storage.change_status()
        print('Статус задачи изменен')


@menu_action('7', 'Показать меню')
def action_show_menu():
    menu = []

    for cmd, action_name in actions.items():
        menu.append('{}. {}'.format(cmd, action_name))

    print('\n'.join(menu))


@menu_action('8', 'Выйти')
def action_exit():
    sys.exit(0)


def main():

    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)


    action_show_menu()

    while True:
        cmd = input('\nprint command: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда')


@menu_action('7', 'Показать меню')
def action_show_menu():
    menu = []
'''
    for cmd, action_name in actions.items():
        menu.append('{}. {}'.format(cmd, action_name))

    print('\n'.join(menu))'''
