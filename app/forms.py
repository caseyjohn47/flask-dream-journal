from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

# Form for logging in
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=128)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# Form for a new journal entry
class NewEntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    entry = StringField('Entry', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Submit')

# Form for editing a journal entry
class EditEntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    entry = StringField('Entry', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Submit')

# Form for editing about me
class EditProfileForm(FlaskForm):
    about_me = StringField('About Me', validators=[DataRequired(), Length(max=140)])
    submit = SubmitField('Submit')

# Form for registering a new user
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=128)])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password'), Length(max=128)])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
