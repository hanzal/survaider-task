from flask import Flask, request, render_template, url_for, redirect, flash, session, g, send_file, abort
from flask import Flask, request, render_template, url_for, redirect
import os
import datetime

app = Flask(__name__)

app.config.from_object('config')
app.config['MONGOALCHEMY_DATABASE'] = 'reviews'

from models import HotelChains, Hotels, Reviews
from models import db

db.init_app(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    hotelchains = HotelChains.query.all()           #querying everything
    hotels = Hotels.query.all()
    reviews = Reviews.query.all()
    positive = {}                                   #declaring dictionaries
    negative = {}
    neutral = {}
    for hotel in hotels:
        positive[hotel.property_id]=0               #initialising dictionaries
        negative[hotel.property_id]=0
        neutral[hotel.property_id]=0
    for review in reviews:        
        if review.sentiment == 'Positive':          #counting sentments used for loop to reduce db request
            positive[review.hotel.property_id]+=1
        if review.sentiment == 'Negative':
            negative[review.hotel.property_id]+=1
        if review.sentiment == 'Neutral':
            neutral[review.hotel.property_id]+=1
    
    app.logger.info(positive)
    # app.logger.info(reviews[0].hotel.name + ", " + reviews[0].review + ", " + reviews[0].sentiment + ", " + reviews[0].rating)
    return render_template("index.html",page="home", hotelchains=hotelchains, hotels=hotels, positive=positive, negative=negative, neutral=neutral )


@app.route('/<hotelid>')
def hotelreview(hotelid):
    hotels = Hotels.query.all()             #Get all the hotels from db for menu
    for h in hotels:
        if h.property_id == hotelid:        #check if any hotel matches the id provided
            hotel = h
            reviews = Reviews.query.filter(Reviews.hotel.property_id==hotelid).all()
            positive = {}
            negative = {}
            neutral = {}

            positive=0                      #initialising variables to zero
            negative=0
            neutral=0
            for review in reviews:        
                if review.sentiment == 'Positive':      #counting sentments used for loop to reduce db request
                    positive+=1
                if review.sentiment == 'Negative':
                    negative+=1
                if review.sentiment == 'Neutral':
                    neutral+=1
            
            app.logger.info(positive)
            # app.logger.info(reviews[0].hotel.name + ", " + reviews[0].review + ", " + reviews[0].sentiment + ", " + reviews[0].rating)
            return render_template("individual.html",page="individual", hotels=hotels, reviews=reviews, hotel=hotel, positive=positive, negative=negative, neutral=neutral )
    try:
        hotel
    except NameError:
        return render_template("404.html",page="Error")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5050)
