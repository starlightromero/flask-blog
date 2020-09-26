from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "4721760cf3e19483f9fec4b7ead533d0"

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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
