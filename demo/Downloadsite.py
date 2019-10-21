# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import os
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

downloadDir = 'download'
baseUrl = 'http://www.poemhunter.com'

def getAbsoluteUrl(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://' + source[11:]
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://'+source
    else:
        url = baseUrl + '/' + source
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDir):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDir + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return path

def test():
    html = urlopen('https://www.poemhunter.com/rabindranath-tagore/poems/')
    bs = BeautifulSoup(html)
    downloadList = bs.findAll(src = True)

    for download in downloadList:
        
        fileUrl = getAbsoluteUrl(baseUrl, download['src'])
        if fileUrl is not None:
            print(fileUrl)
    
    urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDir))


test()

