from flask import Flask, render_template, request, redirect, url_for, session, flash
#from your_database_module import db, User
from src.models import db, users, compsci, post_likes_compsci, biology, post_likes_biology, business, post_likes_business, engineering, post_likes_engineer, generalform, post_likes_general
from src.repositories.user_repository import account_repository_singleton
from src.security import bcrypt
from dotenv import load_dotenv
import datetime
import os
import functools
load_dotenv()
app = Flask(__name__)

#  DB connection
#db_user = os.getenv('DB_USER')
#db_pass = os.getenv('DB_PASS')
#db_host = os.getenv('DB_HOST')
#db_port = os.getenv('DB_PORT')
#db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
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

@app.route('/')
def index():
    if session.get('user_id') and request.path != "/logout":
        return redirect('/profileIndex')
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
        user = existing_user.id
        if existing_user.major == 'No major':
            session['user_id'] = existing_user.id
            return redirect(url_for('getProfile', user_id=user))
        
        session['user_id'] = existing_user.id
        flash("You have logged in successfully.")
        return redirect('/profileIndex')
    if session.get('user_id') and request.path == '/login':
        flash("You're already logged in.")
        return redirect('/profileIndex')   
    else:
        return render_template('login.html')
    
@app.get('/signup')
def signup():
    if session.get('user_id'):
        # User is already logged in, redirect to profile page
        return redirect('/profileIndex')
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
        flash("Successfully Created The Account.")
        return redirect('/')

@app.get("/profile")
@authentication
def getProfile():
        user = account_repository_singleton.getUser(session['user_id'])
        if users.query.filter_by(id=user.id).first().major_changed_count >= 2:
            flash("You already changed your major twice.", category="error")
            return redirect("/profileIndex")
        return render_template("creatingProfile.html", user=user)
    
@app.post("/profile")
@authentication
def settingProfile():
   user = account_repository_singleton.getUser(session['user_id'])
   user_major = request.form.get('major')
   user_id = request.form.get('user_id')
   first_name = request.form.get('first_name')
   last_name = request.form.get('last_name')
   account_repository_singleton.updatingMajor(user_id, user_major, first_name, last_name)
   users.query.filter_by(id=user.id).first().major_changed_count += 1
   db.session.commit()
#    return redirect("/")
   flash("Successfully changed major.")
   return redirect("/profileIndex")
   
@app.template_filter('datetimeformat')
def datetimeformat(value, format="%Y-%m-%d %H:%M:%S"):
    return value.strftime(format)

@app.get('/ComputerScience')
@authentication
def compSci():
     user = account_repository_singleton.getUser(session['user_id'])
     post = account_repository_singleton.get_posts()
     for item in post:
         post_id = item.get_id()
         item.set_likes(account_repository_singleton.count_rating(post_id, "like"))
         item.set_dislike(account_repository_singleton.count_rating(post_id, "dislike"))
         can_edit = item.useremail == user.username
         item.set_can_edit(can_edit)

     return render_template('compSci_Forum.html',user=user, forums=post)
 
@app.post('/ComputerScience')
@authentication
def display():
    message = request.form.get('question-input')
    # print(message) testing if message is holding the text input
    username=session['user_id']
    user = account_repository_singleton.get_user_id(username)
    account_repository_singleton.add_post(message,user.first_name,user.username)
    return redirect('/ComputerScience')

