#from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import db_access as database
#from forms import RegistrationForm, LoginForm

from xml.dom.minidom import Element
from bs4 import BeautifulSoup
import requests

source = requests.get('https://confidentialguides.com/guide/the-coolest-places-to-eat-in-manchester/').text #gets the webpage html code
soup = BeautifulSoup(source, 'lxml') #connects bs4 to the webpage

li = soup.find_all('li', class_='c-Guide_Item') #finds a li attribute with the specific class (each resturaunt is stored in a seperate new li)
span = soup.find_all('span', class_='o-M10 c-Meta c-Meta-lrg') #this is for getting the type of food


app = database.app
posts = {
    'user_ID': "",
    'email':''
}
i = 0
likedRestaurants = database.getLikesByUserID(1)


@app.route('/')
def landing():
    return render_template('landingpage.html')

@app.route('/home')
@app.route("/home")
def home():
    restaurants = database.passDataToFront(database.getRestaurants())
    return render_template('home.html', restaurants=restaurants, li=li)

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
                'user_ID': userID,
                'email': email
            }
            return render_template('account.html',posts=posts)
        return render_template('signin.html')
    elif request.method == 'POST':
        return render_template('signup.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/changePassword', methods=['GET', 'POST'])
def changePassword():
    print(request.method)
    if request.method == 'GET':
        newPassword = request.args.get('newPassword')
        confirmPassword = request.args.get('confirmPassword')
        print("here")
        if newPassword == confirmPassword:
            database.changePasswordByID(posts["user_ID"], newPassword)
        return render_template('signup.html')
    return render_template('sign.html')
