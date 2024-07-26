from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import timedelta



uploadFolder = "C:\\Users\\Ravi Singh\\OneDrive\\Desktop\\flask-Blog\\flask_blog\\static\\media"
profileUpload = "C:\\Users\\Ravi Singh\\OneDrive\\Desktop\\flask-Blog\\flask_blog\\static\\profile"

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config["UPLOAD_FOLDER"] = uploadFolder
app.config["PROFILE_UPLOAD_FOLDER"] = profileUpload
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///MyBlog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days= 1)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "loginBLog"
login_manager.login_message_category = "info"



def create_app():
    from flask_blog import routes, model

    @app.before_request
    def make_session_permanent():
        session.permanent = True
    with app.app_context():
        db.create_all()
    
   
    return app