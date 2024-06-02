import requests
from bs4 import BeautifulSoup
import re
import json

class scraper:
    def __init__ (self, SCRAPER_API_END_POINT):
        self.API_END_POINT = SCRAPER_API_END_POINT
    
    
    # fetch the page using url
    def fetch_reader_page(self,PAGE_URL):
        url = self.API_END_POINT + PAGE_URL
        response = requests.get(url)
        if response.status_code == 200:
            return json.dumps({"PAGE_URL": PAGE_URL, "response_status_code": response.status_code, "response_content": response.content.decode('utf-8')}) 
        else:
            return json.dumps({"PAGE_URL": PAGE_URL, "response_status_code": response.status_code, "response_content": "Unable to extract information"}) 
        
    
    def fetch_raw_html(self,PAGE_URL):
        url = PAGE_URL
        response = requests.get(url)
        if response.status_code == 200:
            return json.dumps({"PAGE_URL": PAGE_URL, "response_status_code": response.status_code, "response_content": response.content.decode('utf-8')}) 
        else:
            return json.dumps({"PAGE_URL": PAGE_URL, "response_status_code": response.status_code, "response_content": "Unable to extract information"}) 
    
    # all this type of funciton is name in the way that 
    # (from)_extract_(something) 
    # in this case extract from html "a" tag
    def html_extract_a(self,PAGE_HTML,Pattern):
        soup = BeautifulSoup(PAGE_HTML, 'html.parser')
        a_tags = soup.find_all('a', href=True)
        regex = re.compile(Pattern)
        filtered_links = [(a.text, a['href']) for a in a_tags if regex.search(a['href'])]
        return filtered_links
    
    # extract from the url all the a tag match the pattern
    def url_extract_a(self,PAGE_URL,Pattern):
        url = PAGE_URL
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
            a_tags = soup.find_all('a', href=True)
            regex = re.compile(Pattern)
            filtered_links = [(a.text, a['href']) for a in a_tags if regex.search(a['href'])]
            return json.dumps({"PAGE_URL": PAGE_URL,"Pattern":Pattern, "response_status_code": response.status_code, "response_content": filtered_links}) 
        else :
            return json.dumps({"PAGE_URL": PAGE_URL, "Pattern":Pattern,"response_status_code": response.status_code, "response_content": "Unable to extract information"}) 