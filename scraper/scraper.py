"""
Scraper for eksisozluk
"""


from .eksientry import EksiEntry
from bs4 import BeautifulSoup
import requests

def trim_page_link(page_link):
    """
    :param page_link: page link to be trimmed from ?
    :return: page_link before ?
    """
    try:
        return page_link.split('?')[0]
    except Exception as e:
        return page_link


def get_page_count(page_link):
    """
    Gets the number of pages under a topic given in the link
    :param page_link: link of the eksi page
    :return: number of pages
    """

    page_response = requests.get(page_link, headers={"User-Agent":"Mozilla/5.0"}, timeout=10)
    body = BeautifulSoup(page_response.content, "html.parser")
    item = body.find('div', {'class': 'pager'})
    if item:
        try:
            p_count = item.attrs['data-pagecount']
            return int(p_count)
        except Exception as e:
            print(e)
            return 1


def eksi_page_scraper(page_link, page_start=1, page_end=-1):
    """
    Scrapes the pages between start and end for entries.
    Retrieves the entries in the form of list(EksiEntry)

    :param page_link: topic
    :param page_start: which page to start scraping from
    :param page_end: until which page 
    :return: list(EksiEntry)
    """
    page_link = trim_page_link(page_link)
    page_count = get_page_count(page_link)
    p_start = min(max(page_start, 1), page_count)
    p_end = min(page_end, page_count) if page_end > 0 else page_count
    
    entries = []
    for page in range(p_start, p_end + 1):
        p_link = '{}?p={}'.format(page_link, page)
        entries.extend(parse_eksi_link(p_link))
        
    return entries


def parse_eksi_link(page_link):
    """
    :param page_link: link of the page to be parsed
    :return: entries in the page
    """
    page_response = requests.get(page_link, headers={"User-Agent":"Mozilla/5.0"}, timeout=10)
    body = BeautifulSoup(page_response.content, "html.parser")
    ul_finds = body.find('ul', {'id':'entry-item-list'})
    eksi_entries = []
    for li in ul_finds.findAll('li'):
        eksi_entries.append(parse_eksi_entry(li))
        
    return eksi_entries


def parse_eksi_entry(li_item):
    """
    Converts the li in the html to an EksiEntry
    :param li_item: li in html
    :return: EksiEntry
    """
    
    try:
        author = li_item.attrs['data-author']
        author_id = li_item.attrs['data-author-id']
        comment_count = int(li_item.attrs['data-comment-count'])
        favorite_count = int(li_item.attrs['data-favorite-count'])
        data_id = li_item.attrs['data-id']
        is_favorite = li_item.attrs['data-isfavorite']
        is_pinned = li_item.attrs['data-ispinned']
        author = li_item.attrs['data-author']
        time = li_item.find('a', {'class':'entry-date permalink'}).text
        content_raw = li_item.find('div', {'class':'content'}).text
        content = ' '.join(content_raw.split())
        
        return EksiEntry(author, author_id, comment_count, favorite_count, data_id,
                                    is_favorite, is_pinned, content, time)
        return 
    except Exception as e:
        print(e)
        return None

