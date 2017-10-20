import sqlite3
import datetime
import os.path as Path


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn

def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())

SQL_SELECT_ALL_TASKS = """
    SELECT tasks.id_tasks,
    tasks.tasks_name,
    tasks.tasks_content,
    tasks.tasks_status,
    cal.tasks_datetime
    FROM tasks, cal
    WHERE tasks.id_tasks=cal.id_tasks
    GROUP BY tasks_status
"""
SQL_SELECT_ALL_BY_DAY = """
    SELECT tasks.id_tasks,
    tasks.tasks_name,
    tasks.tasks_content,
    tasks.tasks_status,
    cal.tasks_date,
    cal.tasks_time
    FROM tasks, cal
    WHERE tasks.id_tasks=cal.id_tasks
    AND tasks_date=?
    GROUP BY tasks_date
"""
SQL_SELECT_ACTUALL = """
    SELECT tasks.id_tasks,
    tasks.tasks_name,
    tasks.tasks_content,
    tasks.tasks_status,
    cal.tasks_date,
    cal.tasks_time
    FROM tasks, cal
    WHERE tasks.id_tasks=cal.id_tasks
    HAVING tasks.tasks_status='Не выполнено'
    GROUP BY cal.tasks_date
"""

SQL_SELECT_ID_BY_NAME = """
    SELECT id_tasks
    FROM tasks
    WHERE tasks_name=?
    """
SQL_SELECT_BY_NAME = """
    SELECT tasks.id_tasks,
    tasks.tasks_name,
    tasks.tasks_content,
    tasks.tasks_status,
    cal.tasks_date,
    cal.tasks_time
    FROM tasks, cal
    WHERE tasks.tasks_name=?
    GROUP BY cal.tasks_date
    """

SQL_INSERT_TASKS = """
    INSERT INTO tasks (
    tasks_name,
    tasks_content
    )
    VALUES (?, ?)
"""
SQL_INSERT_CAL = """
    INSERT INTO cal (
    tasks_date,
    tasks_time,
    id_tasks
    )
    VALUES (?, ?, ?)
"""



SQL_UPDATE_TASK_CONTENT = """
    UPDATE tasks SET tasks_content=? WHERE id_tasks=?
"""

SQL_UPDATE_TASK_NAME = """
    UPDATE tasks SET tasks_name=? WHERE id_tasks=?
"""

SQL_UPDATE_TASK_DATE = """
    UPDATE tasks SET tasks_day=? WHERE id_tasks=?
"""

SQL_UPDATE_TASK_TIME = """
    UPDATE tasks SET tasks_time=? WHERE id_tasks=?
"""

SQL_UPDATE_TASK_STATUS = """
    UPDATE tasks SET tasks_status=? WHERE id_tasks=?
"""

def add_task(conn, tasks_name, tasks_content, tasks_date, tasks_time):
    '''добавляет задачу'''
    tasks_name = tasks_name.lower.rsplit('. ', 1).pop()
    with conn:
        found = find_task_by_name()
        if found:
            print('Задача уже существует. Вы можете изменить задачу или начать ее заново')
        else:
            cursor = conn.execute(SQL_INSERT_TASKS, (tasks_name, tasks_content))
            pk = cursor.lastrowid
            cursor = conn.execute(SQL_INSERT_CAL, (tasks_date, tasks_time, pk))

        return tasks_name, tasks_content, tasks_date, tasks_time


def find_task_by_name(conn, tasks_name):
    '''находит задачу по имени'''
    tasks_name = onetime_tasks_name.lower.rsplit('. ', 1).pop()
    with conn:
        cursor = conn.execute(SQL_SELECT_BY_NAME, (tasks_name,))
        return cursor.fetchone()
    #ввести обработку ошибки, если не нашел (алгоритмы поиска)


def find_task_by_day(conn, tasks_date):
    '''выводит список задач по дню'''
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL_BY_DAY, (tasks_day,))
        return cursor.fetchall()


def show_acutal_tasks(conn):
    with get_connection() as conn:
        cursor = conn.execute(SQL_SELECT_ACTUALL)
        return cursor.fetchall()


def change_task(conn, tasks_name, tasks_content, tasks_date, tasks_time):
    '''коректирует параметры задачи'''
    with conn:
        if tasks_name:
            cursor = conn.execute(SQL_UPDATE_TASK_NAME, (tasks_name, pk))
        if tasks_content:
            cursor = conn.execute(SQL_UPDATE_TASK_CONTENT, (tasks_content, pk))
        if tasks_date:
            cursor = conn.execute(SQL_UPDATE_TASK_DATE, (tasks_date, pk))
        if tasks_time:
            cursor = conn.execute(SQL_UPDATE_TASK_TIME, (tasks_time, pk))
    return i

def change_status(conn, tasks_status):
    with conn:
        cursor = conn.execute(SQL_UPDATE_TASK_STATUS, (tasks_name, pk))
    return


# def all_tasks(conn):
#     '''Выводит все задачи за все время'''
#     with conn:
#         cursor = conn.execute(SQL_SELECT_ALL_TASKS)
#         return cursor.fetchall()
