from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,DateField, ValidationError, FileField
from wtforms.validators import Email, EqualTo, DataRequired
from flask_wtf.file import FileAllowed
from todoApp.models import User


#Login Form
class loginUserForm(FlaskForm):

    username = StringField("Enter the username : ",validators=[DataRequired()])
    password = PasswordField("Enter the password : ",validators=[DataRequired()])
    submit = SubmitField("Log IN")


#Registeration Form
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


#Change Profile Pic Form
class updateProfilePicForm(FlaskForm):
	    
	    picture = FileField("Update Profile Picture : ", validators=[FileAllowed(['jpg', 'png'])])
	    submit = SubmitField("Update Profile Picture")
	

#Change Password Form	
class updatePasswordForm(FlaskForm):

    password = PasswordField("Enter the password : ", validators=[DataRequired(),EqualTo('passwordConfirm', message="Password must match")])
    passwordConfirm = PasswordField("Confirm the password : ", validators=[DataRequired()])
    submit = SubmitField("Update Password")


#Forgot Password Form
class forgotPasswordForm(FlaskForm):

    email = StringField("Enter the email : ", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")


#Reset Password Form
class resetPasswordForm(FlaskForm):
    password = PasswordField("Enter the password : ", validators=[DataRequired(),EqualTo('passwordConfirm', message="Password must match")])
    passwordConfirm = PasswordField("Confirm the password : ", validators=[DataRequired()])
    submit = SubmitField("Submit")


#Otp Verification Form
class otpVerification(FlaskForm):

    otpData = StringField('Enter the otp : ', validators=[DataRequired()])
    submit = SubmitField('Verify')

#New Password Form
class resetPasswordForm(FlaskForm):
    password = PasswordField("Enter the password : ", validators=[DataRequired(),EqualTo('passwordConfirm', message="Password must match")])
    passwordConfirm = PasswordField("Confirm the password : ", validators=[DataRequired()])
    submit = SubmitField("Submit")