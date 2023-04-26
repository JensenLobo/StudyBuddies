
from flask import Flask, render_template, request, redirect, url_for, session
#from your_database_module import db, User
from werkzeug.security import generate_password_hash
from src.models import db, users, compsci_forum


class AccountRepository:
   def updatingMajor(self, user_id, major, first_name, last_name):
      users.query.filter_by(id = user_id).update(dict(major=major, first_name=first_name, last_name=last_name))
      db.session.commit()
      
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

   

   def get_user_id():
         return users.id
   
   def add_post(self, forum_message):
      post = compsci_forum(forum_message)
      db.session.add(post)
      db.session.commit()
      return post.post_id
   
   def get_comp_id():
         return compsci_forum.post_id

   def get_posts(self):
      return self.posts

   def __init__(self):
      self.accounts = []
      self.posts = []

   def add_post(self, post):
      self.posts.append(post)
      print(self.posts)







account_repository_singleton = AccountRepository()