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
accountDetails = {
    "userID": "",
    "email": ""
}


@app.route('/')
def landing():
    return render_template('landingpage.html')

@app.route('/home')
@app.route("/home")
def home():
    restaurants = database.getRestaurants()
    #print(restaurants)
    return render_template('home.html', restaurants=restaurants, li=li)

@app.route("/liked")
def liked():
    likedRestaurants = database.getLikesByUserID(int(accountDetails["userID"]))
    return render_template('liked.html', likedRestaurants=likedRestaurants, len=len(likedRestaurants))

@app.route("/likeRestaurant")
def likeRestaurant():
    id = request.args.get('id')
    database.addLikedLink(0, accountDetails["userID"], id)
    print("Liking restaurant " + str(id))
    return "hello"

@app.route("/account")
def account():
    #print(accountDetails)
    return render_template('account.html', accountDetails=accountDetails)

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
        return render_template('signin.html')
    elif request.method == 'POST':
        return render_template('home.html')

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    global accountDetails
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
        userID = database.getUserID(email)
        if password == database.queryUserEmailReturnHash(email):
            accountDetails = {
                "userID": userID,
                "email": email
            }
            return account()
        return render_template('signin.html')
    elif request.method == 'POST':
        return render_template('signup.html')
@app.route('/changePassword', methods=['GET', 'POST'])
def changePassword():
    if request.method == 'GET':
        newPassword = request.args.get('newPassword')
        confirmPassword = request.args.get('confirmPassword')
        if newPassword == confirmPassword:
            database.changePasswordByID(accountDetails["userID"], newPassword)
            return signin()
    return signin()

if __name__ == '__main__':
    app.run(debug=True)
