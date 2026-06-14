"""
Exercise 4 - ratings and stock
========================
Not every value is shown in plain text. For example the star rating is stored as a class
Our job is to extract out the information we want i.e the ratings and stock

TASKS:
    1. For the first book, read the rating word out of the class list.
    2. Read and clean the availability text ("In stock").
    Additional: Modify the current implementation to extract all books on the page
    in this order:
        "Name | Rating | Price | Stock"

How to run (from inside the exercises folder):
    python3 04_ratings_and_stock.py

Hints:
  - book.find("p", class_="star-rating") gives the <p> tag.
  - tag["class"] is a LIST like ["star-rating", "Three"]. The rating is index [1].
  - book.find("p", class_="instock").text.strip() cleans the stock text.
"""


import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

book = soup.find("article", class_="product_pod")

# TODO 1: get the rating word (e.g. "Three").
# hint: rating class

# TODO 2: get the cleaned availability text.

# TODO Additional: How would you get the information for all the books?
# hint: same as the last time we need to use the keyword "all"



