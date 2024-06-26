# ir-system-project
## Abstract
The project consist of three main parts: a Crawler, an Indexer, and a Processor. The overall objective of this project was to create a successful search engine. The objective of the crawler was to download web documents in html format; in this project, it scraped titles of the pages scraped from the seed domain [https://en.wikipedia.org/wiki/Illinois_Institute_of_Technology](url). The objective of the indexer was to construct an inverted index in the pickle format that also provided tf-if score and cosine similarity. The objective of the processor was to handle free text queries in json format that also provided query validation and the top-K ranked results; in this project, top-5 results. A couple of challeneges experienced in the development of this project and would guide the next steps of this project were: the limitations to scrape titles only and the manual movement of raw files. The next steps would be to expand the cralwer capability and the automation of the raw files to the neccessary next process.
## Overview
The project is split up into three parts: the crawler folder, the indexer folder, and the processor folder. The crawler is responsbile for scraping the titles of the webpages stemming from the seed domain. Content crawling achieved by a Scrapy based Crawler for downloading web documents in html format. The indexer is responsible for search indexing, it's a Scikit-Learn based Indexer for contructing an inverted index in pickle format. The processor is responsbile for query processing, a Flask based Processor for handling free text queries in json format. 
## Design
This project uses the curl command to handle the free text queries. One terminal would run the json_processor.py file and the other terminal would run the curl command. Simply run the curl command like the one listed in the Operation section to get results of your query. 
## Architecture
The three moving parts of the project are contained within the *Current* Folder and asynchronously interact. The commands below must be ran accordingly and resulting raw .txt or .pkl files must be moved to the next folder prior to running the command. Future implementation would have the movement of these raw files automated. 
## Operation
The following is needed to run this project codebase: Python 3.10+/ sklearn 1.2+/ Scrapy 2.11+/ Flask 2.2+ <br>
The following commands are needed to run the project: <br>
For the crawler: ``` python3 crawling_spider.py``` <br>
For the indexer: ``` python3 pickle_indexer.py``` <br>
For the processor: ``` python3 json_processor.py``` and ```curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -d "{\"query\": \"University\"}"``` <br>
For the curl command ran above, the query can be changed but the query must be a non-empty string query or else it will throw an error. Some like ```curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -d "{\"query\": \"IIT\"}"``` would also be valid. 
## Conclusion
A failure of the project came from the cralwer and indexer part. Initally, I wanted to scrap the paragraphs of the pages scraped by simiply looking for just the "< p></ p>" parahraph tags in html but it resulted in paragraphs that were also side menus and other non-main paragraphs from the page. This issue made it difficult for the indexer to return tf-idf scores and cosine similairty because of the inconsistentcy in format. I opted for scraping the titles of the pages since this would be more precise. A caveat of the project is that when the crawler and the indexer produce the raw_titles.txt file and inverted index file, respectively, each file had to be manually moved to the folder that will be utlizing it in future features. Therefore, everytime I ran the crawler and new raw_titles.txt would be created, then I would have to drag this file to the indexer folder to test the indexer. If I ran the crawler again, I would have to delete the raw_titles.txt file then move it again. This is also true for the inverted index file in the indexer being moved to the processor folder.
## Data Sources
Seed domain [https://en.wikipedia.org/wiki/Illinois_Institute_of_Technology](url) <br>
BeautifulSoup Documentation [https://tedboy.github.io/bs4_doc/](url) <br>
The rest of the links can be found in the Bibliography
## Test Cases
The indexer has a simple text case example checking if the query is in data, future implementations should handle the case where the query is not in the data. <br>
The test cases in the processor are simple if statements checking if the query is a non-empty string in the dataset. If it a valid query, then it will return a result or will throw an error if not a valid query.
## Source Code
Used [BeautifulSoup Documentation]([url](https://tedboy.github.io/bs4_doc/)) for the Crawler to retrieve only the titles of the webpages scraped. 
## Bibliography 
“CHATGPT: Get Instant Answers, Find Inspiration, Learn Something New.” ChatGPT. Accessed April 22, 2024. <br> https://chat.openai.com/. <br>
GeeksforGeeks. “Web Scraping from Wikipedia Using Python - A Complete Guide.” GeeksforGeeks, January 9, 2023.<br>  https://www.geeksforgeeks.org/web-scraping-from-wikipedia-using-python-a-complete-guide/. <br>
Herbert, Anthony. “How to Process Incoming Request Data in Flask.” DigitalOcean, January 26, 2021.<br>  https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask. <br>
NeuralNine. “Coding Web Crawler in Python with Scrapy.” YouTube, November 23, 2022.<br>  https://www.youtube.com/watch?v=m_3gjHGxIJc&t=774s. <br>
S3CloudHub. “How to Create a Simple Flask App in Just 5 Minutes: Python Flask Tutorial for Beginners.” YouTube,<br>  August 18, 2022. https://youtu.be/6M3LzGmIAso?si=r_t_10c7o_bWv-j1. <br>
