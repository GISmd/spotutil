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

import matplotlib
import matplotlib.pyplot as plt
import os
import sys
import pandas

# You done did it now. We out this bitch
def peace():
    print("usage: python jsontest.py filename [nogui]")
    sys.exit()

def pandamagic(jsonpath, isgui, savepath=None):
    df = pandas.read_json(jsonpath)
    datecols = ['albumReleaseDate', 'addedAt']
    for col in datecols:
        df[col] = pandas.to_datetime(df[col])

    # Plot histogram of addedAt by month and year
    grp = df.groupby([df.addedAt.dt.year.rename('year'),
                      df.addedAt.dt.month.rename('month')])
    plot = grp.addedAt.count().plot(kind='bar')
    fig = plot.get_figure()
    if not savepath:
        fig.savefig("./data/plot.pdf")
    if isgui:
        plt.show()

def main():
    isgui = True

    # Check for proper arguments
    args = len(sys.argv)
    if args > 3:
        peace()
    if args > 2:
        isgui = False if sys.argv[2] == 'nogui' else peace()
    if args > 1:
        jsonname = sys.argv[1]
    else:
        peace()

    # If on a headless terminal, switch to a non-gui backend
    if not isgui:
        matplotlib.use('Agg')

    # Construct path
    cwd = os.getcwd()
    jsonpath = os.path.join(cwd, r'data', jsonname)
    pandamagic(jsonpath, isgui)

main()
