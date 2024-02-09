from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user

#from flask_login import LoginManager, UserMixin, login_url

app = Flask(__name__)

app.config['SECRET_KEY'] = '7a4103576382a48d81e258d2e37f8ecd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase.db'  # recherche du SGBD et de la BD

db = SQLAlchemy(app)
migrate =Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import routes
