from flask import Flask, render_template, request, redirect, url_for
import markdown
import os

app = Flask(__name__)
POSTS_DIR = "posts"

@app.route('/')
def index():
    posts = [f[:-3] for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    return render_template("index.html", posts=posts)

@app.route('/post/<title>')
def post(title):
    filepath = os.path.join(POSTS_DIR, f"{title}.md")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding='utf-8') as f:
            content = f.read()
            html = markdown.markdown(content)
            return render_template("post.html", title=title, content=html)
    return "Post not found", 404

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        with open(os.path.join(POSTS_DIR, f"{title}.md"), "w", encoding='utf-8') as f:
            f.write(content)
        return redirect(url_for('post', title=title))
    return render_template("create.html")

if __name__ == '__main__':
    os.makedirs(POSTS_DIR, exist_ok=True)
    app.run(debug=True)
