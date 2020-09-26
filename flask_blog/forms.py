from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
)
from flask_blog.models import User


class RegistrationForm(FlaskForm):
    """User Resistration Form."""

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=20)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    @staticmethod
    def validate_username(username):
        """Validate username is not taken."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "That username is taken. Please choose a different username."
            )

    @staticmethod
    def validate_email(email):
        """Validate email is not in use."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                """
                The email is already in use. Please enter a different email.
                Alternatively, if you forgot your password, go to the login
                page and click \"Forgot Password\".
                """
            )


class LoginForm(FlaskForm):
    """User Login Form."""

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=20)]
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
