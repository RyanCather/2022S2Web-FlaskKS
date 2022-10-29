from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, FileField, BooleanField
from flask_wtf.file import FileRequired
from models import User


# used to check the entries submitted on the contact us page are valid (called when form is submitted in app.py)
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], render_kw={"class": "form-control",
                                                                       "placeholder": "Name"})  # checks there is actual data being submitted
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"class": "form-control",
                                                                                  "placeholder": "Email"})  # checks there is actual data being submitted and that it is a valid email address
    message = TextAreaField("Message", validators=[DataRequired()], render_kw={"class": "form-control",
                                                                               "placeholder": "Message to send"})  # checks there is actual data being submitted
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})


# used for uploading photos to the website
class PhotoUploadForm(FlaskForm):
    title = StringField("Image Title", validators=[DataRequired()],
                        render_kw={"class": "form-control", "placeholder": "Name"})
    image = FileField('Photo File Upload', validators=[FileRequired()], render_kw={"class": "form-control"})
    submit = SubmitField("Upload Photo", render_kw={"class": "btn btn-primary"})


# used for registering a new user
class RegistrationForm(FlaskForm):
    email_address = StringField("Email Address", validators=[DataRequired(), Email()],
                                render_kw={"class": "form-control", "placeholder": "Email"})
    name = StringField("Name (Username)", validators=[DataRequired()],
                       render_kw={"class": "form-control", "placeholder": "Full Name"})
    password = PasswordField("Password", validators=[DataRequired()],
                             render_kw={"class": "form-control", "placeholder": "Password"})
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")],
                                     render_kw={"class": "form-control", "placeholder": "Confirm Password"})
    submit = SubmitField("Register", render_kw={"class": "btn btn-primary"})

    def validate_email_address(self, email_address_to_register):
        user = User.query.filter_by(email_address=email_address_to_register.data).first()
        if user is not None:
            raise ValidationError("Please Use a Different Email Address)")


# user log in form
class LoginForm(FlaskForm):
    email_address = StringField('Email Address', validators=[DataRequired()],
                                render_kw={"placeholder": "user@gmail.com", "class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={"placeholder": "password", "class": "form-control",
                                        "aria-describedby": "basic-addon2"})  # value doesnt work
    submit = SubmitField('Sign In', render_kw={"class": "btn btn-primary"})


# reset password form
class ResetPasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()],
                                     render_kw={"class": "form-control", "placeholder": "Current Password"})
    new_password = StringField('New Password', validators=[DataRequired()],
                               render_kw={"class": "form-control", "placeholder": "New Password"})
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("new_password")],
                                     render_kw={"class": "form-control", "placeholder": "Confirm Password"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})


# reset password form for admins
class ResetPasswordFormAdmin(FlaskForm):
    new_password = StringField('New Password', validators=[DataRequired()],
                               render_kw={"class": "form-control", "placeholder": "New Password"})
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("new_password")],
                                     render_kw={"class": "form-control", "placeholder": "Confirm Password"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})


class TodoForm(FlaskForm):
    text = StringField('text', validators=[DataRequired()],
                       render_kw={"placeholder": "Add a new TODO item", "class": "form-control"})
    submit = SubmitField('Create new entry', render_kw={"class": "btn btn-primary"})