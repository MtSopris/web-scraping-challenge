from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_scrape")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    mongo_data = mongo.mars_scrape.scraped.find_one()

    # Return template and data
    return render_template("index.html", mars=mongo_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    scrape_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.mars_scrape.scraped.update({}, scrape_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)