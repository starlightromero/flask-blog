from flask import render_template, flash, redirect, url_for
from flask_blog import app, db, bcrypt
from flask_blog.models import User, Post
from flask_blog.forms import RegistrationForm, LoginForm

posts = []


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
        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")
        user = Username(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(User)
        db.session.commit()
        flash(f"Your account has been created! You are now able to log in.")
        return redirect(url_for("login"))
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
