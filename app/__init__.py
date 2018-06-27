from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from .momentjs import momentjs
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager




app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.session_protection = "strong"
login.login_view = 'login'
bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)


# app.jinja_env.globals['momentjs'] = momentjs




from app import routes,models
