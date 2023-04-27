from flask import Flask, render_template, request, redirect, url_for, session
#from your_database_module import db, User
from werkzeug.security import generate_password_hash
from src.models import db, users
from src.repositories.user_repository import account_repository_singleton
from src.security import bcrypt
from dotenv import load_dotenv
import os

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

def hash_password(password):
    return generate_password_hash(password)

@app.route('/')
def index():
    return render_template('about.html')


@app.get('/profileIndex')
def profileIndex():
    if 'user' not in session:
        return render_template('about.html')
    return render_template('profileIndex.html')

     


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
        session['user'] = {
            'username': username
        }
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

    # Check if the username ends with "@uncc.edu"
        if not username.lower().endswith('@uncc.edu'):
          return render_template('signup.html', error='Username should end with "@uncc.edu"')
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
   return render_template("profileIndex.html")
   

@app.route('/major')
def major():
    return render_template('major.html')


# Genreal page for all users to see
@app.route('/general')
def general():
    return render_template('general.html')

@app.get('/ComputerScience')
def compSci():
    print('testing')
    return render_template('compSci_Forum.html')


@app.post('/ComputerScience')
def display():
    message = request.form.get('question-input')
    # print(message) testing if message is holding the text input
    account_repository_singleton.add_post(message)
    return render_template('compSci_Forum.html')

@app.route('/authentication', methods=['POST'])
def authentication():
    return render_template('authentication.html')



@app.route('/business_Forum', methods=['GET', 'POST'])
def business_forum():
    if request.method == 'POST':
        message = request.form['question-input']
        account_repository_singleton.add_post(message)
        return redirect(url_for('business_forum'))
    else:
        posts = set(account_repository_singleton.get_posts())
    return render_template('business_Forum.html', posts=posts)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    message = request.form.get('question-input')
    account_repository_singleton.add_post(message)
    return redirect(url_for('business_forum'))


