from cgitb import html
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm
import os
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

'''
app.config['SECRET_KEY'] = 'HpAscFI5ZgMfDSJHBe9WQ9E787w7fd2a'
db = SQLAlchemy(app)
'''
resturaunts = [['Nandos', '* * * * *', 'M146HQ'], 'goodbye']

source = requests.get('http://schema.org/SearchResultsPage').text
soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', resturaunts=resturaunts)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		return redirect(url_for('home'))
	return render_template('register.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)