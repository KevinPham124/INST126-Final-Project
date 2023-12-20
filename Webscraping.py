# INST126 Final Project by Kevin Pham
# Webscraping Program 

import requests
from bs4 import BeautifulSoup

# This variable allows for a user to copy and paste a website url that they would like to scrape text from
url = input("What website would you like to webscrape from?: \n")

# This variable allows for a user to type the specific word that they would like to count on the website they selected
word_to_count = input ("Please enter the specific word you would like to count from this wesbite: \n")

# This variable makes a request to the website that the user wants to scrape from
req = requests.get(url)

# This checks to see if the request was successful, equaling status code 200 which means the response was OK
if req.status_code == 200:
    # This variable parses the HTML content of the website that the user wants to scrape from
    soup = BeautifulSoup(req.content, "html.parser")
    # This variable counts the words on the website
    word_count = soup.get_text().lower().split().count(word_to_count.lower())