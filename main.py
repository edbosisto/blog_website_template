from flask import Flask, render_template
import datetime
import requests
import os


app = Flask(__name__)
current_year = datetime.datetime.now().year

# Get blog data from custom npoint API
blog_url = os.environ.get("BLOG_URL")
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", year=current_year, posts=all_posts)


@app.route('/about')
def get_about():
    return render_template("about.html", year=current_year)


@app.route('/contact')
def get_contact():
    return render_template("contact.html", year=current_year)


@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
