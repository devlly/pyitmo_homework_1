import sqlite3
import os.path as Path

SQL_SELECT_ALL = """
    SELECT id, task_name, task_content, task_status, to_do_time
    FROM organazier
"""

SQL_SELECT_BY_PK = SQL_SELECT_ALL + " WHERE id=?"
SQL_SELECT_BY_TASK_NAME = SQL_SELECT_ALL + " WHERE task_name=?"
SQL_SELECT_BY_TASK_STATUS = SQL_SELECT_ALL + " WHERE task_status=?"
SQL_SELECT_BY_TO_DO_TIME = SQL_SELECT_ALL + " WHERE to_do_time=?"

SQL_INSERT_TASK_NAME = """
    INSERT INTO organizer (task_name) VALUES (?)
"""
SQL_INSERT_TASK_CONTENT = """
    INSERT INTO organizer (task_content) VALUES (?)
"""

SQL_INSERT_TO_DO_TIME = """
    INSERT INTO organizer (to_do_time) VALUES (?)
"""

SQL_UPDATE_TASK_CONTENT = """
    UPDATE organizer SET task_content=? WHERE id=?
"""
SQL_UPDATE_TASK_NAME = """
    UPDATE organizer SET task_name=? WHERE id=?
"""
SQL_UPDATE_TASK_STATUS = """
    UPDATE organizer SET task_status=? WHERE id=?
"""
SQL_UPDATE_TO_DO_TIME = """
    UPDATE organizer SET to_do_time=? WHERE id=?
"""

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())



def all_task(conn):
    print('выводит все задачи, какие есть')


def task_list_by_day(conn, to_do_time):
    print('выводит список задач на сегодня')

def add_task(conn, task_name, task_content, time_to_do):
    print('добавляет задачу')

def change_task(conn, task_name, task_content, time_to_do):
    print('изменяет задачу')

def change_status(conn, task_status):
    print('завершает или начинает задачу заново')


fun = [0, all_task(), add_task(), change_status(), change_status()]

while 1>0:

    print("""Ежедневник. Выберете действие:\n
    1. Вывести список задач\n
    2. Добавить задачу\n
    3. Отредактировать задачу\n
    4. Завершить задачу\n
    5. Начать задачу сначала\n
    6. Выход\n
     """)

    i = int(input())
    if i in range(6):
        print(fun[i])
    if i == 6: 
        break 

print('конец программы')











