
import sqlite3
from pathlib import Path

# Database file location
DB_PATH = Path(__file__).with_name("schemes.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS schemes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            state TEXT,
            category TEXT,
            description TEXT,
            eligibility TEXT,
            benefits TEXT,
            documents TEXT,
            application_process TEXT,
            official_url TEXT,
            source TEXT,
            last_verified TEXT
        )
    """)

    connection.commit()
    connection.close()
