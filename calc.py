import sqlite3

def create_db():
    conn = sqlite3.connect("specimen_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS specimens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            microscope_size REAL,
            magnification REAL,
            actual_size REAL
        )
    """)
    conn.commit()
    conn.close()

def save_record(username, microscope_size, magnification, actual_size):
    conn = sqlite3.connect("specimen_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO specimens (username, microscope_size, magnification, actual_size)
        VALUES (?, ?, ?, ?)
    """, (username, microscope_size, magnification, actual_size))
    conn.commit()
    conn.close()



