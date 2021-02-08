from flask import Blueprint, render_template,url_for, redirect
from flask_login import current_user

core = Blueprint('core', __name__)

@core.route('/')
def home():

    return render_template('home.html')


@core.route('/about')
def about():
    
    return render_template('about.html')


