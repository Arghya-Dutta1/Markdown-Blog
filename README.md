
# 📖 Markdown Blog

A simple Flask-based blog where users can create and view blog posts written in **Markdown**.

## 🚀 Features

- Create new blog posts using Markdown syntax
- View posts rendered as HTML
- Live routing for individual blog posts
- Edit/Delete existing posts
- Search posts by title
- Add and filter posts by tags
- Input sanitization using the `markdown` library
- Clean templated layout using Flask's `Jinja2`

## 🛠 Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (with Jinja2 templating)
- **Markdown Parser**: Python `markdown` library

## 📁 Project Structure

```
markdown_blog/
├── app.py                 # Main Flask application
├── templates/             # HTML templates (base, index, post, create, edit)
│   ├── base.html
│   ├── index.html
│   ├── post.html
│   ├── create.html
│   └── edit.html
├── static/                # Static files (CSS)
│   └── style.css
├── posts/                 # Folder where markdown posts are stored
│   └── sample.md
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## ✅ Installation & Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/markdown-blog.git
   cd markdown-blog
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**
   ```bash
   python app.py
   ```

4. **Visit in Browser**
   ```
   http://127.0.0.1:5000/
   ```

## 🔍 Search

Search posts by title using the search box on the homepage.

## 🏷 Tags

- Add tags when creating a post (comma-separated).
- Tags are shown on each post's page.
- Click on a tag to view all related posts.

## 📝 Edit/Delete

- Edit the content of any existing post.
- Delete posts with a confirmation prompt.

## 🔒 Security

- Markdown rendering is safely handled by the `markdown` module.
- Flask auto-escapes HTML unless explicitly marked as safe (`| safe` filter used carefully).

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Happy blogging ✨
