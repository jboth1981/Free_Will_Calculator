from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '19f246287731d7bca4ce6823e42b0685'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:zkzKtwNm8BWOdDqJKkQG@database-1.cnbsxgnwlqln.us-east-1.rds.amazonaws.com:3306/FREE_WILL_DB'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes