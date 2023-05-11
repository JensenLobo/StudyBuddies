from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# This is the model for the users table in the database.
class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    major = db.Column(db.String(255), default="No major", nullable=True)
    first_name = db.Column(db.String(255), default="No first", nullable=True)
    last_name = db.Column(db.String(255), default="No last", nullable=True)
    major_changed_count = db.Column(db.Integer, default=0)

    # This is the constructor for the users model.
    def __init__(self, username, password_hash, major='No major', first_name='No first', last_name='No last', major_changed_count=0):
        self.username = username
        self.password_hash = (password_hash)
        self.major = major
        self.first_name = first_name
        self.last_name = last_name
        self.major_changed_count = major_changed_count

    # This function is used to get the id of the user.
    def __repr__(self):
        return self
    
    # This function is used to get the id of the user.
    def user_info(self) -> str:
        return f'<Account ID: {self.id}, Username: {self.username}'

# This is the model for the posts table in the database.
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

# This is the model for the post_likes table in the database.
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

# This is the model for the posts table in the database.
class biology(db.Model):
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

# This is the model for the post_likes table in the database.
class post_likes_biology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, post_id, rating):
        self.user_id = user_id
        self.post_id = post_id
        self.rating = rating


# This is the model for the posts table in the database.
class business(db.Model):
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

# This is the model for the post_likes table in the database.
class post_likes_business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, post_id, rating):
        self.user_id = user_id
        self.post_id = post_id
        self.rating = rating


# This is the model for the posts table in the database.
class engineering(db.Model):
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

# This is the model for the post_likes table in the database.
class post_likes_engineer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, post_id, rating):
        self.user_id = user_id
        self.post_id = post_id
        self.rating = rating


# This is the model for the posts table in the database.
class generalform(db.Model):
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

# This is the model for the post_likes table in the database.
class post_likes_general(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, post_id, rating):
        self.user_id = user_id
        self.post_id = post_id
        self.rating = rating

