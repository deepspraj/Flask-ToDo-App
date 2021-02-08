from todoApp import db, login_manager
from flask import Flask
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
from todoApp.users.profilePicHandler import addProfilePic
from todoApp.users.locationHandler import locationFinder



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(64),  unique=True, index=True)
    email = db.Column(db.String(64),  unique=True, index=True)
    passwordHashed = db.Column(db.String(128))
    joined = db.Column(db.String(64))
    profileImage = db.Column(db.String)
    location = db.Column(db.String(64))

    taskData = db.relationship('tasks', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.passwordHashed = generate_password_hash(password)
        self.joined = date.today().strftime("%b-%d-%Y")
        self.profileImage = addProfilePic()
        self.location = locationFinder()

    def checkPassword(self,password):
        return check_password_hash(self.passwordHashed,password)

    def __repr__(self):
        return f"Email : {self.email}\nUsername : {self.username}.\nPassword : {self.passwordHashed}"



class tasks(db.Model):
    
    __tablename__ = 'Task'
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    task = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    dateOfCreation = db.Column(db.String(64))
    


    def __init__(self, task, date, userId):
        self.task = task
        self.date = date
        self.userId = userId
        self.dateOfCreation = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def __repr__(self):

        return f"Task : {self.task}.\nDate : {self.date}. UserID : {self.userId}."



        