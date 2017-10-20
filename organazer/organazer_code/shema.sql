
CREATE TABLE IF NOT EXIST tasks (
    id_tasks INTEGER PRIMARY KEY AUTOINCREMENT,
    tasks_name UNIQUE TEXT NOT NULL,
    tasks_content TEXT NOT NULL DEFAULT '',
    tasks_status TEXT NOT NULL DEFAULT 'Не выполнено',
)

-- CREATE TABLE IF NOT EXIST cal (
--     id_cal INTEGER PRIMARY KEY AUTOINCREMENT,
--     tasks_date TEXT NOT NULL DEFAULT CURRENT_DATE,
--     tasks_time TEXT NOT NULL DEFAULT '',
--     id_tasks INTEGER
-- )
--
-- CREATE INDEX index_task ON cal (id_tasks)
-- CREATE INDEX index_name ON tasks (tasks_name)