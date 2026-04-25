import sqlite3

def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade TEXT)")
    conn.execute("INSERT OR IGNORE INTO students VALUES (1,'Alice','A')")
    conn.execute("INSERT OR IGNORE INTO students VALUES (2,'Bob','B')")
    conn.execute("INSERT OR IGNORE INTO students VALUES (3,'Charlie','A+')")
    conn.commit()

def get_all_students():
    conn = get_db()
    return conn.execute("SELECT * FROM students").fetchall()
