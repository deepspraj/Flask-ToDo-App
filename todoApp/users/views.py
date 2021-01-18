from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import logout_user, login_required, current_user, login_user
from todoApp.users.forms import loginUserForm, registerUserForm
from todoApp.models import User
from todoApp import db
from todoApp.core.views import core

users = Blueprint('users', __name__)


#account
@users.route('/account')
@login_required
def account():

    return render_template('account.html', current_user=current_user)


#logout
@users.route('/logout')
@login_required
def logoutUser():

    logout_user()
    
    return redirect(url_for('core.home'))

#login
@users.route('/login', methods=['GET','POST'])
def loginUser():

    form = loginUserForm()

    if form.validate_on_submit():

        logUser = User.query.filter_by(username= form.username.data).first()

        if logUser.checkPassword(password=form.password.data) and logUser is not None:
            login_user(logUser)

            flash("User successfully logged in..!!")

            return redirect('account')

    return render_template('login.html', form=form)



#Register
@users.route('/register', methods=['GET', 'POST'])
def registerUser():

    form = registerUserForm()

    if form.validate_on_submit():

        newUser = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(newUser)
        db.session.commit()

        return redirect('login')

    return render_template('register.html', form=form)





