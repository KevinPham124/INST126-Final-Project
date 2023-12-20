# INST126 Final Project by Kevin Pham
# Webscraping Program 

import requests
from bs4 import BeautifulSoup

req = requests.get("")

soup = BeautifulSoup(req.content, "html.parser")

res = soup.title

print(res.get_text())