from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://h54023kc:y20-pass@dbhost.cs.man.ac.uk/2021_comp10120_y20'
db = SQLAlchemy(app)

class users(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   email = db.Column(db.String(200))
   password_hash = db.Column(db.String(100))

   def __init__(self, email, password_hash):
       self.email = email
       self.password_hash = password_hash
class restaurants(db.Model):
    id = db.Column('restaurant_id', db.Integer, primary_key = True)
    Restaurant_Name = db.Column(db.String(100))
    Food_Type = db.Column(db.String(200))
    Location = db.Column(db.String(200))
    Linkpic = db.Column(db.String(300))
    Linkweb = db.Column(db.String(300))

    def __init__(self, Restaurant_Name, Food_Type,Location,Linkpic,Linkweb):
        self.Restaurant_Name = Restaurant_Name
        self.Food_Type = Food_Type
        self.Location = Location
        self.Linkpic = Linkpic
        self.Linkweb = Linkweb

class LIKED(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    Disliked_bit = db.Column(db.Boolean)
    Userid_int = db.Column(db.Integer)
    Restaurantid_int = db.Column(db.Integer)

    def __init__(self,Disliked_bit,Userid_int,Restaurantid_int):
        self.Disliked_bit = Disliked_bit
        self.Userid_int = Userid_int
        self.Restaurantid_int = Restaurantid_int
def create_db():
    db.create_all()

def AddRestaurants():
    name = "Ice Stone Gelato"
    food_type = "Ice Cream and Deserts"
    Address = "M1 7DY"
    Linkweb = "https://www.google.com/maps/place/IceStone+Gelato/@53.4704223,-2.2373532,21z/data=!4m13!1m7!3m6!1s0x487bb19331bc9ed3:0x5a905cb68ffc970b!2sOxford+Rd,+Manchester+M1+7DY!3b1!8m2!3d53.4704789!4d-2.2370621!3m4!1s0x487bb19331f7e379:0x105d79e57595fd10!8m2!3d53.4704983!4d-2.2372026"
    inserted_row = restaurants(name,food_type,Address,"",Linkweb)
    db.session.add (inserted_row)
    db.session.commit()

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
def getUserID(email):
    records = users.query.filter_by(email=email).first()
    if records != None:
        return records.id

def getRestaurants():
    data = restaurants.query.all()
    output_data = []
    for record in data:
        output_data.append([record.Restaurant_Name,
                            record.Food_Type,
                            record.Location,
                            record.Linkpic,
                            record.Linkweb])
    return output_data

def getRestaurantsByID(id):
    data = restaurants.query.filter_by(id=id).first()
    return [data.Restaurant_Name, data.Food_Type, data.Location, data.Linkpic, data.Linkweb]

def addLikedLink(Disliked_bit, Userid_int, Restaurantid_int):
    inserted_row = LIKED(Disliked_bit, Userid_int, Restaurantid_int)
    db.session.add (inserted_row)
    db.session.commit()

def getLikesByUserID(user_id):
    data = LIKED.query.filter_by(Userid_int=user_id).all()
    output_data = []
    for index, record in enumerate(data):
        output_data.append([record.Disliked_bit,
                            record.Restaurantid_int])
        output_data[index].append(getRestaurantsByID(record.Restaurantid_int))
    return output_data
