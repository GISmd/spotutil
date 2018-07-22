# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:00:00 2018

@author: mcdeid, twelvvv

Initial Spotify Authorization Code Flow framework

Plan: TBD

Possible useful methods:
    - Return tracks with a given release year or range of years.
    - Return tracks matching certain values in any columns (i.e. if artist
    name=="Rhye" or if trackPopularity>x...)
    - Methods for returning plots on the playlist data
"""

from bottle import route, run, request
import spotipy
from spotipy import oauth2

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = '6680a1079f4d4ce184da86a059111bc2'
SPOTIPY_CLIENT_SECRET = '5b0ff424ff3f43d1bbceb5e110d8893e'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,
                               SPOTIPY_REDIRECT_URI, scope=SCOPE,
                               cache_path=CACHE)


@route('/')
def index():
    """Handle http requests"""
    access_token = ""
    auth_token = sp_oauth.get_cached_token()

    if auth_token:
        print("Found cached token!")
        access_token = auth_token['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            print("Found Spotify auth code in Request URL! "
                  "Trying to get valid access token...")
            token = sp_oauth.get_access_token(code)
            access_token = token['access_token']

    if access_token:
        print("Access token available! Trying to get user information...")
        sp = spotipy.Spotify(access_token)
        user_info = sp.current_user()
        return user_info
    else:
        authButton = ("<a href='" + sp_oauth.get_authorize_url()
                      + "'>Login to Spotify</a>")
        return authButton


run(host='', port=8080)
