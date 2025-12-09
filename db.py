import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "campaigns.db"


def get_connection():
    # connect to SQLite DB file
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # allows dict(row)
    return conn
