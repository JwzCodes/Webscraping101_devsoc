"""
Exercise 5 - visiting other pages
========================
Now that we can search through all the information we need, how do we visit other pages?
This catalogue has 50 pages we can go through but for this example we will go through only the first 3


IMPORTANT - be a polite scraper:
    - add time.sleep(1) between requests so we don't accidentaly overload the server with requests.
    - we only do 3 pages here so the exercise is quick.

TASKS:
    1. Loop over pages 1, 2, 3.
    2. Build each page URL.
    3. Scrape the titles from each page and count the total.


How to run (from inside the exercises folder):
    python3 05_visiting_other_pages.py
"""

import time
import requests
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/catalogue/page-{}.html"

all_titles = []

# TODO: loop over page numbers 1 to 3 (inclusive).

