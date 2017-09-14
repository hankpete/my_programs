#!/usr/bin/env python3

## read website to get nfl team records and stats, make predictions
## about who will win, send email of picks

#5-15-17

#%%
import urllib.request
import sys

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
print("\nPredictions:")
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
    #score convention, away vs home
    away_pts = np.average( [ team_data[home]["PA"], team_data[away]["PF"] ] )
    home_pts = np.average( [ team_data[home]["PF"], team_data[away]["PA"] ] )
    print("{}: {} @ {}: {}".format(away, int(away_pts), home, int(home_pts)))
    diff = home_pts - away_pts
    if diff >= 0:
        winner = home
    else:
        winner = away
    results.append( {"Home" : home, "Away" : away, "Diff" : diff, \
                     "Winner" : winner, "Bet" : 0} )
    teams.remove(home)
    teams.remove(away)

bet = len(results)
while bet > 0:
    #look for the biggest difference not yet used
    biggest = 0
    for j in range(len(results)):
        if results[j]["Bet"] != 0:
            #already bet on
            continue
        if np.abs(results[j]["Diff"]) >= biggest:
            biggest = np.abs(results[j]["Diff"])
            i = j
    results[i]["Bet"] = str(bet)
    bet -= 1

#read website to get schedule times
#make latex pdf

#map teams
teams = {"ARI":"Cardinals","ATL":"Falcons","BAL":"Ravens","BUF":"Bills","CAR":"Panthers","CHI":"Bears","CIN":"Bengals","CLE":"Browns",
         "DAL":"Cowboys","DEN":"Broncos","DET":"Lions","GB":"Packers","HOU":"Texans","IND":"Cults","JAC":"Jaguars","KC":"Chiefs",
         "MIA":"Dolphins","MIN":"Vikings","NE":"Patriots","NO":"Saints","NYG":"Giants","NYJ":"Jets","OAK":"Raiders","PHI":"Eagles",
         "PIT":"Steelers","LAC":"Chargers","SEA":"Seahawks","SF":"49ers","LAR":"Rams","TB":"Buccaneers","TEN":"Titans","WAS":"Redskins"}

#%%
import urllib.request
import os

#%%
year = "2017"
site = "http://www.thehuddle.com/" + year + "/nfl/nfl-schedule-wk-txt.php"

with urllib.request.urlopen(site) as response:
   html = response.read()

#it comes as character codes. turn into letters
html_str = ""
for i in html:
    html_str += str(chr(i))
#get rid of annoying things now
html_str = html_str.replace("&nbsp","")
html_str = html_str.replace("<br>","")


#%%
#find the part in the html with tables of schedules
#add just those to a text string 

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

text = ""
i = 0
while True:
    if html_str[i:i+6] == "Week "+str(week) or html_str[i:i+7] == "Week "+str(week):
        #our week
        j = i + 5
        while html_str[j] != "<":
            j += 1
        text += "\n\\section*{\\LARGE Football Picks " + year + ": " + html_str[i:j] + "}"
        text += "\n{\\large Hank Bot} \\par"
        text += "\n\\setlength{\\tabcolsep}{2em}"
        text += "\n{\\renewcommand{\\arraystretch}{2}"
        text += "\n\\begin{tabular}{ l l }"

        i = j
        
        game_count = 0
        while html_str[i:i+6] != "Week "+str(week + 1) and html_str[i:i+7] != "Week "+str(week + 1) and i < len(html_str):
            if html_str[i:i+4] == "<td>":
                #new element of list (matchup, time, day)
                j = i + 4
                while html_str[j] != "<":   
                    #go until content done
                    j += 1
                content = html_str[i+4:j]
                for day in days:
                    if day in content: 
                        #new day, make title
                        text += "\n\\textbf{" + content + "} \\\ "

                if " at " in content:
                    #new matchup
                    game_count += 1
                    for r in results:
                        if teams[ r["Winner"] ] in content:
                            if r["Winner"] == r["Home"]:
                                text +=  "\n" + teams[ r["Away"] ] + " @ $\\boxed{ \\text{" + teams[ r["Home"] ] + "} }$ & " + r["Bet"] + " \\\ "
                            else:
                                text +=  "\n$\\boxed{ \\text{" + teams[ r["Away"] ] + "} }$ @ " + teams[ r["Home"] ] + " & " + r["Bet"] + " \\\ "
                    if game_count > 15:
                        text += "\n\\end{tabular}}"

                elif "Byes" in html_str[i+4:j]:
                    #put the byes at the bottom
                    text += "\n\\end{tabular}}"
                    text += "\n\\vfill{}"
                    text += "\n" + content.replace(";", " ").replace(",", ", ")
            i += 1
        break

    else:
        i += 1

                
#put it all in a tex file
Dir = "/home/hpeter/Documents/Football/"
filename = "{}picks_week{}.tex".format(Dir, week)
with open(filename,"w") as f:
    f.write(
"""
\\documentclass[12pt, letterpaper]{article}
\\usepackage[margin=0.9in]{geometry}
\\usepackage[scaled]{helvet}
\\renewcommand\\familydefault{\\sfdefault} 
\\usepackage[T1]{fontenc}
\\usepackage{amsmath}
\\pagestyle{empty}

\\begin{document}
\\setlength{\parindent}{0.5em}
\\setlength{\parskip}{1.4em}
"""
    )
    f.write(text)
    f.write("\n\\end{document}\n")

#%%
#make it
os.system("pdflatex -output-directory {} {} >> pdflatex.out".format(Dir, filename))
print("\nMy picks: {}".format(filename))
os.system("xdg-open {}picks_week{}.pdf > /dev/null 2>&1".format(Dir, week))

os.system("{}random_bot.py {}".format(Dir, week))

