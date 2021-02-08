from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import logout_user, login_required, current_user, login_user
from todoApp.users.forms import *
from todoApp.models import User
from todoApp import db
from todoApp.core.views import core
from todoApp.error.errorHandlers import errorPages
from todoApp.users.otpHandler import otpGenerate
from cryptography.fernet import Fernet
from todoApp.users.otpHandler import otpGenerate
from werkzeug.security import generate_password_hash
from todoApp.users.profilePicHandler import addProfilePic

users = Blueprint('users', __name__)


#Account View
@users.route('/account')
@login_required
def account():

    return render_template('account.html', current_user=current_user)


#logout View
@users.route('/logout')
@login_required
def logoutUser():

    logout_user()
    
    return redirect(url_for('core.home'))


#login View
@users.route('/login', methods=['GET','POST'])
def loginUser():

    form = loginUserForm()

    if form.validate_on_submit():

        logUser = User.query.filter_by(username= form.username.data).first()

        if logUser.checkPassword(password=form.password.data) and logUser is not None:
            login_user(logUser)
            flash("User successfully logged in..!!")

            return redirect('account')

        if logUser is None:
	            return render_template('error.html')


    return render_template('login.html', form=form)



#Register View
@users.route('/register', methods=['GET', 'POST'])
def registerUser():

    form = registerUserForm()  

    if form.validate_on_submit():
        if (User.query.filter_by(email=form.email.data).first() is None) and (User.query.filter_by(username=form.username.data).first() is None):
            newRegister = otpGenerate()
            dataOtp = newRegister.otpGenerater(receiverEmail=form.email.data)

            key = Fernet.generate_key()

            with open('key.txt', 'wb') as safeKey:
                safeKey.write(key)

            f = Fernet(key)

            userName = f.encrypt(bytes(form.data['username'], 'utf-8'))
            emailId = f.encrypt(bytes(form.data['email'], 'utf-8'))
            passwordHash = f.encrypt(bytes(form.data['password'], 'utf-8'))
            otpEncrypt = f.encrypt(bytes(dataOtp, 'utf-8'))
            

            return redirect(url_for('users.otpVerify', ZOBmsZfI=userName, kOmpgatI=emailId, sDxPebsj=passwordHash, AXrBhKqy=otpEncrypt))

    return render_template('register.html', form=form)


#Otp Verification View
@users.route('/verifyOtp/<ZOBmsZfI>`<kOmpgatI>`<sDxPebsj>`<AXrBhKqy>', methods=['GET', 'POST'])
def otpVerify(ZOBmsZfI,kOmpgatI,sDxPebsj,AXrBhKqy):

    otpForm = otpVerification()

    if otpForm.validate_on_submit():
        
        with open('key.txt', 'rb') as safeKey:
            key = safeKey.read()

        key = str(key, 'utf-8')
        f = Fernet(key)

        username = f.decrypt(bytes(ZOBmsZfI, 'utf-8'))
        email = f.decrypt(bytes(kOmpgatI, 'utf-8'))
        password = f.decrypt(bytes(sDxPebsj, 'utf-8'))
        otp = f.decrypt(bytes(AXrBhKqy, 'utf-8'))

        usernameU = str(username, 'utf-8')
        emailU = str(email, 'utf-8')
        passwordU = str(password, 'utf-8')
        otp = str(otp, 'utf-8')

        if otp == str(otpForm.otpData.data):
            newUser = User(username=usernameU, email=emailU, password=passwordU)
            db.session.add(newUser)
            db.session.commit()

            return redirect (url_for('errorPages.success'))
        else:
            return redirect(url_for('errorPages.wrongOtp'))

    return render_template('verifyOtp.html', otpForm=otpForm)


@users.route('/changeDetails', methods=['GET', 'POST'])
@login_required
def changeDetails():

    updatePictureForm = updateProfilePicForm()
    passwordChange = updatePasswordForm()

    if updatePictureForm.validate_on_submit():
        if updatePictureForm.picture.data:
            pic = addProfilePic(updatePictureForm.picture.data)
            current_user.profileImage = pic
            db.session.commit()
            return redirect(url_for('users.account'))

    if passwordChange.validate_on_submit():
        username = current_user.username
        current = User.query.filter_by(username=username).first()
        current.passwordHashed = generate_password_hash(passwordChange.password.data)
        db.session.commit()
        return redirect(url_for('core.home'))
        
    return render_template('changeAccountDetails.html', updatePictureForm=updatePictureForm, passwordChange=passwordChange)


@users.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():

    passwordForm = forgotPasswordForm()

    if passwordForm.validate_on_submit():
        isUser = User.query.filter_by(email=passwordForm.email.data).first()
        if isUser is None:
            return redirect(url_for('users.registerUser'))

        else:
            token = forgotPass.dumps(passwordForm.email.data, salt=isUser.username)
            resetLink.linkGenerator(passwordForm.email.data,isUser.username, token)
            return redirect(url_for('users.loginUser'))

    return render_template('forgotPassword.html', passwordForm=passwordForm)

from todoApp import forgotPass
from todoApp.users.resetLinkHandler import resetLink
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

@users.route('/forgotPassword/<email>/<token>/<username>', methods=['GET', 'POST'])
def newPassword (email, token, username):
    try:
        checkValidity = forgotPass.loads(token, salt=username, max_age=120)
        newPass = resetPasswordForm()
        if newPass.validate_on_submit():
            userPassword = User.query.filter_by(username=username).first()
            userPassword.passwordHashed = generate_password_hash(newPass.password.data)
            db.session.commit()
            return redirect(url_for('users.loginUser'))
            
        return render_template('newPassword.html', newPass=newPass, email=email)

    except SignatureExpired:
        return render_template('linkExpired.html')
