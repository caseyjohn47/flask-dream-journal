from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, length
from app.models import User

# Form for logging in
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# Form for a new journal entry
class NewEntryForm(FlaskForm):
    entry = StringField('Entry', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form for editing a journal entry
class EditEntryForm(FlaskForm):
    entry = StringField('Entry', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form for editing about me
class EditProfileForm(FlaskForm):
    about_me = StringField('About Me', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form for registering a new user
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
