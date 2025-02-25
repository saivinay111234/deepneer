import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("database/topics.db")
cursor = conn.cursor()

# Fetch and display all topics
cursor.execute("SELECT * FROM topics")
topics = cursor.fetchall()

print("\n📌 Current Topics in Database:")
print("---------------------------------------------------")
for topic in topics:
    status = "✅ Unlocked" if topic[3] == 1 else "🔒 Locked"
    print(f"{topic[0]}. {topic[1]} - {topic[2]} ({status})")

conn.close()
