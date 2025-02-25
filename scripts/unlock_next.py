import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("database/topics.db")
cursor = conn.cursor()

# Find the next locked topic
cursor.execute("SELECT id, name FROM topics WHERE unlocked=0 ORDER BY id ASC LIMIT 1")
next_topic = cursor.fetchone()

if next_topic:
    cursor.execute("UPDATE topics SET unlocked=1 WHERE id=?", (next_topic[0],))
    conn.commit()
    print(f"✅ '{next_topic[1]}' has been unlocked!")
else:
    print("⚠️ No locked topics left to unlock.")

conn.close()
