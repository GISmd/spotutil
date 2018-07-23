# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 22:17:00 2018

@author: twelvvv

Grab spotify album uri's from http://everynoise.com/spotify_new_albums.html and
add them to a playlist
"""


import requests
from bs4 import BeautifulSoup

# import pdb; pdb.set_trace()
r = requests.get('http://everynoise.com/spotify_new_albums.html')
soup = BeautifulSoup(r.content, "html.parser")
all_releases = soup.select('td[class="allreleases"]')   # right column
a_tags = all_releases[0].select('a')                    # <a href...
del a_tags[0]  # First index doesn't contain album url

uri = list()
for a in a_tags:
    url = a.get('href')
    uri.append(url.split(':')[2])
