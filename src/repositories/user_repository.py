
from flask import Flask, render_template, request, redirect, url_for, session
#from your_database_module import db, User
from werkzeug.security import generate_password_hash
from src.models import db, users, compsci


class AccountRepository:
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
   def add_post(self, forum_message, username):
      post = compsci(forum_message, username)
      db.session.add(post)
      db.session.commit()
      return post.post_id
   
   def get_comp_id():
         return compsci.post_id

   def get_posts(self):
      posts =  compsci.query.all()
      return posts

   def __init__(self):
      self.accounts = []
      self.posts = []
  
   def getpost(self,id):
      user = compsci.query.filter_by(post_id=id).first()
      return user
   #def add_post(self, post):
    #  self.posts.append(post)
    #  print(self.posts)







account_repository_singleton = AccountRepository()