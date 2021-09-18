from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Jasim Ahmed",
        "title": "Blog post 1",
        "content": "second post content",
        "date_posted": "April 21, 2021"
    },    
    {
        "author": "Jane Doe",
        "title": "Blog post 2",
        "content": "first post content",
        "date_posted": "June 28, 2020"
    },
    {
        "author": "Happy Jane",
        "title": "Blog post 3",
        "content": "Last post content",
        "date_posted": "July 28, 2021"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)
    # return "<h1>Home Page!<h1>"

@app.route("/about")
def about():
    return render_template("about.html", title="About")
    # return "<h1> About page is running<h1>"

if __name__ == "__main__":
    app.run(debug=True)
