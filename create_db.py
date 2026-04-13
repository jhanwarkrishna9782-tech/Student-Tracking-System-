import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
branch TEXT,
skills TEXT,
email TEXT,
phone TEXT,
college TEXT,
year TEXT,
resume TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")