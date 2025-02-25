import sqlite3
import os

# Ensure the database directory exists
db_path = "database/topics.db"
if not os.path.exists("database"):
    os.makedirs("database")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the topics table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        unlocked INTEGER DEFAULT 0,
        youtube_link TEXT,
        notebook_file TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id INTEGER,
        username TEXT NOT NULL,
        message TEXT NOT NULL,
        FOREIGN KEY (topic_id) REFERENCES topics(id)
    )
""")
conn.commit()

# Insert a sample topic with YouTube and Notebook details
topics = [
    ("Linear Regression", "Supervised Learning", 1, "CtsRRUddV2s", "linear_regression.ipynb")  # Only YouTube ID
]

cursor.executemany("INSERT INTO topics (name, category, unlocked, youtube_link, notebook_file) VALUES (?, ?, ?, ?, ?)", topics)
conn.commit()
conn.close()

print("✅ Database initialized with default topics!")
