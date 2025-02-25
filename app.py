from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import os
import markdown
import mdx_math

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database/topics.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

# Topics Page
@app.route('/topics')
def topics():
    conn = get_db_connection()
    topics = conn.execute("SELECT * FROM topics WHERE unlocked=1").fetchall()
    conn.close()
    return render_template('topics.html', topics=topics)

# Topic Detail Page
@app.route('/topic/<int:topic_id>')
def topic_detail(topic_id):
    conn = get_db_connection()
    topic = conn.execute("SELECT * FROM topics WHERE id=?", (topic_id,)).fetchone()
    conn.close()
    
    if not topic or topic["unlocked"] == 0:
        return render_template('locked_topic.html', topic=topic)

    # Load Markdown file dynamically
    md_file_path = f"algorithm_content/{topic['name'].lower().replace(' ', '_')}.md"
    if os.path.exists(md_file_path):
        with open(md_file_path, 'r', encoding="utf-8") as file:
            content_html = markdown.markdown(file.read(), extensions=["fenced_code", "tables", mdx_math.MathExtension()])
    else:
        content_html = "<p>🚧 Content for this topic is coming soon...</p>"

    return render_template('topic_detail.html', topic=topic, content_html=content_html)

# Unlock next topic
@app.route('/unlock_next', methods=['POST'])
def unlock_next():
    conn = get_db_connection()
    next_topic = conn.execute("SELECT id FROM topics WHERE unlocked=0 ORDER BY id ASC LIMIT 1").fetchone()

    if next_topic:
        conn.execute("UPDATE topics SET unlocked=1 WHERE id=?", (next_topic["id"],))
        conn.commit()
    
    conn.close()
    return redirect(url_for('topics'))

# Chat System for Questions & Answers
@app.route('/topic/<int:topic_id>/chat', methods=['GET', 'POST'])
def topic_chat(topic_id):
    conn = get_db_connection()

    if request.method == 'POST':
        data = request.get_json()
        conn.execute("INSERT INTO chat (topic_id, username, message) VALUES (?, ?, ?)",
                     (topic_id, data['username'], data['message']))
        conn.commit()

    messages = conn.execute("SELECT username, message FROM chat WHERE topic_id=?", (topic_id,)).fetchall()
    conn.close()
    
    return jsonify({"messages": [dict(msg) for msg in messages]})

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"📩 New Contact Message from {name} ({email}): {message}")
        return render_template('contact.html', message="✅ Message sent successfully!")
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)
