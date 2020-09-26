"""Import flask and forms."""
from flask import Flask, render_template, flash, redirect, url_for
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
