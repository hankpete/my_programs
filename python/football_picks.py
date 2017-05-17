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
#get the team stats
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

def next_content():
    """get the content between <td> </td> tags"""
    global i
    #go to the next element in the table
    while html_str[i:i+3] != "<td":
        i += 1
    while html_str[i] != ">":
        i += 1
    i += 1
    #go to the end of the <td> element
    j = i
    while html_str[j] != "<":
        j += 1
    return html_str[i:j]

team_data = {}
teams = ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE",
         "DAL","DEN","DET","GB","HOU","IND","JAX","KC",
         "MIA","MIN","NE","NO","NYG","NYJ","OAK","PHI",
         "PIT","LAC","SEA","SF","LA","TB","TEN","WAS"]
for team in teams:
    #fill dict data, one team at a time, one element of the table at a time
    i = html_str.index('<a href="/teams/profile?team={}">'.format(team))
    wins = next_content()
    losses = next_content()
    ties = next_content()
    pct = next_content()
    pf = next_content()
    pa = next_content()
    net_pts = next_content()
    td = next_content()
    home = next_content()
    road = next_content()
    div = next_content()
    pct_div = next_content()
    conf = next_content()
    pct_conf = next_content()
    non_conf = next_content()
    streak = next_content()
    last5 = next_content()
    team_data[team] = {"W" : wins, "L" : losses, "T" : ties, "Pct" : pct,
             "PF" : pf, "PA" : pa, "Net Pts" : net_pts, "TD" : td,
             "Home" : home, "Road" : road, "Div" : div, "Pct_Div" : pct_div,
             "Conf" : conf, "Pct_Conf" : pct_conf, "Non-Conf" : non_conf,
             "Streak" : streak, "Last 5" : last5}
    
#%%
#now get the team schedules
site = "http://thehuddle.com/2017/nfl/nfl-schedule-grid.php"

with urllib.request.urlopen(site) as response:
   html = response.read()

#it comes as character codes. turn into letters
html_str = ""
for i in html:
    html_str += str(chr(i))
    
#%%
#look up each team and get its schedule
def next_team():
    """get the content between <td> </td> tags"""
    global i
    #go to the next element in the table
    while html_str[i:i+3] != "<td":
        i += 1
    while html_str[i] != ">":
        i += 1
    i += 1
    #go to the end of the <td> element
    j = i
    while html_str[j] != "<":
        j += 1
    return html_str[i:j]

team_schedule = {}
#note: LAR and JAC instead of LA and JAX
teams = ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE",
         "DAL","DEN","DET","GB","HOU","IND","JAC","KC",
         "MIA","MIN","NE","NO","NYG","NYJ","OAK","PHI",
         "PIT","LAC","SEA","SF","LAR","TB","TEN","WAS"]
for team in teams:
    #fill dict data, one team at a time, one element of the table at a time
    team_schedule[team] = {}
    try:
        i = html_str.index('<th><strong>{}</strong></th>'.format(team))
    except:
        i = html_str.index('<th>{}</th>'.format(team))
    for x in range(1,18):
        team_schedule[team][x] = next_team()
        
print(team_schedule["NYJ"])



















