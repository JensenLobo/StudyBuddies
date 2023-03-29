from flask import Flask, render_template, request, redirect, url_for, session
#from your_database_module import db, User
from werkzeug.security import generate_password_hash
app = Flask(__name__)


def hash_password(password):
    return generate_password_hash(password)

@app.route('/')
def index():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'your_username' and password == 'your_password':
            session['username'] = username
            return redirect(url_for('home.html'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.get('/signup')
def signup():
    print("wogh")
    return render_template('signup.html')


@app.post('/signup')
def create_account():
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the passwords match
        if password != confirm_password:
            return render_template('signup.html', error='Passwords do not match')

        # Check if the username ends with "@uncc.edu"
        if not username.endswith('@uncc.edu'):
            return render_template('signup.html', error='Username should end with "@uncc.edu"')

        # Check if the username is already in use
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('signup.html', error='Username is already in use')

        # Validate the password (for example, you might require a certain length or complexity)
        if len(password) < 8:
            return render_template('signup.html', error='Password should be at least 8 characters long')

        # Save the user in the database
        user = User(username=username, password=hash_password(password))
        db.session.add(user)
        db.session.commit()

        # Set the session and redirect to the home page
        session['username'] = username
        return redirect(url_for('about.html'))

@app.route('/major')
def major():
    return render_template('major.html')


# Genreal page for all users to see
@app.route('/general')
def general():
    return render_template('general.html')
