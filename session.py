# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:03:50 2020

Here we're creating session for HTTPS Request.
With the help of session, we specify retries for our request 
to bypass HTTPS error

@author: satoshi
"""

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def create_session():
    session = requests.Session()
    retry = Retry(connect = 3, backoff_factor = 0.5)
    adapter = HTTPAdapter(max_retries = retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

