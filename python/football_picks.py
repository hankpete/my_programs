#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 15:14:31 2017

@author: hpeter
"""

## read website to get nfl team records and stats, make predictions
## about who will win, send email of picks

#5-15-17

#%%
import urllib
#import os

#%%
site = "http://www.nfl.com/standings"

with urllib.request.urlopen(site) as response:
   html = response.read()

#it comes as character codes. turn into letters
html_str = ""
for i in html:
    html_str += str(chr(i))


#%%
#find the part in the html with tables of records
#put those in dictionary for teams

def shift(i):
    while html_str[i:i+4] != "<td>":
        i += 1
    return i + 4
    
team_data = {}
teams = ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE",
"DAL","DEN","DET","GB","HOU","IND","JAX","KC",
"MIA","MIN","NE","NO","NYG","NYJ","OAK","PHI",
"PIT","LAC","SEA","SF","LA","TB","TEN","WAS"]
for team in teams:
    i = html_str.index('<a href="/teams/profile?team={}">'.format(team))
    
    i = shift(i)
    wins = html_str[i]
    
    i = shift(i)
    losses = html_str[i]
    
    i = shift(i)
    ties = html_str[i]
    
    team_data[team] = {"W" : wins, "L" : losses, "T" : ties}

print(team_data)
#%%
