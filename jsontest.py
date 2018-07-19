# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:41:18 2018

@author: mcdeid

Just playing with a json download from Skiley: https://www.skiley.net/

Plan: Create a playlist class that can read a json file and can give you 
various useful outputs via methods using pandas.

Possible useful methods:
    - Return tracks with a given release year or range of years.
    - Return tracks matching certain values in any columns (i.e. if artist 
    name=="Rhye" or if trackPopularity>x...)
    - Methods for returning plots on the playlist data
"""

import os
import pandas as pd

cwd = os.getcwd()
jsonname = r'Choice Cuts __ 1.json'
jsonpath = os.path.join(cwd, r'data', jsonname)

df = pd.read_json(jsonpath)
datecols = ['albumReleaseDate','addedAt']
for col in datecols:
    df[col] = pd.to_datetime(df[col])
# Plot histogram of addedAt by month and year
df.addedAt.groupby([df.addedAt.dt.year, df.addedAt.dt.month]).count().plot(kind='bar')
#print(df.columns)
#print(df[:5])