from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,DateField, ValidationError
from wtforms.validators import Email,EqualTo,DataRequired
from todoApp.models import User


# Login

class loginUserForm(FlaskForm):


    username = StringField("Enter the username : ")
    password = PasswordField("Enter the password : ")
    submit = SubmitField("Log IN")


# Register

class registerUserForm(FlaskForm):

    username =StringField("Enter the username : ", validators=[DataRequired()])
    email = StringField("Enter the email : ", validators=[DataRequired(), Email()])
    password = PasswordField("Enter the password : ", validators=[DataRequired(),EqualTo('passwordConfirm', message="Password must match")])
    passwordConfirm = PasswordField("Confirm the password : ", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validateEmail(self, field):

        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validateUsername(self, field):

        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')






