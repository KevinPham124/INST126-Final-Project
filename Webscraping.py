# INST126 Final Project by Kevin Pham
# Webscraping Program 

import requests
from bs4 import BeautifulSoup

# This variable allows for a user to copy and paste a website url that they would like to scrape text from
url = input("What website would you like to webscrape from?: \n")

# This variable allows for a user to type the specific word that they would like to count on the website they selected
word_to_count = input ("Please enter the specific word you would like to count from this wesbite: \n")
