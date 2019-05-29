# Eksisozluk Scraper

## Scraper

Eksisozluk scraper tool.

```python
# import the scraper
from scraper import eksi_page_scaper
# load entries from the given url, between the given pages
entries = eksi_page_scraper('https://eksisozluk.com/game-of-thrones--2213329', page_start=1, page_end=30)
# sort the entries according to favorite count
sorted_fav_entries = sorted(entries, key = lambda e: e.favorite_count, reverse=True)

```

## NLP Tool

NLP Tool is taken from https://github.com/brolin59/PYTHON-TURKCE-DOGAL-DIL-ISLEME-TURKISH-NLP

Some functionality may not work

## ML

Under Development

