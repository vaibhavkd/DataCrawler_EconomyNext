# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:18:41 2020

@author: Vaibhav Deodhe
"""
import session
from bs4 import BeautifulSoup as bs
import csv
import re

session = session.create_session()

#Here we will check if article_link is valid or not
def check_validity(article_link):
    search = re.search("/page/", article_link)
    if search or (article_link == "#"):
        return False
    else:
        return True

def get_article_links():
    try:
        f = csv.writer(open("article_links.csv", "w", newline=''))
        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        for i in range(1, 187):
            url = "https://economynext.com/economy/" + f"page/{i}/"
            print(url)
            src = session.get(url, headers=headers).text
            soup=bs(src,'lxml') 
            divs = soup.findChildren('div', {'class': 'col-8'})
            for div in divs:
                link = div.find('a')
                article_link = link.get('href')
                f.writerow([article_link])
    except Exception:
        print("Retry")
            
        

    
if __name__ == "__main__":
    get_article_links()


