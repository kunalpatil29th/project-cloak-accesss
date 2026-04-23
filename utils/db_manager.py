import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_name='cloak_sessions.db'):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    start_time TEXT,
                    end_time TEXT,
                    duration REAL
                )
            ''')
            conn.commit()

    def log_session(self, start_time, end_time):
        duration = (end_time - start_time).total_seconds()
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO sessions (start_time, end_time, duration)
                VALUES (?, ?, ?)
            ''', (start_time.isoformat(), end_time.isoformat(), duration))
            conn.commit()

    def get_all_sessions(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM sessions ORDER BY id DESC')
            return cursor.fetchall()
