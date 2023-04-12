
from flask import Flask, render_template, request, redirect, url_for, session
#from your_database_module import db, User
from werkzeug.security import generate_password_hash
from src.models import db, users


class AccountRepository:
 def create_account(self, username, password_hash):


    


    # Check if the username is already in use
    existing_user = users.query.filter_by(username=username).first()
    if existing_user != None:
       return render_template('signup.html', error='Username is already in use')

   
    # Save the user in the database
    print(username, password_hash)

    user = users(username, password_hash)
    db.session.add(user)
    db.session.commit()

    # Set the session and redirect to the home page
    session['username'] = username
    return render_template('login.html')
 

#  def get_user_id():
#         return users.id


 









account_repository_singleton = AccountRepository()