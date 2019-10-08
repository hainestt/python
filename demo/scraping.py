# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def getLinks(url):
    html = urlopen('http://www.pythonscraping.com')
    bs = BeautifulSoup(html)
    imgLocation = bs.find('a', {'id': 'logo'}).find('img')['src']
    urlretrieve(imgLocation, 'logo.jpg')

getLinks('')
