# INST126 Final Project by Kevin Pham
# Webscraping Program 

#The lines of code below check off the following:
# - Advanced Topic: Webscraping and JSON: Item 10.2
from bs4 import BeautifulSoup
import requests

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
    # Message that displays how many words appears in the website
    print(f"The word '{word_to_count}' appears {word_count} times on the website!")

else: 
    # Error message to show user that the request was not successful
    print(f"Uh Oh! We were unable to request the website you wanted. Status code: {req.status_code}")

