# backend/models/database.py

import sqlite3
from datetime import datetime

conn = sqlite3.connect("qa_data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS qa_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        filename TEXT,
        prompt TEXT,
        answer TEXT,
        timestamp TEXT
    )
""")
conn.commit()

def save_to_db(email, filename, prompt, answer):
    timestamp = datetime.now().isoformat()
    cursor.execute(
        "INSERT INTO qa_data (email, filename, prompt, answer, timestamp) VALUES (?, ?, ?, ?, ?)",
        (email, filename, prompt, answer, timestamp)
    )
    conn.commit()
