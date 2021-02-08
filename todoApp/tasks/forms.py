from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,DateField
from wtforms.validators import Email,EqualTo,DataRequired
from datetime import datetime


#Create New Task Form
class createTask(FlaskForm):

    taskname = StringField("Enter the task : ", validators=[DataRequired()])
    dateOfTask = DateField("Enter the date : ",format='%m/%d/%Y', validators=[DataRequired()])
    submit = SubmitField("Create")


#Update Task Form
class updateTask(FlaskForm):
    taskname = StringField("Enter the task", validators=[DataRequired()])
    dateOfTask = DateField("Enter the date", validators=[DataRequired()])
    submit = SubmitField("Update")

