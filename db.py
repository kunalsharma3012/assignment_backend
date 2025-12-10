
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "campaigns.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

   
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            clicks INTEGER NOT NULL,
            cost REAL NOT NULL,
            impressions INTEGER NOT NULL
        );
        """
    )


    cursor.execute("SELECT COUNT(*) FROM campaigns;")
    count = cursor.fetchone()[0]

    if count == 0:
       
        campaigns_data = [
            (1, "Summer Sale",       "Active", 150, 45.99, 1000),
            (2, "Black Friday",      "Paused", 320, 89.50, 2500),
            (3, "Diwali Blast",      "Active", 210, 60.00, 1800),
            (4, "New Year Push",     "Paused", 90,  30.25,  900),
            (5, "Winter Clearance",  "Active", 400, 120.75, 5000),
            (6, "Monsoon Offer",     "Active", 175, 50.10, 2000),
            (7, "Festive Sale",      "Paused", 60,  15.99,  600),
            (8, "App Install Drive", "Active", 520, 200.00, 8000),
            (9, "Retargeting Test",  "Paused", 45,  10.50,  450),
            (10, "Brand Awareness",  "Active", 300, 99.99, 7000),
        ]

        cursor.executemany(
            """
            INSERT INTO campaigns (id, name, status, clicks, cost, impressions)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            campaigns_data,
        )
        print("✅ Inserted sample campaigns data")

    conn.commit()
    conn.close()



init_db()
