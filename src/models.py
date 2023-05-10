from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    major = db.Column(db.String(255), default="No major", nullable=True)
    first_name = db.Column(db.String(255), default="No first", nullable=True)
    last_name = db.Column(db.String(255), default="No last", nullable=True)


    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = (password_hash)
        self.major = "No major"


    def __repr__(self):
        return self
    
    def user_info(self) -> str:
        return f'<Account ID: {self.id}, Username: {self.username}'

class compsci(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    useremail = db.Column(db.String(255), nullable=False)
    forum_message = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, forum_message,username,useremail):
        self.username = username
        self.useremail = useremail
        self.forum_message = forum_message

    def get_id(self):
        return self.post_id        

    def __repr__(self):
        return self
   
    def post_info(self) -> str:
        return f'Post ID: {self.post_id}, Post Statement: {self.forum_message}'
    
    def set_likes(self, likes):
        self.likes = likes

    def set_dislike(self, dislike):
        self.dislikes = dislike

    def set_can_edit(self, can_edit):
        self.can_edit = can_edit

class post_likes_compsci(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, post_id, rating):
        self.user_id = user_id
        self.post_id = post_id
        self.rating = rating

