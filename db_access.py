from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://t74769sm:y20-pass@dbhost.cs.man.ac.uk/2021_comp10120_y20'
db = SQLAlchemy(app)

class users(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   email = db.Column(db.String(200))
   password_hash = db.Column(db.String(100))

   def __init__(self, email, password_hash):
       self.email = email
       self.password_hash = password_hash

def create_db():
    db.create_all()

def insert_db(email, password):
    inserted_row = users(email,password)
    db.session.add (inserted_row)
    db.session.commit()

def queryUserEmailReturnHash(email_input):
    records = users.query.filter_by(email=email_input).first()
    if records != None:
        return records.password_hash
    else:
        return False
