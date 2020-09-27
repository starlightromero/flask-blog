"""Import flask, sqlalchemy, and forms."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["ENV"] = "development"
app.config["DEBUG"] = True
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "4721760cf3e19483f9fec4b7ead533d0"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

from flask_blog import routes
