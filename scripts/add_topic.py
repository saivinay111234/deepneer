import sqlite3

conn = sqlite3.connect("database/topics.db")
cursor = conn.cursor()

# Take user input for new algorithm
new_topic_name = input("Enter the algorithm name: ")
new_category = input("Enter the category (Supervised Learning / Unsupervised Learning / Reinforcement Learning): ")
unlocked_status = int(input("Enter 1 if unlocked, 0 if locked: "))  # 0 = Locked, 1 = Unlocked
youtube_link = input("Enter YouTube Video ID (e.g., CtsRRUddV2s): ")
notebook_file = input("Enter Notebook Filename (e.g., linear_regression.ipynb): ")

# Check if topic already exists
cursor.execute("SELECT * FROM topics WHERE name=?", (new_topic_name,))
existing_topic = cursor.fetchone()

if existing_topic:
    print(f"⚠️ '{new_topic_name}' already exists in {existing_topic[2]}.")
else:
    # Insert new topic
    cursor.execute("INSERT INTO topics (name, category, unlocked, youtube_link, notebook_file) VALUES (?, ?, ?, ?, ?)", 
                   (new_topic_name, new_category, unlocked_status, youtube_link, notebook_file))
    conn.commit()
    print(f"✅ '{new_topic_name}' added successfully to {new_category}!")

conn.close()
