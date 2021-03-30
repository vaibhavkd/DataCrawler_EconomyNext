# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:27:19 2020

@author: Vaibhav Deodhe
"""
import csv
import session
from bs4 import BeautifulSoup as bs
import dateparser
from datetime import datetime

session = session.create_session()

def crawl_data():
    
    f = csv.writer(open("article_info.csv", "w", newline=''))
    f.writerow(['Title', 'Link', 'Description', 'Date_Published', 'Date_Fetched', 'Source']) # Write column headers as the first line  
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    
    #We'll get links into article_links
    with open('article_links.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            
            try:
                url = row[0]
                src = session.get(url, headers=headers).text
                soup= bs(src,'lxml') 
    
                #Title of the article
                title = soup.body.h1.string
                
                #Link for an article
                link = url
                
                #Description for the article, we'll concanate all the paragraphs together.
                description = ""
                divs = soup.findAll("div", {"class": "aXjCH"})
                
                for div in divs:
                    content = div.findAll("p")
                    for p in content:
                        description = description + " " + p.text
                
                #Date-Published of article
                datePublished = dateparser.parse(soup.find("span", {"class": "post-date-time"}).text)
                
                #Date-Fetched of article
                dateFetched = datetime.now()
                
                #Source of article
                source = 'Economy Next'
                
                f.writerow([title, link, description, datePublished, dateFetched, source])
                print(url)
                
            except Exception:
                print(f"Article info couldn't be saved.")
            
            


            

if __name__ == "__main__":
    crawl_data()