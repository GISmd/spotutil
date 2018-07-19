# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:41:18 2018

@author: mcdeid

Just playing with a json download from Skiley: https://www.skiley.net/

How to use this script as of 19 July 2018:
    Clone the repo, make a data folder in the repo directory, export a playlist
    from skiley and place it in the data folder, make sure the jsonname variable
    matches the json file you want to run this on, and run!

Plan: Create a playlist class that can read a json file and can give you 
various useful outputs via methods using pandas.

Possible useful methods:
    - Return tracks with a given release year or range of years.
    - Return tracks matching certain values in any columns (i.e. if artist 
    name=="Rhye" or if trackPopularity>x...)
    - Methods for returning plots on the playlist data

Issues:
    - Needed to rename series when grouping if grouping by series of the same 
    name: https://github.com/pandas-dev/pandas/issues/21075
"""

import os
import pandas

cwd = os.getcwd()
jsonname = r'Choice Cuts __ 1.json'
jsonpath = os.path.join(cwd, r'data', jsonname)

df = pandas.read_json(jsonpath)
datecols = ['albumReleaseDate','addedAt']
for col in datecols:
    df[col] = pandas.to_datetime(df[col])

# Plot histogram of addedAt by month and year
grp = df.groupby([df.addedAt.dt.year.rename('year'), df.addedAt.dt.month.rename('month')])
grp.addedAt.count().plot(kind='bar')
#print(df.columns)
#print(df[:5])