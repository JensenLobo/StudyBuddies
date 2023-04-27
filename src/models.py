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

class compsci_forum(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    forum_message = db.Column(db.String(255), nullable=False)
    message_likes = db.Column(db.Integer, nullable=True)
    major_id = db.Column(db.String(255), nullable=True)


    def __init__(self, forum_message):
        self.forum_message = forum_message


    def __repr__(self):
        return self
   
    def post_info(self) -> str:
        return f'Post ID: {self.post_id}, Post Statement: {self.forum_message}'
