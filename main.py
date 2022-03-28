#from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import db_access as database
#from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://h54023kc:y20-pass@dbhost.cs.man.ac.uk/2021_comp10120_y20'
db = SQLAlchemy(app)

posts = {
    'user_ID': "User ID: ",
    'email':''
}

likedRestaurants = database.getLikesByUserID(1)

print(likedRestaurants)

@app.route('/landing')
def landing():
    return render_template('landingpage.html')

@app.route('/')
@app.route("/home")
def home():
    restaurants = database.passDataToFront(database.getRestaurants())
    return render_template('home.html', restaurants=restaurants)

@app.route("/liked")
def liked():
    return render_template('liked.html', likedRestaurants=likedRestaurants)

@app.route("/account")
def account():
    return render_template('account.html', posts=posts)

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

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
            print("added acc")
        return render_template('signup.html')
    elif request.method == 'POST':
        return render_template('home.html')

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    global posts
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
        userID = database.getUserID(email)
        if password == database.queryUserEmailReturnHash(email):
            posts = {
                'user_ID': "User ID: " + str(userID),
                'email': email
            }
            return render_template('account.html',posts=posts)
        return render_template('signin.html')
    elif request.method == 'POST':
        return render_template('signup.html')
if __name__ == '__main__':
    app.run(debug=True)
