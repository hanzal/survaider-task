# Survaider Challenge

This Flask app was built with the requirements provided by the Survaider Team

# What is it about? 
This is a simple Python-Flask App which will read a JSON file containing reviews about hotels and display the Pie charts showing the sentimentality of the reviews.

# JSON Files

Two JSON files are used here.
- For the relationship between Hotel Chain and Hotels - relation.json
- For the reviews of the hotels - reviews.json
The structure of the JSON files are:

relation.json
```sh
[
	{
		"parent": {
			"property_id": "XomY5oG3kvr5grpyoBV",
			"name": "Sterling Holiday Resorts"
		},
		"units": [
			{
				"property_id": "djpKvjWr1mxvMx2bjol",
				"name": "Villagio, Goa"
			},
		]
	}
]
```

reviews.json
```sh
[
	{
		"property_id" : "djpKvjWr1mxvMx2bjol",
		"rating" : "1",
		"review" : "\nIn our last twenty years holidays , this is one of the WORST Resort. Welcome drinks unberarable. Without any information they demanded family members identity card. The room and the house keeping is good. \n",
		"sentiment" : "Negative",
		"review_link" : "https://www.tripadvisor.in/ShowUserReviews-g1925961-d2013657-r215003609-Goa_Villagio_A_Sterling_Holidays_Resort-Betalbatim_Salcette_District_Goa.html#CHECK_RATES_CONT"
	},
	{
		"property_id" : "djpKvjWr1mxvMx2bjol",
		"rating" : "4",
		"review" : "\nThis one is really oven fresh! Here it is...We visited Villagio in the first week of June and to our surprise it had a good occupancy !\n",
		"sentiment" : "Positive",
		"review_link" : "https://www.tripadvisor.in/ShowUserReviews-g1925961-d2013657-r210729760-Goa_Villagio_A_Sterling_Holidays_Resort-Betalbatim_Salcette_District_Goa.html#CHECK_RATES_CONT"
	},
```

JSON files are found in the 'static/json' folder

# Tools used
- Python 3.5
- MongoDB 3.0.4
- Flask
- MongoAlchemy

# Setting up the system
- Install python 3.5
- Install the required tools by:
```sh
$ pip install -r requirements.txt
```
- Install MongoDB

# Running the app
- Start the MongoDB instance on port 27017 (default port)
- Execute createdb.py as
```sh
$ python createdb.py
```
- Start server by
```sh
$ python app.py
```
- Go to localhost:5050 to see the reviews