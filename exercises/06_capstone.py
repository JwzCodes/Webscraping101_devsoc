"""
Exercise 6 - CAPSTONE: scrape 5 pages to a CSV
==================================================

To combine everything we have learned together, crawl all 50 pages, collect
title, price, rating and availability for all 1000 books, and save
them to data/books.csv.

A small trick: instead of hard-coding 50 pages, we follow the
"next" button until there isn't one. That way the scraper would still
work if the site added more pages.

TASKS:
    1. find all book cards on the current page.
    2. build a dictionary with title, price, rating, availability.
    3. loop onto the next page using the "next" link.
    4. Write all rows to data/books.csv.

How to run (from inside the exercises folder):
    python 06_capstone.py
"""
import csv
import os
import time
import requests
from bs4 import BeautifulSoup

START_URL = "https://books.toscrape.com/catalogue/page-1.html"
BASE = "https://books.toscrape.com/catalogue/"

all_books = []
url = START_URL
page_count = 0

# TODO 1: get all book cards on this page

# TODO 2: loop and build a dict for each book, append to all_books

# TODO 3: find the next page link

# TODO 4: write all_books to data/books.csv

