from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = (password_hash)


    def __repr__(self):
        return self
    
    def user_info(self) -> str:
        return f'<Account ID: {self.id}, Username: {self.username}'



