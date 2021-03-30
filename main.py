# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 21:54:38 2020

@author: Vaibhav Deodhe
"""

import get_article_links
import crawl_data

if __name__ == "__main__":
    try:
        get_article_links.main()
        try:
            crawl_data()
        except Exception:
            print("Failed to crawl data")
    except Exception:
        print("Failed to get article_links")
        
    
    