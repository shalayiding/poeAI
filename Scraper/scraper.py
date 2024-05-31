import requests
from bs4 import BeautifulSoup
import re


class scraper:
    def __init__ (self, SCRAPER_API_END_POINT):
        self.API_END_POINT = SCRAPER_API_END_POINT
    
    
    # fetch the page using url
    def fetch_reader_page(self,PAGE_URL):
        url = self.API_END_POINT + PAGE_URL
        response = requests.get(url)
        return response
    
    def fetch_raw_html(self,PAGE_URL):
        url = PAGE_URL
        response = requests.get(url)
        return response
    
    # all this type of funciton is name in the way that 
    # (from)_extract_(something) 
    # in this case extract from html "a" tag
    def html_extract_a(self,PAGE_HTML,Pattern):
        soup = BeautifulSoup(PAGE_HTML, 'html.parser')
        a_tags = soup.find_all('a', href=True)
        regex = re.compile(Pattern)
        filtered_links = [(a.text, a['href']) for a in a_tags if regex.search(a['href'])]
        return filtered_links
        