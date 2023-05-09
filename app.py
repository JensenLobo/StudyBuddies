from flask import Flask, render_template, request, redirect, url_for, session, flash
#from your_database_module import db, User
from werkzeug.security import generate_password_hash
from src.models import db, users, compsci
from src.repositories.user_repository import account_repository_singleton
from src.security import bcrypt
from dotenv import load_dotenv
import os
import functools
load_dotenv()
app = Flask(__name__)

#  DB connection
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = \
      f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('KEY')
db.init_app(app)
bcrypt.init_app(app)

def authentication(fun):
  @functools.wraps(fun)
  def wrapper(*args,**kwargs):
       if 'user_id' in session:
           return fun(*args,**kwargs)
       
       return redirect(url_for('index'))
  return wrapper

def hash_password(password):
    return generate_password_hash(password)

@app.route('/')
def index():
    return render_template('about.html')


@app.get('/profileIndex')
@authentication
def profileIndex():
    user = account_repository_singleton.getUser(session['user_id'])
    return render_template('profileIndex.html', user=user)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

         # Check if the username is already in use
        if not username or not password:
         return render_template('login.html', error= "Invalid username or password")
        existing_user = users.query.filter_by(username=username).first()
        if not existing_user:
            return render_template('/login.html', error = "Invalid Username")
        if not bcrypt.check_password_hash(existing_user.password_hash, password):
            return render_template('/login.html', error = "Wrong password")
       # user = account_repository_singleton.getUser(existing_user.id)

       
        session['user_id'] = existing_user.id
        return redirect('/profileIndex')

    else:
        return render_template('login.html')

@app.get('/signup')
def signup():
    return render_template('signup.html')


@app.post('/signup')
def create_account():
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

       # return render_template('login.html')
       # Check if the passwords match
        if password != confirm_password:
         return render_template('signup.html', error='Passwords do not match')
        if username.lower().startswith('@uncc.edu'):
            return render_template('signup.html', error='Username should not start with "@uncc.edu"')
    # Check if the username ends with "@uncc.edu"
        if not username.lower().endswith('@uncc.edu'):
          return render_template('signup.html', error='Signup with UNCC credentials"')
         # Validate the password (for example, you might require a certain length or complexity)
        if len(password) < 8:
            return render_template('signup.html', error='Password should be at least 8 characters long')
        hashed_password = bcrypt.generate_password_hash(password).decode()
        result = account_repository_singleton.create_account(username.lower(), hashed_password)
        if result == False:
            return render_template('signup.html', error='Username is already in use')

        return redirect(url_for('getProfile', user_id = result))


        

@app.get("/profile")
def getProfile():
    return render_template("creatingProfile.html")

@app.post("/profile")
def settingProfile():
   user_major = request.form.get('major')
   user_id = request.form.get('user_id')
   first_name = request.form.get('first_name')
   last_name = request.form.get('last_name')
   account_repository_singleton.updatingMajor(user_id, user_major, first_name, last_name)
#    return redirect("/")
   return redirect("/profileIndex")
   

@app.route('/major')
def major():
    return render_template('major.html')


# Genreal page for all users to see
@app.route('/general')
def general():
    return render_template('general.html')

@app.get('/ComputerScience')
@authentication
def compSci():
     user = account_repository_singleton.getUser(session['user_id'])
     post = account_repository_singleton.get_posts()
     return render_template('compSci_Forum.html',user=user, forums=post)
 

@app.post('/ComputerScience')
def display():
    
    message = request.form.get('question-input')
    # print(message) testing if message is holding the text input
    username=session['user_id']
    user = account_repository_singleton.get_user_id(username)
    account_repository_singleton.add_post(message,user.first_name,user.username)
    return redirect('/ComputerScience')

@app.get('/like/<id>')
def likepost(id):
    post = account_repository_singleton.getpost(id)
    print(post.likelist)
    if session['user_id'] not in post.likelist:
      post.likelist.append(session['user_id'])
      post.message_likes += 1
      db.session.commit()
    return redirect('/ComputerScience')

@app.get('/dislike/<id>')
def dislikepost(id):
    post = account_repository_singleton.getpost(id)
    if session['user_id'] not in post.dislikelist:
      post.dislikelist.append(session['user_id'])
      post.message_dislikes += 1
      db.session.commit()
    
    return redirect('/ComputerScience')

@app.route('/business_Forum', methods=['GET', 'POST'])
@authentication
def business_forum():
    user = account_repository_singleton.getUser(session['user_id'])
    if request.method == 'POST':
        message = request.form['question-input']
        account_repository_singleton.add_post(message)
        return redirect(url_for('business_forum', user=user))
    else:
        posts = set(account_repository_singleton.get_posts())
    return render_template('business_Forum.html', posts=posts)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    message = request.form.get('question-input')
    account_repository_singleton.add_post(message)
    return redirect(url_for('business_forum'))
@app.get('/logout')
def logout():
    del session['user_id']
    return redirect('/')

@app.get('/groups')
def groups():
    #user_id = request.form.get('user_id')
  
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    user_major = account_repository_singleton.getMajor(user_id)
    print(user_major)
    if user_major == 'Computer Science':
        return redirect('/ComputerScience')
    #elif user_major == 'Biology':
        return redirect('/general')
    #elif user_major == 'Engineering':
        return render_template('hist_groups.html')
    elif user_major == 'Business':
        return redirect('/business_Forum')
    else:
        # Handle unknown major or no major
        return redirect('/general')
  
@app.route('/deleteaccount', methods=['POST'])
def delete_account():
    account = users.query.get(session['user_id'])
    useremail = account.username
    print(useremail)
    if account.major == "Computer Science":
        user = compsci.query.filter_by(useremail=useremail).all()
        for u in user:
         db.session.delete(u)
       
    db.session.delete(account)
    db.session.commit()
    session.pop('user_id')
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update_post(id):
    account = users.query.get(session['user_id'])
    post = account_repository_singleton.get_comp_id(id)
    #post = compsci.query.get(post_id)
    if post is not None and post.useremail == account.username:
        forum_message = request.form.get('question-input')
        post.forum_message = forum_message
        db.session.commit()
        return redirect('/ComputerScience')
    return redirect('/')

    

    
