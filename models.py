from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# for contact us form to use what the user has submitted
class ContactForm(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    message = db.Column(db.Text)
    dateSubmitted = db.Column(db.DateTime)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message
        self.dateSubmitted = datetime.today()  # inserts current date and time to be stored into table


# for photos form
class Photos(db.Model):
    photoid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    filename = db.Column(db.String(255))
    userid = db.Column(db.Integer)
    dateSubmitted = db.Column(db.DateTime)
    enabled = db.Column(db.Boolean)

    # this functions will make it easier to create new entries in the database when uploading images
    def __init__(self, title, filename, userid, enabled):
        self.title = title
        self.filename = filename
        self.userid = userid
        self.dateSubmitted = datetime.today()
        self.enabled = enabled


# for To do form to use what the user has submitted
class Todo (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    text = db.Column(db.Text)
    done = db.Column(db.Boolean)

    def __init__(self, text, user_id, done):
        self.user_id = user_id
        self.text = text
        self.done = done


# for user registration
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    user_level = db.Column(db.Integer)
    active = db.Column(db.Boolean)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        if self.user_level == 2:
            return True
        else:
            return False


# The flask login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))