import sqlite3, datetime

def get_conn():
    conn = sqlite3.connect("tasks.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title TEXT,
        due TEXT,
        status TEXT DEFAULT 'pending'
    )""")
    return conn

def add_task(title: str, due: str):
    conn = get_conn()
    conn.execute("INSERT INTO tasks(title, due) VALUES(?, ?)", (title, due))
    conn.commit(); conn.close()
    return "Task added."

def list_tasks(status="pending"):
    conn = get_conn()
    cur = conn.execute("SELECT id, title, due, status FROM tasks WHERE status=?", (status,))
    rows = cur.fetchall(); conn.close()
    return rows

def mark_done(task_id: int):
    conn = get_conn()
    conn.execute("UPDATE tasks SET status='done' WHERE id=?", (task_id,))
    conn.commit(); conn.close()
    return "Marked done."

def due_soon(hours=24):
    conn = get_conn()
    now = datetime.datetime.now()
    soon = (now + datetime.timedelta(hours=hours)).isoformat(timespec="minutes")
    cur = conn.execute("SELECT id,title,due FROM tasks WHERE status='pending' AND due<=?", (soon,))
    rows = cur.fetchall(); conn.close()
    return rows
