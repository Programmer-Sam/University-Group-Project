from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

def start_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://h54023kc:y20-pass@dbhost.cs.man.ac.uk/2021_comp10120_y20'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 20
    db = SQLAlchemy(app)
    return app, db

app, db = start_app()
class users(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   email = db.Column(db.String(200))
   password_hash = db.Column(db.String(100))

   def __init__(self, email, password_hash):
       self.email = email
       self.password_hash = password_hash
class restaurants(db.Model):
    Restaurantid_int = db.Column('restaurant_id', db.Integer, primary_key = True)
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

def AddRestaurant(name, food_type, address, image_url, website):
    inserted_row = restaurants(name, food_type, address, image_url, website)
    db.session.add (inserted_row)
    db.session.commit()
    db.session.close()

def insert_db(email, password):
    inserted_row = users(email,password)
    db.session.add (inserted_row)
    db.session.commit()
    db.session.close()

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
        output_data.append([record.Restaurantid_int, record.Restaurant_Name,
                            record.Food_Type,
                            record.Location,
                            record.Linkpic,
                            record.Linkweb])
    print(output_data)

    return output_data

# def passDataToFront(data):
#     names = []
#     food_type = []
#     locations = []
#     picture = []
#     for record in data:
#         names.append(record[0])
#         food_type.append(record[1])
#         locations.append(record[2])
#         picture.append(record[4])
#     return names, food_type, locations, picture

def getRestaurantsByID(id):
    data = restaurants.query.filter_by(Restaurantid_int=id).first()
    return [data.Restaurantid_int, data.Restaurant_Name, data.Food_Type, data.Location, data.Linkpic, data.Linkweb]

def addLikedLink(Disliked_bit, Userid_int, Restaurantid_int):
    inserted_row = LIKED(Disliked_bit, Userid_int, Restaurantid_int)
    db.session.add (inserted_row)
    db.session.commit()
    db.session.close()
    db.session.expunge_all()

def getLikesByUserID(user_id):
    data = LIKED.query.filter_by(Userid_int=user_id).all()
    output_data = []
    for index, record in enumerate(data):
        output_data.append([record.Disliked_bit,
                            record.Restaurantid_int, *getRestaurantsByID(record.Restaurantid_int)])
    return output_data

def changePasswordByID(input_id, newPassword):
    print(input_id, newPassword)
    if users.query.filter_by(id=input_id).first()!= None:
        db.session.query(users).filter(users.id==input_id).update({'password_hash':newPassword})
        db.session.commit()
        db.session.close()
