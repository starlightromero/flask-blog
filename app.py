from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Starlight Romero",
        "title": "Blog Post One",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Starlight Romero",
        "title": "Blog Post Two",
        "date_posted": "April 21, 2018",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
