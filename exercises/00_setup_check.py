"""
Exercise 0 - Setup check
========================
This program is here to check if you have installed the requirements correctly
and to prompt you on how you should install it if you have not done so.

How to run (from inside the exercises folder):
    python3 00_setup_check.py
"""

import sys

print("Python version:", sys.version.split()[0])

try:
    import requests
    print("requests OK   ->", requests.__version__)
except ImportError:
    print("requests MISSING -> run: pip install -r requirements.txt")
    sys.exit(1)

try:
    import bs4
    print("beautifulsoup4 OK ->", bs4.__version__)
except ImportError:
    print("beautifulsoup4 MISSING -> run: pip install -r requirements.txt")
    sys.exit(1)

# Final check: can we reach the practice website?
try:
    r = requests.get("https://books.toscrape.com/", timeout=10)
    print("Website reachable -> HTTP", r.status_code)
except Exception as e:
    print("Could not reach the website:", e)
    sys.exit(1)

print("\nAll good we are ready to start")
