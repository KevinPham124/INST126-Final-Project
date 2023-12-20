# INST126 Final Project by Kevin Pham
# Webscraping Program 

import requests
from bs4 import BeautifulSoup

req = requests.get("")

soup = BeautifulSoup(req.content, "html.parser")

res = soup.title

print(res.get_text())

# user chooses a file to enter
# path_file = input("Enter the path from your working directory to a file you want
to enter (must be the exact name and format!): ")
# instead of seraching for a file, it targets a folder?
folder_search = os.path.exists(input("What folder would you like to search in?: "))
if folder_search == True:
counting_word = input("Enter a word you want to count in this folder:\t")
if counting_word == True:
with open(folder_search) as textfile:
all_text = textfile.read()
# counts words of the text file in lowercase
word_count = all_text.lower().count(counting_word.lower())
# tried to make it loop back to the first prompt when an incorrect folder or word
is entered by the user
# not sure if correct format or how to integrate it into program
while all_text == False:
print("Error, please try again!")
folder_search = os.path.exists(input("What folder would you like to search in?:
"))
if folder_search == True:
counting_word = input("Enter a word you want to count in this folder:\t")
# presents how many words are in the selected text file and closes the program
print("The word '{}' appears '{}' times in the text file '{}'\n\nGoodbye!\
n".format(counting_word, word_count, path_file))