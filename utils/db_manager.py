"""
Project Cloak Access: utils - db_manager.py

Definition:
Database Management System (DBMS): Software that interacts with end users, applications, 
and the database itself to capture and analyze data. SQLite is a C-language library 
that implements a small, fast, self-contained, high-reliability, full-featured, SQL 
database engine.

Concepts:
1. SQL (Structured Query Language): A domain-specific language used in programming 
   and designed for managing data held in a relational database management system.
2. Relational Database: A digital database based on the relational model of data.
3. Transaction: A logical unit of work that contains one or more SQL statements.
"""

import sqlite3
from datetime import datetime

class DBManager:
    """
    Manager class for handling database operations.
    
    Definition: CRUD - Acronym for Create, Read, Update, and Delete, the four basic 
    functions of persistent storage.
    """
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
    
    def delete_session(self, session_id):
        """
        Deletes a specific session by ID.
        
        Definition: DELETE Statement - An SQL command that removes one or more 
        records from a table.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM sessions WHERE id = ?', (session_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def clear_all_sessions(self):
        """
        Clears all sessions from the database.
        
        Definition: TRUNCATE - An SQL command that removes all records from a 
        table quickly, but SQLite doesn't support TRUNCATE, so we use DELETE.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM sessions')
            conn.commit()
    
    def get_statistics(self):
        """
        Calculates session statistics: total sessions, total duration, average duration.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*), SUM(duration), AVG(duration) FROM sessions')
            result = cursor.fetchone()
            
            return {
                'total_sessions': result[0] or 0,
                'total_duration': result[1] or 0.0,
                'avg_duration': result[2] or 0.0
            }
