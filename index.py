#from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import db_access as database
#from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://h54023kc:y20-pass@dbhost.cs.man.ac.uk/2021_comp10120_y20'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/test', methods=['POST'])
def test():
    return render_template('signin.html')

@app.route('/nav', methods=['GET', 'POST'])
def nav():
    if request.method == 'POST':
        if request.form.get('accountButton') == 'Account':
            return render_template('account.html')
        elif request.form.get('likedButton') == 'Liked':
            return render_template('liked.html')
        elif request.form.get('homeButton') == 'Home':
            return render_template('home.html')
    elif request.method == 'GET':
        return render_template('home.html')
    return render_template('home.html')

@app.route('/accountNav', methods=['GET', 'POST'])
def accountNav():
    if request.method == 'POST':
        if request.form.get('signInButton') == 'SignIn':
            return render_template('signin.html')
        elif request.form.get('signUpButton') == 'SignUp':
            return render_template('signup.html')
    elif request.method == 'GET':
        return render_template('home.html')
    return render_template('home.html')

@app.route('/addUserAccount', methods=['GET', 'POST'])
def addUserAccount():
    if request.method == 'GET':
        email = request.args.get('Email')
        password = request.args.get('Password')
        confirmPassword = request.args.get('confirmPassword')
        if confirmPassword == password:
            database.insert_db(email, password)
        return render_template('signup.html')
    elif request.method == 'POST':
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
