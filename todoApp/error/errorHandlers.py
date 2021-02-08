from flask import Blueprint, render_template


errorPages = Blueprint('errorPages', __name__)


@errorPages.app_errorhandler(404)
def pageNotFound(e):
    
    return render_template('404.html'), 404



@errorPages.route('/wrongOtp')
def wrongOtp():

    return render_template('wrongOtp.html')


@errorPages.route('/error')
def errorInUser():

    return render_template('error.html')



@errorPages.route('/success')
def success():

    return render_template('success.html')