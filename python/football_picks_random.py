#!/usr/bin/env python3

## read website to get nfl team records and stats, make predictions
## about who will win, send email of picks

#5-15-17

#%%
import urllib.request
import sys
import random

try:
    week = int(sys.argv[1])
except:
    week = ""
    while week not in range(1,18):
        week = int(input("Specify week number: "))
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
    pf = float(next_content())
    pa = float(next_content())
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
    if team == "JAX":
        team = "JAC"
    elif team == "LA":
        team = "LAR"
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

#%%
#make predictions as to who will win and how many points to put on them

import numpy as np

results = []
byes = 0
for team in teams:
    if team_schedule[team][week] == "BYE":
        byes += 1
byes = int(byes / 2)
bets = list(range(1, 17 - byes))
while len(teams) != 0:
    team = teams[0]
    opp = team_schedule[team][week]
    if opp == "BYE":
        teams.remove(team)
        continue
    if "@" in opp:
        home = opp.replace("@","")
        away = team
    else:
        home = team
        away = opp
    #randomized
    r = random.randint(0,1)
    if r == 0:
        winner = home
    elif r == 1:
        winner = away
    bet = bets [ random.randint(0, len(bets) - 1) ]
    bets.remove(bet)
    results.append( {"Home" : home, "Away" : away, "Winner" : winner, "Bet" : str(bet)} )
    teams.remove(home)
    teams.remove(away)

#repopulate teams
teams = ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE",
         "DAL","DEN","DET","GB","HOU","IND","JAC","KC",
         "MIA","MIN","NE","NO","NYG","NYJ","OAK","PHI",
         "PIT","LAC","SEA","SF","LAR","TB","TEN","WAS"]




#%%
#make a document to send to mom
#show me the doc
#ask if it is good
#send email to mom if good
import os

filename = "/home/hpeter/Documents/Football/picks_week{}_random.tex".format(week)
with open(filename,"w") as f:
    f.write(
"""
\\documentclass[12pt, letterpaper]{article}
\\usepackage[margin=0.9in]{geometry}
\\usepackage[scaled]{helvet}
\\usepackage{amsmath}
\\renewcommand\\familydefault{\\sfdefault} 
\\usepackage[T1]{fontenc}
\\pagestyle{empty}
\\setlength{\parindent}{1em}
\\setlength{\parskip}{1.5em}

\\begin{document}
"""
    )
    f.write("{\\LARGE Football Picks Week " + str(week) + "} \\par\n")
    f.write("{\\large RANDOM BOT 3000} \\par\n")
    #colomn spacing
    f.write("\\setlength{\\tabcolsep}{2em}\n")
    #row spacing
    f.write("{\\renewcommand{\\arraystretch}{2}\n")
    #put picks in table
    f.write("\\begin{tabular}{ l l }\n")
    bet = len(results)
    while bet > 0:
        for r in results:
            if r["Bet"] == str(bet):
                #box the winner and put match/bet in separate columns
                if r["Winner"] == r["Home"]:
                    f.write(r["Away"] + " @ $\\boxed{ \\text{" + r["Home"] + \
                          "} }$ & " + r["Bet"] + " \\\ \n")
                else:
                    f.write("$\\boxed{ \\text{" + r["Away"] + "} }$ @ " + \
                            r["Home"] + " & " + r["Bet"] + " \\\ \n")
                continue
        bet -= 1

    #end (don't forget row spacing end)
    f.write("\\end{tabular}}\n")
    f.write("\\end{document}\n")


os.system("pdflatex -output-directory /home/hpeter/Documents/Football/ {} >> pdflatex.out".format(filename))
print("\nRandom picks: {}".format(filename))
os.system("xdg-open /home/hpeter/Documents/Football/picks_week{}_random.pdf > /dev/null 2>&1".format(week))

R = input("\nSend to family (y/n)?: ")
if R.lower() == "y":
    to = "cptrsn@comcast.net"
    cc = "slptrsn@gmail.com,stv.ptrsn9@gmail.com"
    subject = "Picks Week " + str(week)
    body = "Here are my picks.\n\nHP"
    attachment = "/home/hpeter/Documents/Football/picks_week" + str(week) + "_random.pdf,"
    attachment += "/home/hpeter/Documents/Football/picks_week" + str(week) + ".pdf"
    
    os.system("thunderbird -compose \"to='{}',cc='{}',subject='{}',body='{}',attachment='{}'\"".format(to,cc,subject,body,attachment))
else:
    print("Exiting Now.")
