from app import app
from flask import url_for
from models import db
import json
db.init_app(app)

from app import HotelChains, Hotels, Reviews
with app.app_context():

    with open('static/json/relation.json', encoding='utf8') as relations_file:    
        relations = json.load(relations_file)
        for relation in relations:
            HotelChain = HotelChains(name = relation['parent']['name'], property_id = relation['parent']['property_id'])
            HotelChain.save()
            for hotel in relation['units']:
                app.logger.info(hotel['name'])
                new_hotel = Hotels(name= hotel['name'], hotelchain = HotelChain, property_id = hotel['property_id'])
                new_hotel.save()


    with open('static/json/reviews.json', encoding='utf8') as reviews_file:    
        reviews = json.load(reviews_file)
        for review in reviews:
            hotel = Hotels.query.filter(Hotels.property_id == review['property_id']).first()
            app.logger.info(hotel.name + " : " + review['sentiment'])
            app.logger.info(hotel.name)
            new_review = Reviews(review=review['review'], hotel=hotel, review_link=review['review_link'], sentiment=review['sentiment'], rating=review['rating'])
            new_review.save()