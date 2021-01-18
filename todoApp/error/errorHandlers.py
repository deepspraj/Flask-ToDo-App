from flask import Blueprint, render_template




errorPages = Blueprint('errorPages', __name__)


@errorPages.app_errorhandler(404)
def pageNotFound(e):
    
    return render_template('404.html'), 404