import sqlite3
import datetime

'''SQL_SELECT_ALL_REGTASKS = """
    SELECT id, regtasks_name, regtask_content, regtask_status, regtasks_weekday, regtasks_time
    FROM regtasks
""" '''

SQL_SELECT_ALL_ONETIME_TASKS = """
    SELECT id,
    onetime_tasks_name,
    onetime_tasks_content,
    onetime_tasks_day,
    onetime_tasks_time,
    onetime_tasks_status,
    FROM onetime_tasks
"""

'''SQL_SELECT_ALL_CALENDAR = """
    SELECT id, cal_plan_date, cal_tasks_body

""" '''

SQL_SELECT_ALL_BY_DAY = SQL_SELECT_ALL_ONETIME_TASKS + " WHERE onetime_tasks_day=?"
SQL_SELECT_BY_NAME = SQL_SELECT_ALL_ONETIME_TASKS + " WHERE onetime_tasks_name=?"

'''SQL_INSERT_REGTASKS = """
    INSERT INTO regtasks (
    regtasks_name,
    regtasks_content,
    regtasks_weekday,
    regtime_time
    )
     VALUES (?, ?, ?, ?)
""" '''

SQL_INSERT_ONETIME_TASKS = """
    INSERT INTO onetime_tasks (
    onetime_tasks_name,
    onetime_tasks_content,
    onetime_tasks_day,
    onetime_tasks_time
    )
    VALUES (?, ?, ?, ?)
"""


SQL_UPDATE_ONETIME_TASK_CONTENT = """
    UPDATE onetime_tasks SET onetime_tasks_content=? WHERE id=?
"""

SQL_UPDATE_ONETIME_TASK_NAME = """
    UPDATE onetime_tasks SET onetime_tasks_name=? WHERE id=?
"""

SQL_UPDATE_ONETIME_TASK_DAY = """
    UPDATE onetime_tasks SET onetime_tasks_day=? WHERE id=?
"""

SQL_UPDATE_ONETIME_TASK_TIME = """
    UPDATE onetime_tasks SET onetime_tasks_time=? WHERE id=?
"""

SQL_UPDATE_ONETIME_TASK_STATUS = """
    UPDATE onetime_tasks SET onetime_tasks_status=? WHERE id=?
"""

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())


def all_tasks(conn):
    '''Выводит все задачи за все время'''
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL_ONETIME_TASKS)
        return sorted(cursor.fetchall(), key=onetime_tasks_status)


def find_task_by_day(conn, onetime_tasks_day):
    ''''выводит список задач по дню'''
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL_BY_DAY, (onetime_tasks_day,))
        return cursor.fetchall()


def task_list_for_today(conn):
    ''' выводит список задач на сегодня'''
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL_BY_DAY, (CURRENT_DATE,))
        return cursor.fetchall()


def find_task_by_name(conn, onetime_tasks_name):
    '''находит задачу по имени'''
    onetime_tasks_name = onetime_tasks_name.lower.rsplit('. ', 1).pop()
    with conn:
        cursor = conn.execute(SQL_SELECT_BY_NAME,
                            (onetime_tasks_name,))
        return cursor.fetchone()


def change_onetime_task_name(conn, onetime_tasks_name):
    '''изменяет имя задачи'''
    with conn:row = storage.find_task_by_name(conn, name)
        cursor = conn.execute(SQL_UPDATE_ONETIME_TASK_NAME, (onetime_tasks_name,))
        return cursor


def change_onetime_task_content(conn, onetime_tasks_content):
    '''изменяет содержание задачи'''
    with conn:
        cursor = conn.execute('''
        SQL_UPDATE_ONETIME_TASK_CONTENT,
        (onetime_tasks_content,)
        ''')
        return cursor

def change_onetime_task_date(conn, onetime_tasks_date):
    '''изменяет день задачи'''
    with conn:
        cursor = conn.execute('''
        SQL_UPDATE_ONETIME_TASK_DAY,
        (onetime_tasks_day,)
        ''')
        return cursor

def change_onetime_task_time(conn, onetime_tasks_time):
    '''изменяет время начала задачи'''
    with conn:
        cursor = conn.execute('''
        SQL_UPDATE_ONETIME_TASK_TIME,
        (onetime_tasks_time,)
        ''')
        return cursor

def change_onetime_task_status(conn, onetime_tasks_status):
    '''изменяет статус задачи'''
    with conn:
        cursor = conn.execute('''
        SQL_UPDATE_ONETIME_TASK_STATUS,
        (onetime_tasks_status,)
        ''')
        return cursor


def add_onetime_tasks(conn, onetime_tasks_name, onetime_tasks_content, onetime_tasks_weekday, onetime_tasks_time):
    '''добавляет задачу'''
    onetime_tasks_name = onetime_tasks_name.lower.rsplit('. ', 1).pop()
    with conn:
        found = find_task_by_name(conn, onetime_tasks_name)

        if found:
            print('Task already exist. You can change it or start again in change-task nemu')
            return found.get('''
        onetime_tasks_name,
        onetime_tasks_content,
        onetime_tasks_day,
        onetime_tasks_time,
        onetime_tasks_status
        ''')

        cursor = conn.executescript('''
                             SQL_INSERT_ONETIME_TASKS,
                             (
                             onetime_tasks_name,
                             onetime_tasks_content,
                             onetime_tasks_day,
                             onetime_tasks_time,
                             )
                             ''')
        change_onetime_task_name()
        change_onetime_task_content()
        change_onetime_task_day()
        change_onetime_task_time()

        return cursor
