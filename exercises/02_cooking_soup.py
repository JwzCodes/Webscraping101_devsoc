"""
Exercise 2 - Cooking the soup
========================
In this excersise we will parse raw HTML, which is just one long string. BeautifulSoup turns it into
a tree we can search. We "make soup" out of the HTML.

TASKS:
  1. Download the page (same as exercise 1).
  2. Create a BeautifulSoup object from response.text.
  3. Print the page <title>.
  4. Print how many links are on the page.

How to run (from inside the exercises folder):
    python3 02_cooking_soup.py
"""

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

response = requests.get(URL)

# TODO 1: setup the soup. Use the "html.parser" parser.
# soup = ...

# TODO 2: print the page title text. Hint: soup.title.text
# print("Page title:", ...)

# TODO 3: find all links and print how many there are.
# Hint: the <a> tag may have something to do with it


