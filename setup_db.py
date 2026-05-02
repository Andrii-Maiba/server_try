import sqlite3
import bcrypt

# Connect to SQLite database
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

# Insert or update sample user (username: Dog, password: 12345)
hashed = bcrypt.hashpw('12345'.encode('utf-8'), bcrypt.gensalt())
cursor.execute("INSERT OR REPLACE INTO users (username, password_hash) VALUES (?, ?)", ('Dog', hashed.decode('utf-8')))

conn.commit()
cursor.close()
conn.close()

print("Database and table created successfully.")