import sqlite3

def init_db():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT NOT NULL,

        description TEXT NOT NULL,

        status TEXT DEFAULT 'Open',

        priority TEXT DEFAULT 'Medium',

        assigned_to TEXT DEFAULT 'Unassigned'
    )
    """)

    conn.commit()
    conn.close()