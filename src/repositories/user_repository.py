from flask import Flask, render_template, request, redirect, url_for, session
#from your_database_module import db, User
from src.models import db, users, compsci, post_likes_compsci,biology,post_likes_biology,business,post_likes_business, engineering, post_likes_engineer, generalform, post_likes_general

class AccountRepository:
   def __init__(self):
      self.accounts = []
      self.posts = []

   def updatingMajor(self, user_id, major, first_name, last_name):
      users.query.filter_by(id = user_id).update(dict(major=major, first_name=first_name, last_name=last_name))
      db.session.commit()
   
   def getMajor(self, user_id):
    if user_id:
        user = users.query.filter_by(id=user_id).first()
        if user:
            return user.major
    return None
   def getUser(self, user_id):
    user = users.query.filter_by(id=user_id).first()
    return user

   def create_account(self, username, password_hash):
      # Check if the username is already in use
      existing_user = users.query.filter_by(username=username).first()
      if existing_user != None:
         return False
      # Save the user in the database
      user = users(username, password_hash)
      db.session.add(user)
      db.session.commit()
      # Set the session and redirect to the home page
      session['username'] = username
      return user.id

   def get_user_id(self, id):
      user = users.query.filter_by(id=id).first()
      return user
   
   def add_post(self, forum_message, username,user):
      post = compsci(forum_message, username,user)
      db.session.add(post)
      db.session.commit()
      return post.post_id
   
   def get_comp_id(self, post_id):
         user = compsci.query.filter_by(post_id=post_id).first()
         return user

   def get_posts(self):
      posts =  compsci.query.order_by(compsci.created_at.asc()).all()
      return posts

   def add_rating(self, user_id, post_id, rating):
      print("esetsef1", user_id, post_id, rating)

      previous_rating = post_likes_compsci.query.filter_by(user_id=user_id, post_id=post_id).first()
      if previous_rating == None:
         rating = post_likes_compsci(user_id, post_id, rating)
         db.session.add(rating)
         db.session.commit()
         return True

      print("esetsef", previous_rating.rating, rating)
      if previous_rating.rating == rating:
         return False

      # delete the old rating
      post_likes_compsci.query.filter_by(user_id=user_id, post_id=post_id).update(dict(rating=rating))
      db.session.commit()
      return True

   def count_rating(self, post_id, rating):
      count = post_likes_compsci.query.filter_by(post_id=post_id, rating=rating).count()
      if count is None:
         return 0
      return count
   # def remove_likes
   def get_postsbio(self):
      posts =  biology.query.order_by(biology.created_at.asc()).all()
      return posts
  
   def count_ratingbio(self, post_id, rating):
      count = post_likes_biology.query.filter_by(post_id=post_id, rating=rating).count()
      if count is None:
         return 0
      return count
   def add_postbio(self, forum_message, username,user):
      post = biology(forum_message, username,user)
      db.session.add(post)
      db.session.commit()
      return post.post_id
   
   def add_ratingbio(self, user_id, post_id, rating):
      print("esetsef1", user_id, post_id, rating)
      previous_rating = post_likes_biology.query.filter_by(user_id=user_id, post_id=post_id).first()
      if previous_rating == None:
         rating = post_likes_biology(user_id, post_id, rating)
         db.session.add(rating)
         db.session.commit()
         return True

      print("esetsef", previous_rating.rating, rating)
      if previous_rating.rating == rating:
         return False

      # delete the old rating
      post_likes_biology.query.filter_by(user_id=user_id, post_id=post_id).update(dict(rating=rating))
      db.session.commit()
      return True

   
   def get_comp_idbio(self, post_id):
         user = biology.query.filter_by(post_id=post_id).first()
         return user
   
   def get_postsbus(self):
      posts =  business.query.order_by(business.created_at.asc()).all()
      return posts
   
   def count_ratingbus(self, post_id, rating):
      count = post_likes_business.query.filter_by(post_id=post_id, rating=rating).count()
      if count is None:
         return 0
      return count
   
   def add_postbus(self, forum_message, username,user):
      post = business(forum_message, username,user)
      db.session.add(post)
      db.session.commit()
      return post.post_id
   
   def get_comp_idbus(self, post_id):
         user = business.query.filter_by(post_id=post_id).first()
         return user
   
   def add_ratingbus(self, user_id, post_id, rating):
      print("esetsef1", user_id, post_id, rating)
      previous_rating = post_likes_business.query.filter_by(user_id=user_id, post_id=post_id).first()
      if previous_rating == None:
         rating = post_likes_business(user_id, post_id, rating)
         db.session.add(rating)
         db.session.commit()
         return True

      print("esetsef", previous_rating.rating, rating)
      if previous_rating.rating == rating:
         return False

      # delete the old rating
      post_likes_business.query.filter_by(user_id=user_id, post_id=post_id).update(dict(rating=rating))
      db.session.commit()
      return True
   
   def get_postseng(self):
      posts =  engineering.query.order_by(engineering.created_at.asc()).all()
      return posts
   
   def count_ratingeng(self, post_id, rating):
      count = post_likes_engineer.query.filter_by(post_id=post_id, rating=rating).count()
      if count is None:
         return 0
      return count
   
   def add_posteng(self, forum_message, username,user):
      post = engineering(forum_message, username,user)
      db.session.add(post)
      db.session.commit()
      return post.post_id
   
   
   def get_comp_ideng(self, post_id):
         user = engineering.query.filter_by(post_id=post_id).first()
         return user
   
   def add_ratingeng(self, user_id, post_id, rating):
      print("esetsef1", user_id, post_id, rating)
      previous_rating = post_likes_engineer.query.filter_by(user_id=user_id, post_id=post_id).first()
      if previous_rating == None:
         rating = post_likes_engineer(user_id, post_id, rating)
         db.session.add(rating)
         db.session.commit()
         return True

      print("esetsef", previous_rating.rating, rating)
      if previous_rating.rating == rating:
         return False

      # delete the old rating
      post_likes_engineer.query.filter_by(user_id=user_id, post_id=post_id).update(dict(rating=rating))
      db.session.commit()
      return True
   
   def get_postsgen(self):
      posts =  generalform.query.order_by(generalform.created_at.asc()).all()
      return posts
   

   def count_ratinggen(self, post_id, rating):
      count = post_likes_general.query.filter_by(post_id=post_id, rating=rating).count()
      if count is None:
         return 0
      return count
   

   def add_postgen(self, forum_message, username,user):
      post = generalform(forum_message, username,user)
      db.session.add(post)
      db.session.commit()
      return post.post_id
   

   def get_comp_idgen(self, post_id):
         user = generalform.query.filter_by(post_id=post_id).first()
         return user
   

   def add_ratinggen(self, user_id, post_id, rating):
      print("esetsef1", user_id, post_id, rating)
      previous_rating = post_likes_general.query.filter_by(user_id=user_id, post_id=post_id).first()
      if previous_rating == None:
         rating = post_likes_general(user_id, post_id, rating)
         db.session.add(rating)
         db.session.commit()
         return True

      print("esetsef", previous_rating.rating, rating)
      if previous_rating.rating == rating:
         return False

      # delete the old rating
      post_likes_general.query.filter_by(user_id=user_id, post_id=post_id).update(dict(rating=rating))
      db.session.commit()
      return True
   


   
account_repository_singleton = AccountRepository()