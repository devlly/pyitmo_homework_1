import os.path as Path
import sys
import datetime

from organazer_code import storage

get_connection = lambda : storage.connect('onetime_tasks.sqlite')


def action_add():
    '''добавляем задачу'''
    task_name = input('write task name:')
    task_content = input('write task content')
    task_date = input('write date to start do')
    task_time = input('write time to start if exist')

    with get_connection() as conn:
        storage.add_onetime_tasks('''
        conn,
        task_name,
        task_content,
        task_date,
        task_time
        ''')
    print('task {} was added for {} {}'.format(task_name, task_date, task_time))


def check_task_by_name():
    '''проверяем, что есть задача с заданным именем для функции изменения'''
    with get_connection() as conn:
        try:
            name = input('print old task name')
            task = storage.find_task_by_name(conn, name)
        except ValueError:
            print('it is no task with this name. try one more time or add new task')
            show_change_menu()


def action_change():
    '''функции изменений параметров задачи'''


    def change_onetime_task_name():
        check_task_by_name()
        with get_connection() as conn:
            newname = input('print new task name')
            for row in task:
                onetime_tasks_name = storage.change_onetime_task_name(conn, newname)
                if task:print('task name was changed. new name is {}'.format(newname))


    def change_onetime_task_content():
        check_task_by_name()
        with get_connection() as conn:
            new = input('print new task content')
            for row in task:
                onetime_tasks_content = storage.change_onetime_task_content(conn, new)
                if task:print('task content was changed. new content is {}'.format(new))


    def change_onetime_task_day():
        check_task_by_name()
        with get_connection() as conn:
            new = input('print new task date')
            for row in task:
                onetime_tasks_day = storage.change_onetime_task_day(conn, new)
                if task:print('task date was changed. new date is {}'.format(new))


    def change_onetime_task_time():
        check_task_by_name()
        with get_connection() as conn:
            new = input('print new task time')
            for row in task:
                onetime_tasks_time = storage.change_onetime_task_time(conn, new)
                if task:print('task start time was changed. new time is {}'.format(new))


    def change_onetime_task_status():
        check_task_by_name()
        with get_connection() as conn:
            new = input('print new task status')
            for row in task:
                onetime_tasks_status = storage.change_onetime_task_status(conn, new)
                if task:print('task status was changed. new status is {}'.format(new))


    def show_change_menu():
        '''показать меню по изменению параметров'''
        print("""
        print 'n' to change task name
        print 'c' to change task content
        print 'd' to change day
        print 't' to change time
        print 'st' to change task status
        print 'm' to back to main menu
        print 'chm' to see change-task menu
        print '0' to finish work with organazer
        """)


    action_change = {
    'n': change_onetime_task_name,
    'c': change_onetime_task_content,
    'd': change_onetime_task_day,
    't': change_onetime_task_time,
    'st': change_onetime_task_status,
    'm': action_show_menu,
    'chm': show_change_menu,
    '0': action_exit
    }

        action_show_change_menu()
        while True:
            cmd = input('\nprint command: ')
            action_change = actions_change.get(cmd)

            if action_change:
                action_change()
            else:
                print('unknown command. try one more time')


def action_show_tasks_by_day():
    date = input('print a date')
    with get_connection() as conn:
        rows = storage.find_task_by_day(conn, date)

    template = '{row[onetime_tasks_time]} - {row[onetime_tasks_name]} - {row[onetime_tasks_content]} - {row[onetime_tasks_status]} '

    for row in rows:
            print(template.format(row=row))


def action_find_task():
    with get_connection() as conn:
        rows = storage.all_tasks(conn)
    template = '{row[onetime_tasks_day]} - {row[onetime_tasks_time]} - {row[onetime_tasks_name]} - {row[onetime_tasks_content]} - {row[onetime_tasks_status]} '

    for row in rows:
        print(template.format(row=row))


def action_show_menu():
    print("""
    print 'a' to add task
    print 'ch' to change task
    print 'sh' to show tasks
    print 'f' to find task
    print 'm' to see menu
    print '0' to finish work with organazer
    """)


def action_exit():
    sys.exit(0)


def main():

    creation_schema = Path.join(
        Path.dirname(__file__), 'scheme.sql'
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)


    actions = {
        'a': action_add,
        'ch': action_change,
        'sh': action_show_tasks,
        'f': action_find_task,
        'm': action_show_menu,
        '0': action_exit
    }

    action_show_menu()
    while True:
        cmd = input('\nprint command: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('unnown command. try one more time')
