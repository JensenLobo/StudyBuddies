from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

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
    forum_message = db.Column(db.String(255), nullable=False)
    message_likes = db.Column(db.Integer, nullable=True)
    message_dislikes = db.Column(db.Integer, nullable=True)
    dislikelist = db.Column(db.ARRAY(db.Integer), nullable=True, default=[])
    likelist = db.Column(db.ARRAY(db.Integer), nullable=True, default=[])


    def __init__(self, forum_message,username):
        self.username = username
        self.forum_message = forum_message
        self.message_likes = 0
        self.message_dislikes = 0

    def __repr__(self):
        return self
   
    def post_info(self) -> str:
        return f'Post ID: {self.post_id}, Post Statement: {self.forum_message}'
