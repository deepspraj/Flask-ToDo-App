import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)


app.config['SECRET_KEY'] = 'deepspraj'


baseDirectory = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDirectory, 'todobase.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

forgotPass = URLSafeTimedSerializer(app.config['SECRET_KEY'])

db = SQLAlchemy(app)

Migrate(app, db)

###########################
#### LOGIN CONFIGS #######
#########################

login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.loginUser"


from todoApp.tasks.views import task
from todoApp.users.views import users
from todoApp.error.errorHandlers import errorPages
from todoApp.core.views import core

app.register_blueprint(core)
app.register_blueprint(errorPages)
app.register_blueprint(task)
app.register_blueprint(users)
