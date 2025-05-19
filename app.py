from flask import Flask, render_template, request, redirect, url_for
import markdown
import os

app = Flask(__name__)
POSTS_DIR = "posts"

def estimate_reading_time(text):
    words = text.split()
    words_per_minute = 100
    time = max(1, len(words) // words_per_minute)
    return f"(Est. {time} min read)"

@app.route('/')
def index():
    query = request.args.get('q', '').lower()
    all_posts = [f[:-3] for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    if query:
        posts = [post for post in all_posts if query in post.lower()]
    else:
        posts = all_posts
    return render_template("index.html", posts=posts)

@app.route('/post/<title>')
def post(title):
    filepath = os.path.join(POSTS_DIR, f"{title}.md")
    if not os.path.exists(filepath):
        return "Post not found", 404
    with open(filepath, "r", encoding='utf-8') as f:
        lines = f.readlines()
        if lines[0].startswith("Tags:"):
            tags_line = lines[0][5:].strip()
            tags = [tag.strip() for tag in tags_line.split(",") if tag.strip()]
            content = "".join(lines[2:]) 
        else:
            tags = []
            content = "".join(lines)
    html = markdown.markdown(content)
    reading_time = estimate_reading_time(content)
    return render_template("post.html", title=title, content=html, tags=tags, reading_time=reading_time)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags']
        filename = os.path.join(POSTS_DIR, f"{title}.md")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Tags: {tags}\n\n{content}")
        return redirect(url_for('index'))
    return render_template("create.html")

@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit(title):
    filepath = os.path.join(POSTS_DIR, f"{title}.md")
    if not os.path.exists(filepath):
        return "Post not found", 404

    if request.method == 'POST':
        content = request.form['content']
        with open(filepath, "w", encoding='utf-8') as f:
            f.write(content)
        return redirect(url_for('post', title=title))

    with open(filepath, "r", encoding='utf-8') as f:
        content = f.read()
    return render_template("edit.html", title=title, content=content)

@app.route('/delete/<title>')
def delete(title):
    filepath = os.path.join(POSTS_DIR, f"{title}.md")
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect(url_for('index'))

@app.route('/tag/<tag>')
def tagged(tag):
    all_posts = [f[:-3] for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    matched = []
    for title in all_posts:
        filepath = os.path.join(POSTS_DIR, f"{title}.md")
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline()
            if first_line.startswith("Tags:") and tag in first_line:
                matched.append(title)
    return render_template("index.html", posts=matched)

if __name__ == '__main__':
    os.makedirs(POSTS_DIR, exist_ok=True)
    app.run(debug=True)
