from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from flask_blog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """Load logged in user with given id."""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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

    def get_reset_token(self, expires_sec=900):
        """Generate user token to reset password."""
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_token(token):
        """Verify given token."""
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except ValueError:
            return None
        return User.query.get(user_id)


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
