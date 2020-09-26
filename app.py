"""Import flask, sqlalchemy, and forms."""
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "4721760cf3e19483f9fec4b7ead533d0"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

db = SQLAlchemy(app)


class User(db.Model):
    """User database class."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(20), nullable=False, default="default.jpg"
    )
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        """Return username, email, and image_file for User."""
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def __str__(self):
        """Return username, email, and image_file for User."""
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    """Post database class."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        """Return title and date_posted for Post."""
        return f"Post('{self.title}', '{self.date_posted}')"

    def __str__(self):
        """Return title and date_posted for Post."""
        return f"Post('{self.title}', '{self.date_posted}')"


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


@app.route("/home")
@app.route("/")
def home():
    """Show home template."""
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    """Show about template."""
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Show register template."""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Show login template."""
    form = LoginForm()
    if form.validate_on_submit():
        if (
            form.email.data == "starlightromero@gmail.com"
            and form.password.data == "password"
        ):
            flash("You have been logged in!")
            return redirect(url_for("home"))
        flash("Login Unsuccessful. Please verify email and password.")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
