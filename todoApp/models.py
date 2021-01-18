from todoApp import db, login_manager
from flask import Flask
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(64),  unique=True, index=True)
    email = db.Column(db.String(64),  unique=True, index=True)
    passwordHashed = db.Column(db.String)

    taskData = db.relationship('tasks', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.passwordHashed = generate_password_hash(password)


    def checkPassword(self,password):
        return check_password_hash(self.passwordHashed,password)

    def __repr__(self):
        return f"Email : {self.email}\nUsername : {self.username}.\nPassword : {self.passwordHashed}"



class tasks(db.Model):
    
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    task = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    dateOfCreation = db.Column(db.DateTime, nullable=False, default=datetime.now)
    


    def __init__(self, task, date, userId):
        self.task = task
        self.date = date
        self.userId = userId


    def __repr__(self):

        return f"Task : {self.task}.\nDate : {self.date}. UserID : {self.userId}."



        