@app.get('/like/<id>')
@authentication
def likepost(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_id(id).get_id()
    account_repository_singleton.add_rating(user_id, post_id, "like")
    return redirect('/ComputerScience')

@app.get('/dislike/<id>')
@authentication
def dislikepost(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_id(id).get_id()
    account_repository_singleton.add_rating(user_id, post_id, "dislike")
    return redirect('/ComputerScience')

@app.get('/biology')
@authentication
def biologyy():
     user = account_repository_singleton.getUser(session['user_id'])
     post = account_repository_singleton.get_postsbio()
     for item in post:
         post_id = item.get_id()
         item.set_likes(account_repository_singleton.count_ratingbio(post_id, "like"))
         item.set_dislike(account_repository_singleton.count_ratingbio(post_id, "dislike"))
         can_edit = item.useremail == user.username
         item.set_can_edit(can_edit)
     return render_template('biology_Form.html',user=user, forums=post)

@app.post('/biology')
@authentication
def displaybio():
    message = request.form.get('question-input')
    # print(message) testing if message is holding the text input
    username=session['user_id']
    user = account_repository_singleton.get_user_id(username)
    account_repository_singleton.add_postbio(message,user.first_name,user.username)
    return redirect('/biology')

@app.get('/likebio/<id>')
@authentication
def likepostbio(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_idbio(id).get_id()
    account_repository_singleton.add_ratingbio(user_id, post_id, "like")
    return redirect('/biology')

@app.get('/dislikebio/<id>')
@authentication
def dislikepostbio(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_idbio(id).get_id()
    account_repository_singleton.add_ratingbio(user_id, post_id, "dislike")
    return redirect('/biology')

@app.get('/business')
@authentication
def busness():
     user = account_repository_singleton.getUser(session['user_id'])
     post = account_repository_singleton.get_postsbus()
     for item in post:
         post_id = item.get_id()
         item.set_likes(account_repository_singleton.count_ratingbus(post_id, "like"))
         item.set_dislike(account_repository_singleton.count_ratingbus(post_id, "dislike"))
         can_edit = item.useremail == user.username
         item.set_can_edit(can_edit)
     return render_template('business_Forum.html',user=user, forums=post)

@app.post('/business')
@authentication
def displaybus():
    message = request.form.get('question-input')
    # print(message) testing if message is holding the text input
    username=session['user_id']
    user = account_repository_singleton.get_user_id(username)
    account_repository_singleton.add_postbus(message,user.first_name,user.username)
    return redirect('/business')

@app.get('/likebus/<id>')
@authentication
def likepostbus(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_idbus(id).get_id()
    account_repository_singleton.add_ratingbus(user_id, post_id, "like")
    return redirect('/business')

@app.get('/dislikebus/<id>')
@authentication
def dislikepostbus(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_idbus(id).get_id()
    account_repository_singleton.add_ratingbus(user_id, post_id, "dislike")
    return redirect('/business')

@app.get('/engineer')
@authentication
def engineer():
     user = account_repository_singleton.getUser(session['user_id'])
     post = account_repository_singleton.get_postseng()
     for item in post:
         post_id = item.get_id()
         item.set_likes(account_repository_singleton.count_ratingeng(post_id, "like"))
         item.set_dislike(account_repository_singleton.count_ratingeng(post_id, "dislike"))
         can_edit = item.useremail == user.username
         item.set_can_edit(can_edit)
     return render_template('engineering_forum.html',user=user, forums=post)

@app.post('/engineer')
@authentication
def displayeng():
    message = request.form.get('question-input')
    # print(message) testing if message is holding the text input
    username=session['user_id']
    user = account_repository_singleton.get_user_id(username)
    account_repository_singleton.add_posteng(message,user.first_name,user.username)
    return redirect('/engineer')

@app.get('/likeeng/<id>')
@authentication
def likeposteng(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_ideng(id).get_id()
    account_repository_singleton.add_ratingeng(user_id, post_id, "like")
    return redirect('/engineer')

@app.get('/dislikeeng/<id>')
@authentication
def dislikeposteng(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_ideng(id).get_id()
    account_repository_singleton.add_ratingeng(user_id, post_id, "dislike")
    return redirect('/engineer')

@app.get('/general')
@authentication
def general():
     user = account_repository_singleton.getUser(session['user_id'])
     post = account_repository_singleton.get_postsgen()
     for item in post:
         post_id = item.get_id()
         item.set_likes(account_repository_singleton.count_ratinggen(post_id, "like"))
         item.set_dislike(account_repository_singleton.count_ratinggen(post_id, "dislike"))
         can_edit = item.useremail == user.username
         item.set_can_edit(can_edit)
     return render_template('general.html',user=user, forums=post)

@app.post('/general')
@authentication
def displaygen():
    message = request.form.get('question-input')
    # print(message) testing if message is holding the text input
    username=session['user_id']
    user = account_repository_singleton.get_user_id(username)
    account_repository_singleton.add_postgen(message,user.first_name,user.username)
    return redirect('/general')

@app.get('/likegen/<id>')
@authentication
def likepostgen(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_idgen(id).get_id()
    account_repository_singleton.add_ratinggen(user_id, post_id, "like")
    return redirect('/general')

@app.get('/dislikegen/<id>')
@authentication
def dislikepostgen(id):
    user_id = session['user_id']
    post_id = account_repository_singleton.get_comp_idgen(id).get_id()
    account_repository_singleton.add_ratinggen(user_id, post_id, "dislike")
    return redirect('/general')

@app.get('/logout')
def logout():
    try:
        del session['user_id']
        flash("Successfully logged out.")
    except KeyError:
        flash("You need to be logged in", category="error")

    return redirect('/')

@app.get('/groups')
def groups():
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    user_major = account_repository_singleton.getMajor(user_id)
    print(user_major)
    if user_major == 'Computer Science':
        return redirect('/ComputerScience')
    elif user_major == 'Biology':
        return redirect('/biology')
    elif user_major == 'Engineering':
        return redirect('/engineer')
    elif user_major == 'Business':
        return redirect('/business')
    else:
        # Handle unknown major or no major
        return redirect('/profileIndex')
  
@app.route('/deleteaccount', methods=['POST'])
def delete_account():
    account = users.query.get(session['user_id'])
    useremail = account.username
    user_id = account.id
    posts = generalform.query.filter_by(useremail=useremail).all()
    for post in posts:
         post_rating = post_likes_general.query.filter_by(user_id=user_id).all()
         other_post_rating = post_likes_general.query.filter_by(post_id=post.post_id).all()
         for rating in post_rating:
             db.session.delete(rating)
             db.session.commit()
         for rating in other_post_rating:
             db.session.delete(rating)
             db.session.commit()
         db.session.delete(post)
         db.session.commit() 

    if account.major == "Computer Science":
        posts = compsci.query.filter_by(useremail=useremail).all()
        for post in posts:
         post_rating = post_likes_compsci.query.filter_by(user_id=user_id).all()
         other_post_rating = post_likes_compsci.query.filter_by(post_id=post.post_id).all()
         for rating in other_post_rating:
             db.session.delete(rating)
             db.session.commit()
         for rating in post_rating:
             db.session.delete(rating)
             db.session.commit()
         db.session.delete(post)
         db.session.commit()
   
    elif account.major == "Biology":
        posts = biology.query.filter_by(useremail=useremail).all()
        for post in posts:
         post_rating = post_likes_biology.query.filter_by(user_id=user_id).all()
         other_post_rating = post_likes_biology.query.filter_by(post_id=post.post_id).all()
         for rating in other_post_rating:
             db.session.delete(rating)
             db.session.commit()
         for rating in post_rating:
             db.session.delete(rating)
             db.session.commit()
         db.session.delete(post)
         db.session.commit()
   
    elif account.major == "Business":
        posts = business.query.filter_by(useremail=useremail).all()
        for post in posts:
         post_rating = post_likes_business.query.filter_by(user_id=user_id).all()
         other_post_rating = post_likes_business.query.filter_by(post_id=post.post_id).all()
         for rating in other_post_rating:
             db.session.delete(rating)
             db.session.commit()
         for rating in post_rating:
             db.session.delete(rating)
             db.session.commit()
         db.session.delete(post)
         db.session.commit()
    
    elif account.major == "Engineering":
        posts = engineering.query.filter_by(useremail=useremail).all()
        for post in posts:
         post_rating = post_likes_engineer.query.filter_by(user_id=user_id).all()
         other_post_rating = post_likes_engineer.query.filter_by(post_id=post.post_id).all()
         for rating in other_post_rating:
             db.session.delete(rating)
             db.session.commit()
         for rating in post_rating:
             db.session.delete(rating)
             db.session.commit()
         db.session.delete(post)
         db.session.commit()
     
    db.session.delete(account)
    db.session.commit()
    session.pop('user_id')
    flash("Successfully deleted the account.")
    return redirect('/')

@app.get('/updated')
def edit_post():
    post_id = request.args.get('id')
    account = users.query.get(session['user_id'])
    post = account_repository_singleton.get_comp_id(post_id)
    if post.useremail == account.username:
        return render_template('editMessage.html', post=post)
    return redirect('/ComputerScience')

@app.route('/update/<int:id>', methods=['POST'])
def update_post(id):
    account = users.query.get(session['user_id'])
    if account.major == "Computer Science":
        post = account_repository_singleton.get_comp_id(id)
    #post = compsci.query.get(post_id)
        if post is not None and post.useremail == account.username:
             forum_message = request.form.get('question-input')
             post.forum_message = forum_message
             db.session.commit()
             return redirect('/ComputerScience')
    elif account.major == "Biology":
        post = account_repository_singleton.get_comp_idbio(id)
        if post is not None and post.useremail == account.username:
             forum_message = request.form.get('question-input')
             post.forum_message = forum_message
             db.session.commit()
             return redirect('/biology')
    elif account.major == "Business":
        post = account_repository_singleton.get_comp_idbus(id)
        if post is not None and post.useremail == account.username:
             forum_message = request.form.get('question-input')
             post.forum_message = forum_message
             db.session.commit()
             return redirect('/business')
    
    elif account.major == "Engineering":
        post = account_repository_singleton.get_comp_ideng(id)
        if post is not None and post.useremail == account.username:
             forum_message = request.form.get('question-input')
             post.forum_message = forum_message
             db.session.commit()
             return redirect('/engineer')
    else:
        return redirect('/profileIndex')

    return redirect('/')

@app.route('/updategen/<int:id>', methods=['POST'])
def update_postgen(id):
     account = users.query.get(session['user_id'])
     post = account_repository_singleton.get_comp_idgen(id)
     if post is not None and post.useremail == account.username:
             forum_message = request.form.get('question-input')
             post.forum_message = forum_message
             db.session.commit()
             return redirect('/general')