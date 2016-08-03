# GrouponWebsiteScrape
The project aims at scraping the Groupon website for the deals in Los Angeles using **Scrapy** by making the crawler boilerplate in order to scrape the website using the pagination links. The scraped data is stored in JSON file as well as transferred to MongoDB using **ITEM_PIPELINES** in pipelines.py. 

#Pre-requisites
IF you are working on windows:
* Install set-up tools
* Install pip
* Install scrapy
* Install PyMongo

#Procedure
```
$ start the Command prompt
$ start the MongoDB by typing mongod on the command prompt
$ start the mongodb by typing mongo on the command prompt
$ start scraping the website by typing **scrapy crawl <crawler_name>**
```

#Scraped contents
In this project the scraped data consist of:
```
$ Link to the deal
$ Title of the deal
$ Location of the deals
$ Original price of the deal
$ Discounted price of the deal
$ Likes ratio of the deal
```
#Enhancements
This project can be extended to create a cronjob where it runs every morning to get the fresh deals and store in DB
