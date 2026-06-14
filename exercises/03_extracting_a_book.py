"""
Exercise 3 - extracting_a_book
========================
Every book on the page lives inside a container.
If we grab the first one, we can practise extracting the informationh we want
before we do it to the rest of the books.

TASKS:
  1. Find the FIRST book
  2. Get that book's title.
  3. Get that book's price text.
  4. Modify the current implementation to extract all books

How to run (from inside the exercises folder):
    python3 03_extracting_a_book.py
"""

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/index.html"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# TODO 1: grab the first book card.
# Hint: use inspect element to find the class container
# book = ...

# TODO 2: get the title.
# Hint: find where the title is stored

# TODO 3: get the price.
# Hint: you can inspect the location of the price

# TODO 4: how do you modify the current implementation to print all the books?
# Hint: use the keyword 'all'