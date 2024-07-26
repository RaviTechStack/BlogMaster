from datetime import datetime
from flask_blog import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer(), unique=True, nullable=False)
    profile_pic = db.Column(db.String(120), nullable=False, default='default_profile.jpg')
    cover_pic = db.Column(db.String(120), nullable=False, default='default_cover.jpg')
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    blogs = db.relationship("Blog", backref = "author", lazy= True)
    def _repr_(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    

class Blog(db.Model):
    blog_id = db.Column(db.Integer, primary_key= True)
    blog_title = db.Column(db.String(200), nullable= False )
    blog_content = db.Column(db.String(2000), nullable= False )
    blog_img = db.Column(db.String(200), nullable= False )
    blog_highlights = db.Column(db.String(500), nullable= True )
    blog_category = db.Column(db.String(50), nullable= True )
    blog_user = db.Column(db.Integer, db.ForeignKey("user.id"), nullable= False)

    def __repr__(self):
        return f"{self.blog_title} and {self.blog_img}"