# web-scraping-challenge

In this repo you will find code to collect data about mars. it collect the most resent headlines from nasa. The current featured image from JPL. Measurements and other data about the planet itself. Finally it shows current image of all four of Mars' hemispheres.

Below will guide you through the files contained in the repo.

mission_to_mars.ipynb is code to scrape four websites containing data about mars. The code collects data for storage and presentation of the scraped dat for each of the four site.

scrape_mars.py is the python code to scrape the four websites and collects it into a dictonary for the app.py flask app.

app.py is an app to collect the the dat and transfer it into a mongo database.

index.html is the site to present the dat collectd and offer a scrape button to update the data for the user.

also included are the images for the output of the html for referance.  