#  import the main web development frame work 
from flask import Flask
#  import render_template to render gtml on the browser 
from flask import render_template
#  import request  to access every request related from HTTP with request
from flask import request
#  import redirect to redirects to other rputs
from flask import redirect

#  import url_for to generate url based on the view function name

from flask import url_for



#  used to get the basepath to get the other file like(static, html)
app = Flask(__name__)

#  static data to mimic databases

posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is my first post!'},
    {'id': 2, 'title': 'Second Post', 'content': 'Here is my second post.'}
]

@app.route("/")
def index():
    return render_template("index.html", posts = posts)
@app.route("/create", methods = ["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        post_id = len(posts) + 1
        post = {
            "id":post_id, 
            "title": title, 
            "content": content
        }
        posts.append(post)
        return redirect(url_for("index"))
    return render_template("create.html")

@app.route("/edit/<int:post_id>", methods = ["GET", "POST"])

def edit(post_id):
    post = next((post for post in posts if post["id"]== post_id))
    if not post:
        return "No Post", 404
    if request.method == "POST":
        post["title"] = request.form["title"]
        post["content"] = request.form["content"]
        return redirect(url_for("index"))
    return render_template("edit.html", post = post)
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
