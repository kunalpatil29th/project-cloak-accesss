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
4. Input Validation: The process of ensuring that user input is safe, correct, and useful.
"""

import sqlite3
from datetime import datetime
from typing import Optional, List, Dict, Tuple, Any
import sys
import os

# Add parent directory to import logger
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger import logger


class DBManager:
    """
    Manager class for handling database operations.
    
    Definition: CRUD - Acronym for Create, Read, Update, and Delete, the four basic 
    functions of persistent storage.
    """
    def __init__(self, db_name: str = 'cloak_sessions.db') -> None:
        self.db_name: str = db_name
        self.init_db()

    def init_db(self) -> None:
        try:
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
                logger.info(f"Database initialized: {self.db_name}")
        except sqlite3.Error as e:
            logger.error(f"Database initialization error: {e}")

    def log_session(self, start_time: datetime, end_time: datetime) -> None:
        try:
            if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
                raise TypeError("start_time and end_time must be datetime objects")
            
            duration: float = (end_time - start_time).total_seconds()
            
            if duration < 0:
                raise ValueError("end_time must be after start_time")
            
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO sessions (start_time, end_time, duration)
                    VALUES (?, ?, ?)
                ''', (start_time.isoformat(), end_time.isoformat(), duration))
                conn.commit()
                logger.info(f"Session logged: {duration:.2f} seconds")
        except Exception as e:
            logger.error(f"Error logging session: {e}")

    def get_all_sessions(self) -> List[Tuple[Any, ...]]:
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM sessions ORDER BY id DESC')
                return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Error fetching sessions: {e}")
            return []
    
    def delete_session(self, session_id: int) -> bool:
        """
        Deletes a specific session by ID.
        
        Definition: DELETE Statement - An SQL command that removes one or more 
        records from a table.
        """
        try:
            if not isinstance(session_id, int) or session_id <= 0:
                raise ValueError("session_id must be a positive integer")
            
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM sessions WHERE id = ?', (session_id,))
                conn.commit()
                deleted = cursor.rowcount > 0
                if deleted:
                    logger.info(f"Session {session_id} deleted")
                return deleted
        except Exception as e:
            logger.error(f"Error deleting session: {e}")
            return False
    
    def clear_all_sessions(self) -> None:
        """
        Clears all sessions from the database.
        
        Definition: TRUNCATE - An SQL command that removes all records from a 
        table quickly, but SQLite doesn't support TRUNCATE, so we use DELETE.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM sessions')
                conn.commit()
                logger.info("All sessions cleared")
        except sqlite3.Error as e:
            logger.error(f"Error clearing sessions: {e}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Calculates session statistics: total sessions, total duration, average duration.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT COUNT(*), SUM(duration), AVG(duration) FROM sessions')
                result: Optional[Tuple[Optional[int], Optional[float], Optional[float]]] = cursor.fetchone()
                
                if result is None:
                    return {
                        'total_sessions': 0,
                        'total_duration': 0.0,
                        'avg_duration': 0.0
                    }
                
                stats = {
                    'total_sessions': result[0] or 0,
                    'total_duration': result[1] or 0.0,
                    'avg_duration': result[2] or 0.0
                }
                logger.info(f"Statistics: {stats}")
                return stats
        except sqlite3.Error as e:
            logger.error(f"Error getting statistics: {e}")
            return {
                'total_sessions': 0,
                'total_duration': 0.0,
                'avg_duration': 0.0
            }
