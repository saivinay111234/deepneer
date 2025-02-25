import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("database/topics.db")
cursor = conn.cursor()

# Take user input for the topic to remove
topic_name = input("Enter the algorithm name to remove: ")

# Delete the topic
cursor.execute("DELETE FROM topics WHERE name=?", (topic_name,))
conn.commit()

# Confirm deletion
if cursor.rowcount > 0:
    print(f"✅ '{topic_name}' has been removed successfully!")
else:
    print(f"⚠️ '{topic_name}' not found in the database.")

conn.close()
