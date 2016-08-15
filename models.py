from flask_mongoalchemy import MongoAlchemy


db = MongoAlchemy()

class HotelChains(db.Document):
    name = db.StringField()
    property_id = db.StringField()

class Hotels(db.Document):
    name = db.StringField()
    hotelchain = db.DocumentField(HotelChains)     #to store parent
    property_id = db.StringField()

class Reviews(db.Document):
    review = db.StringField()
    hotel = db.DocumentField(Hotels)                #to store hotel
    review_link = db.StringField()
    rating = db.StringField()
    sentiment = db.StringField()