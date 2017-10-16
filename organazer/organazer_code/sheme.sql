'''CREATE TABLE IF NOT EXIST regtasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    regtasks_name TEXT NOT NULL,
    regtasks_content TEXT NOT NULL DEFAULT '',
    regtasks_status TEXT NOT NULL DEFAULT 'Не выполнено',
    regtasks_start_date DATE NOT NULL DEFAULT CURRENT_DAY,
    regtasks_weekday DATE NOT NULL DEFAULT WEEKDAY,
    regtasks_time DATETIME NOT NULL DEFAULT ''

)'''

CREATE TABLE IF NOT EXIST onetime_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    onetime_tasks_name TEXT NOT NULL,
    onetime_tasks_content TEXT NOT NULL DEFAULT '',
    onetime_tasks_day DATE NOT NULL DEFAULT CURRENT_DATE,
    onetime_tasks_time DATETIME NOT NULL DEFAULT '',
    onetime_tasks_status TEXT NOT NULL DEFAULT 'Не выполнено',

)


'''CREATE TABLE IF NOT EXIST calendar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cal_plan_date DATE NOT NULL,
    cal_tasks_body TEXT NOT NULL DEFAULT ''
)'''
