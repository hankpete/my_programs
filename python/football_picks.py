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
    
#random data
#team_data = {'JAX': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 52.87435980765907, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.625, 'PA': 42.204931017453404, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 28, 'L': 6, 'Net Pts': 10.669428790205664, 'W': 10, 'T': 0}, 'CIN': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 43.28356446600784, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0625, 'PA': 33.07707074565975, 'Non-Conf': '0-0', 'Streak': 2, 'TD': 4, 'L': 15, 'Net Pts': 10.206493720348085, 'W': 1, 'T': 0}, 'IND': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 12.509404878538199, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.25, 'PA': 75.3468097809007, 'Non-Conf': '0-0', 'Streak': 0, 'TD': 55, 'L': 12, 'Net Pts': -62.8374049023625, 'W': 4, 'T': 0}, 'SEA': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 64.30606438397878, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.5625, 'PA': 24.437682440589647, 'Non-Conf': '0-0', 'Streak': 10, 'TD': 71, 'L': 7, 'Net Pts': 39.86838194338913, 'W': 9, 'T': 0}, 'MIA': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 87.91874090354852, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 63.0041093316548, 'Non-Conf': '0-0', 'Streak': 7, 'TD': 10, 'L': 3, 'Net Pts': 24.91463157189372, 'W': 13, 'T': 0}, 'ATL': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 68.25993924414338, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.25, 'PA': 31.047014917949145, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 92, 'L': 12, 'Net Pts': 37.21292432619424, 'W': 4, 'T': 0}, 'PHI': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 15.149787593668984, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.3125, 'PA': 22.177406565910474, 'Non-Conf': '0-0', 'Streak': 5, 'TD': 89, 'L': 11, 'Net Pts': -7.0276189722414895, 'W': 5, 'T': 0}, 'SF': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 44.19624615986885, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.125, 'PA': 19.73792206841495, 'Non-Conf': '0-0', 'Streak': 2, 'TD': 86, 'L': 14, 'Net Pts': 24.4583240914539, 'W': 2, 'T': 0}, 'NYG': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 20.451114291238483, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0, 'PA': 38.02605596980951, 'Non-Conf': '0-0', 'Streak': 0, 'TD': 73, 'L': 16, 'Net Pts': -17.57494167857103, 'W': 0, 'T': 0}, 'PIT': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 75.44145806401082, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0625, 'PA': 25.97811731733961, 'Non-Conf': '0-0', 'Streak': 2, 'TD': 81, 'L': 15, 'Net Pts': 49.46334074667121, 'W': 1, 'T': 0}, 'NE': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 73.79153066033584, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.3125, 'PA': 38.73922961220578, 'Non-Conf': '0-0', 'Streak': 0, 'TD': 99, 'L': 11, 'Net Pts': 35.052301048130055, 'W': 5, 'T': 0}, 'WAS': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 96.6687742041372, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.875, 'PA': 34.345760222654995, 'Non-Conf': '0-0', 'Streak': 14, 'TD': 46, 'L': 2, 'Net Pts': 62.3230139814822, 'W': 14, 'T': 0}, 'TEN': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 14.951389417701888, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 64.53747227151499, 'Non-Conf': '0-0', 'Streak': 8, 'TD': 9, 'L': 3, 'Net Pts': -49.586082853813096, 'W': 13, 'T': 0}, 'TB': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 11.721456709920542, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.5, 'PA': 22.706847812823682, 'Non-Conf': '0-0', 'Streak': 0, 'TD': 7, 'L': 8, 'Net Pts': -10.98539110290314, 'W': 8, 'T': 0}, 'DAL': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 30.438623065695992, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.6875, 'PA': 64.39679321212375, 'Non-Conf': '0-0', 'Streak': 6, 'TD': 56, 'L': 5, 'Net Pts': -33.95817014642776, 'W': 11, 'T': 0}, 'CLE': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 59.091505836557744, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 2.3212450303987, 'Non-Conf': '0-0', 'Streak': 9, 'TD': 22, 'L': 3, 'Net Pts': 56.770260806159044, 'W': 13, 'T': 0}, 'DEN': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 28.828170399732755, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 33.94931360100026, 'Non-Conf': '0-0', 'Streak': 6, 'TD': 33, 'L': 3, 'Net Pts': -5.1211432012675075, 'W': 13, 'T': 0}, 'MIN': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 14.373959022207439, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.6875, 'PA': 72.12092249364235, 'Non-Conf': '0-0', 'Streak': 8, 'TD': 49, 'L': 5, 'Net Pts': -57.74696347143492, 'W': 11, 'T': 0}, 'BUF': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 0.5765071186098814, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.1875, 'PA': 39.47988044709155, 'Non-Conf': '0-0', 'Streak': 4, 'TD': 31, 'L': 13, 'Net Pts': -38.90337332848167, 'W': 3, 'T': 0}, 'BAL': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 21.83104564662628, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.75, 'PA': 66.27217566507605, 'Non-Conf': '0-0', 'Streak': 11, 'TD': 98, 'L': 4, 'Net Pts': -44.44113001844977, 'W': 12, 'T': 0}, 'OAK': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 71.91138423689547, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 1.0, 'PA': 74.4825880843894, 'Non-Conf': '0-0', 'Streak': 4, 'TD': 43, 'L': 0, 'Net Pts': -2.5712038474939334, 'W': 16, 'T': 0}, 'HOU': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 53.549484069404315, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.4375, 'PA': 12.67104078329645, 'Non-Conf': '0-0', 'Streak': 6, 'TD': 64, 'L': 9, 'Net Pts': 40.87844328610787, 'W': 7, 'T': 0}, 'GB': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 35.41257631687237, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.125, 'PA': 80.46831918629591, 'Non-Conf': '0-0', 'Streak': 3, 'TD': 43, 'L': 14, 'Net Pts': -45.05574286942355, 'W': 2, 'T': 0}, 'DET': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 46.91166779547425, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.3125, 'PA': 7.577324303522737, 'Non-Conf': '0-0', 'Streak': 5, 'TD': 25, 'L': 11, 'Net Pts': 39.334343491951515, 'W': 5, 'T': 0}, 'CHI': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 16.181474405915573, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.75, 'PA': 34.49411381931993, 'Non-Conf': '0-0', 'Streak': 3, 'TD': 91, 'L': 4, 'Net Pts': -18.312639413404355, 'W': 12, 'T': 0}, 'LA': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 1.2357985486113998, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.9375, 'PA': 7.378605887822564, 'Non-Conf': '0-0', 'Streak': 15, 'TD': 80, 'L': 1, 'Net Pts': -6.142807339211164, 'W': 15, 'T': 0}, 'NO': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 60.39886659805158, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0, 'PA': 37.19190361462223, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 89, 'L': 16, 'Net Pts': 23.206962983429356, 'W': 0, 'T': 0}, 'LAC': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 3.2938648673589976, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.4375, 'PA': 51.9244731485912, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 94, 'L': 9, 'Net Pts': -48.6306082812322, 'W': 7, 'T': 0}, 'CAR': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 39.4050015379659, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.375, 'PA': 43.947706931168064, 'Non-Conf': '0-0', 'Streak': 3, 'TD': 24, 'L': 10, 'Net Pts': -4.542705393202162, 'W': 6, 'T': 0}, 'KC': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 10.58482182602022, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 97.30023618867429, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 27, 'L': 3, 'Net Pts': -86.71541436265407, 'W': 13, 'T': 0}, 'ARI': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 93.11526655058593, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0625, 'PA': 39.51864995749621, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 51, 'L': 15, 'Net Pts': 53.59661659308972, 'W': 1, 'T': 0}, 'NYJ': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 70.26475529821165, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.9375, 'PA': 40.22974377964914, 'Non-Conf': '0-0', 'Streak': 9, 'TD': 29, 'L': 1, 'Net Pts': 30.035011518562513, 'W': 15, 'T': 0}}

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
#saved output:       
#team_schedule={'CIN': {1: 'BAL', 2: 'HOU', 3: '@GB', 4: '@CLE', 5: 'BUF', 6: 'BYE', 7: '@PIT', 8: 'IND', 9: '@JAC', 10: '@TEN', 11: '@DEN', 12: 'CLE', 13: 'PIT', 14: 'CHI', 15: '@MIN', 16: 'DET', 17: '@BAL'}, 'IND': {1: '@LAR', 2: 'ARI', 3: 'CLE', 4: '@SEA', 5: 'SF', 6: '@TEN', 7: 'JAC', 8: '@CIN', 9: '@HOU', 10: 'PIT', 11: 'BYE', 12: 'TEN', 13: '@JAC', 14: '@BUF', 15: 'DEN', 16: '@BAL', 17: 'HOU'}, 'SEA': {1: '@GB', 2: 'SF', 3: '@TEN', 4: 'IND', 5: '@LAR', 6: 'BYE', 7: '@NYG', 8: 'HOU', 9: 'WAS', 10: '@ARI', 11: 'ATL', 12: '@SF', 13: 'PHI', 14: '@JAC', 15: 'LAR', 16: '@DAL', 17: 'ARI'}, 'MIA': {1: 'TB', 2: '@LAC', 3: '@NYJ', 4: 'NO', 5: 'TEN', 6: '@ATL', 7: 'NYJ', 8: '@BAL', 9: 'OAK', 10: '@CAR', 11: 'BYE', 12: '@NE', 13: 'DEN', 14: 'NE', 15: '@BUF', 16: '@KC', 17: 'BUF'}, 'ATL': {1: '@CHI', 2: 'GB', 3: '@DET', 4: 'BUF', 5: 'BYE', 6: 'MIA', 7: '@NE', 8: '@NYJ', 9: '@CAR', 10: 'DAL', 11: '@SEA', 12: 'TB', 13: 'MIN', 14: 'NO', 15: '@TB', 16: '@NO', 17: 'CAR'}, 'PHI': {1: '@WAS', 2: '@KC', 3: 'NYG', 4: '@LAC', 5: 'ARI', 6: '@CAR', 7: 'WAS', 8: 'SF', 9: 'DEN', 10: 'BYE', 11: '@DAL', 12: 'CHI', 13: '@SEA', 14: '@LAR', 15: '@NYG', 16: 'OAK', 17: 'DAL'}, 'SF': {1: 'CAR', 2: '@SEA', 3: 'LAR', 4: '@ARI', 5: '@IND', 6: '@WAS', 7: 'DAL', 8: '@PHI', 9: 'ARI', 10: 'NYG', 11: 'BYE', 12: 'SEA', 13: '@CHI', 14: '@HOU', 15: 'TEN', 16: 'JAC', 17: '@LAR'}, 'NYG': {1: '@DAL', 2: 'DET', 3: '@PHI', 4: '@TB', 5: 'LAC', 6: '@DEN', 7: 'SEA', 8: 'BYE', 9: 'LAR', 10: '@SF', 11: 'KC', 12: '@WAS', 13: '@OAK', 14: 'DAL', 15: 'PHI', 16: '@ARI', 17: 'WAS'}, 'PIT': {1: '@CLE', 2: 'MIN', 3: '@CHI', 4: '@BAL', 5: 'JAC', 6: '@KC', 7: 'CIN', 8: '@DET', 9: 'BYE', 10: '@IND', 11: 'TEN', 12: 'GB', 13: '@CIN', 14: 'BAL', 15: 'NE', 16: '@HOU', 17: 'CLE'}, 'NE': {1: 'KC', 2: '@NO', 3: 'HOU', 4: 'CAR', 5: '@TB', 6: '@NYJ', 7: 'ATL', 8: 'LAC', 9: 'BYE', 10: '@DEN', 11: '@OAK', 12: 'MIA', 13: '@BUF', 14: '@MIA', 15: '@PIT', 16: 'BUF', 17: 'NYJ'}, 'WAS': {1: 'PHI', 2: '@LAR', 3: 'OAK', 4: '@KC', 5: 'BYE', 6: 'SF', 7: '@PHI', 8: 'DAL', 9: '@SEA', 10: 'MIN', 11: '@NO', 12: 'NYG', 13: '@DAL', 14: '@LAC', 15: 'ARI', 16: 'DEN', 17: '@NYG'}, 'JAC': {1: '@HOU', 2: 'TEN', 3: 'BAL', 4: '@NYJ', 5: '@PIT', 6: 'LAR', 7: '@IND', 8: 'BYE', 9: 'CIN', 10: 'LAC', 11: '@CLE', 12: '@ARI', 13: 'IND', 14: 'SEA', 15: 'HOU', 16: '@SF', 17: '@TEN'}, 'TB': {1: '@MIA', 2: 'CHI', 3: '@MIN', 4: 'NYG', 5: 'NE', 6: '@ARI', 7: '@BUF', 8: 'CAR', 9: '@NO', 10: 'NYJ', 11: 'BYE', 12: '@ATL', 13: '@GB', 14: 'DET', 15: 'ATL', 16: '@CAR', 17: 'NO'}, 'TEN': {1: 'OAK', 2: '@JAC', 3: 'SEA', 4: '@HOU', 5: '@MIA', 6: 'IND', 7: '@CLE', 8: 'BYE', 9: 'BAL', 10: 'CIN', 11: '@PIT', 12: '@IND', 13: 'HOU', 14: '@ARI', 15: '@SF', 16: 'LAR', 17: 'JAC'}, 'DAL': {1: 'NYG', 2: '@DEN', 3: '@ARI', 4: 'LAR', 5: 'GB', 6: 'BYE', 7: '@SF', 8: '@WAS', 9: 'KC', 10: '@ATL', 11: 'PHI', 12: 'LAC', 13: 'WAS', 14: '@NYG', 15: '@OAK', 16: 'SEA', 17: '@PHI'}, 'CLE': {1: 'PIT', 2: '@BAL', 3: '@IND', 4: 'CIN', 5: 'NYJ', 6: '@HOU', 7: 'TEN', 8: 'MIN', 9: 'BYE', 10: '@DET', 11: 'JAC', 12: '@CIN', 13: '@LAC', 14: 'GB', 15: 'BAL', 16: '@CHI', 17: '@PIT'}, 'DEN': {1: 'LAC', 2: 'DAL', 3: '@BUF', 4: 'OAK', 5: 'BYE', 6: 'NYG', 7: '@LAC', 8: '@KC', 9: '@PHI', 10: 'NE', 11: 'CIN', 12: '@OAK', 13: '@MIA', 14: 'NYJ', 15: '@IND', 16: '@WAS', 17: 'KC'}, 'MIN': {1: 'NO', 2: '@PIT', 3: 'TB', 4: 'DET', 5: '@CHI', 6: 'GB', 7: 'BAL', 8: '@CLE', 9: 'BYE', 10: '@WAS', 11: 'LAR', 12: '@DET', 13: '@ATL', 14: '@CAR', 15: 'CIN', 16: '@GB', 17: 'CHI'}, 'BUF': {1: 'NYJ', 2: '@CAR', 3: 'DEN', 4: '@ATL', 5: '@CIN', 6: 'BYE', 7: 'TB', 8: 'OAK', 9: '@NYJ', 10: 'NO', 11: '@LAC', 12: '@KC', 13: 'NE', 14: 'IND', 15: 'MIA', 16: '@NE', 17: '@MIA'}, 'BAL': {1: '@CIN', 2: 'CLE', 3: '@JAC', 4: 'PIT', 5: '@OAK', 6: 'CHI', 7: '@MIN', 8: 'MIA', 9: '@TEN', 10: 'BYE', 11: '@GB', 12: 'HOU', 13: 'DET', 14: '@PIT', 15: '@CLE', 16: 'IND', 17: 'CIN'}, 'OAK': {1: '@TEN', 2: 'NYJ', 3: '@WAS', 4: '@DEN', 5: 'BAL', 6: 'LAC', 7: 'KC', 8: '@BUF', 9: '@MIA', 10: 'BYE', 11: 'NE', 12: 'DEN', 13: 'NYG', 14: '@KC', 15: 'DAL', 16: '@PHI', 17: '@LAC'}, 'HOU': {1: 'JAC', 2: '@CIN', 3: '@NE', 4: 'TEN', 5: 'KC', 6: 'CLE', 7: 'BYE', 8: '@SEA', 9: 'IND', 10: '@LAR', 11: 'ARI', 12: '@BAL', 13: '@TEN', 14: 'SF', 15: '@JAC', 16: 'PIT', 17: '@IND'}, 'GB': {1: 'SEA', 2: '@ATL', 3: 'CIN', 4: 'CHI', 5: '@DAL', 6: '@MIN', 7: 'NO', 8: 'BYE', 9: 'DET', 10: '@CHI', 11: 'BAL', 12: '@PIT', 13: 'TB', 14: '@CLE', 15: '@CAR', 16: 'MIN', 17: '@DET'}, 'DET': {1: 'ARI', 2: '@NYG', 3: 'ATL', 4: '@MIN', 5: 'CAR', 6: '@NO', 7: 'BYE', 8: 'PIT', 9: '@GB', 10: 'CLE', 11: '@CHI', 12: 'MIN', 13: '@BAL', 14: '@TB', 15: 'CHI', 16: '@CIN', 17: 'GB'}, 'CHI': {1: 'ATL', 2: '@TB', 3: 'PIT', 4: '@GB', 5: 'MIN', 6: '@BAL', 7: 'CAR', 8: '@NO', 9: 'BYE', 10: 'GB', 11: 'DET', 12: '@PHI', 13: 'SF', 14: '@CIN', 15: '@DET', 16: 'CLE', 17: '@MIN'}, 'NO': {1: '@MIN', 2: 'NE', 3: '@CAR', 4: '@MIA', 5: 'BYE', 6: 'DET', 7: '@GB', 8: 'CHI', 9: 'TB', 10: '@BUF', 11: 'WAS', 12: '@LAR', 13: 'CAR', 14: '@ATL', 15: 'NYJ', 16: 'ATL', 17: '@TB'}, 'LAC': {1: '@DEN', 2: 'MIA', 3: 'KC', 4: 'PHI', 5: '@NYG', 6: '@OAK', 7: 'DEN', 8: '@NE', 9: 'BYE', 10: '@JAC', 11: 'BUF', 12: '@DAL', 13: 'CLE', 14: 'WAS', 15: '@KC', 16: '@NYJ', 17: 'OAK'}, 'LAR': {1: 'IND', 2: 'WAS', 3: '@SF', 4: '@DAL', 5: 'SEA', 6: '@JAC', 7: 'ARI', 8: 'BYE', 9: '@NYG', 10: 'HOU', 11: '@MIN', 12: 'NO', 13: '@ARI', 14: 'PHI', 15: '@SEA', 16: '@TEN', 17: 'SF'}, 'CAR': {1: '@SF', 2: 'BUF', 3: 'NO', 4: '@NE', 5: '@DET', 6: 'PHI', 7: '@CHI', 8: '@TB', 9: 'ATL', 10: 'MIA', 11: 'BYE', 12: '@NYJ', 13: '@NO', 14: 'MIN', 15: 'GB', 16: 'TB', 17: '@ATL'}, 'KC': {1: '@NE', 2: 'PHI', 3: '@LAC', 4: 'WAS', 5: '@HOU', 6: 'PIT', 7: '@OAK', 8: 'DEN', 9: '@DAL', 10: 'BYE', 11: '@NYG', 12: 'BUF', 13: '@NYJ', 14: 'OAK', 15: 'LAC', 16: 'MIA', 17: '@DEN'}, 'ARI': {1: '@DET', 2: '@IND', 3: 'DAL', 4: 'SF', 5: '@PHI', 6: 'TB', 7: '@LAR', 8: 'BYE', 9: '@SF', 10: 'SEA', 11: '@HOU', 12: 'JAC', 13: 'LAR', 14: 'TEN', 15: '@WAS', 16: 'NYG', 17: '@SEA'}, 'NYJ': {1: '@BUF', 2: '@OAK', 3: 'MIA', 4: 'JAC', 5: '@CLE', 6: 'NE', 7: '@MIA', 8: 'ATL', 9: 'BUF', 10: '@TB', 11: 'BYE', 12: 'CAR', 13: 'KC', 14: '@DEN', 15: '@NO', 16: 'LAC', 17: '@NE'}}

#%%
#make predictions as to who will win and how many points to put on them

import numpy as np
#random data
#team_data = {'JAC': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 52.87435980765907, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.625, 'PA': 42.204931017453404, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 28, 'L': 6, 'Net Pts': 10.669428790205664, 'W': 10, 'T': 0}, 'CIN': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 43.28356446600784, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0625, 'PA': 33.07707074565975, 'Non-Conf': '0-0', 'Streak': 2, 'TD': 4, 'L': 15, 'Net Pts': 10.206493720348085, 'W': 1, 'T': 0}, 'IND': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 12.509404878538199, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.25, 'PA': 75.3468097809007, 'Non-Conf': '0-0', 'Streak': 0, 'TD': 55, 'L': 12, 'Net Pts': -62.8374049023625, 'W': 4, 'T': 0}, 'SEA': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 64.30606438397878, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.5625, 'PA': 24.437682440589647, 'Non-Conf': '0-0', 'Streak': 10, 'TD': 71, 'L': 7, 'Net Pts': 39.86838194338913, 'W': 9, 'T': 0}, 'MIA': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 87.91874090354852, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 63.0041093316548, 'Non-Conf': '0-0', 'Streak': 7, 'TD': 10, 'L': 3, 'Net Pts': 24.91463157189372, 'W': 13, 'T': 0}, 'ATL': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 68.25993924414338, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.25, 'PA': 31.047014917949145, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 92, 'L': 12, 'Net Pts': 37.21292432619424, 'W': 4, 'T': 0}, 'PHI': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 15.149787593668984, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.3125, 'PA': 22.177406565910474, 'Non-Conf': '0-0', 'Streak': 5, 'TD': 89, 'L': 11, 'Net Pts': -7.0276189722414895, 'W': 5, 'T': 0}, 'SF': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 44.19624615986885, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.125, 'PA': 19.73792206841495, 'Non-Conf': '0-0', 'Streak': 2, 'TD': 86, 'L': 14, 'Net Pts': 24.4583240914539, 'W': 2, 'T': 0}, 'NYG': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 20.451114291238483, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0, 'PA': 38.02605596980951, 'Non-Conf': '0-0', 'Streak': 0, 'TD': 73, 'L': 16, 'Net Pts': -17.57494167857103, 'W': 0, 'T': 0}, 'PIT': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 75.44145806401082, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0625, 'PA': 25.97811731733961, 'Non-Conf': '0-0', 'Streak': 2, 'TD': 81, 'L': 15, 'Net Pts': 49.46334074667121, 'W': 1, 'T': 0}, 'NE': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 73.79153066033584, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.3125, 'PA': 38.73922961220578, 'Non-Conf': '0-0', 'Streak': 0, 'TD': 99, 'L': 11, 'Net Pts': 35.052301048130055, 'W': 5, 'T': 0}, 'WAS': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 96.6687742041372, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.875, 'PA': 34.345760222654995, 'Non-Conf': '0-0', 'Streak': 14, 'TD': 46, 'L': 2, 'Net Pts': 62.3230139814822, 'W': 14, 'T': 0}, 'TEN': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 14.951389417701888, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 64.53747227151499, 'Non-Conf': '0-0', 'Streak': 8, 'TD': 9, 'L': 3, 'Net Pts': -49.586082853813096, 'W': 13, 'T': 0}, 'TB': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 11.721456709920542, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.5, 'PA': 22.706847812823682, 'Non-Conf': '0-0', 'Streak': 0, 'TD': 7, 'L': 8, 'Net Pts': -10.98539110290314, 'W': 8, 'T': 0}, 'DAL': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 30.438623065695992, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.6875, 'PA': 64.39679321212375, 'Non-Conf': '0-0', 'Streak': 6, 'TD': 56, 'L': 5, 'Net Pts': -33.95817014642776, 'W': 11, 'T': 0}, 'CLE': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 59.091505836557744, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 2.3212450303987, 'Non-Conf': '0-0', 'Streak': 9, 'TD': 22, 'L': 3, 'Net Pts': 56.770260806159044, 'W': 13, 'T': 0}, 'DEN': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 28.828170399732755, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 33.94931360100026, 'Non-Conf': '0-0', 'Streak': 6, 'TD': 33, 'L': 3, 'Net Pts': -5.1211432012675075, 'W': 13, 'T': 0}, 'MIN': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 14.373959022207439, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.6875, 'PA': 72.12092249364235, 'Non-Conf': '0-0', 'Streak': 8, 'TD': 49, 'L': 5, 'Net Pts': -57.74696347143492, 'W': 11, 'T': 0}, 'BUF': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 0.5765071186098814, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.1875, 'PA': 39.47988044709155, 'Non-Conf': '0-0', 'Streak': 4, 'TD': 31, 'L': 13, 'Net Pts': -38.90337332848167, 'W': 3, 'T': 0}, 'BAL': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 21.83104564662628, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.75, 'PA': 66.27217566507605, 'Non-Conf': '0-0', 'Streak': 11, 'TD': 98, 'L': 4, 'Net Pts': -44.44113001844977, 'W': 12, 'T': 0}, 'OAK': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 71.91138423689547, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 1.0, 'PA': 74.4825880843894, 'Non-Conf': '0-0', 'Streak': 4, 'TD': 43, 'L': 0, 'Net Pts': -2.5712038474939334, 'W': 16, 'T': 0}, 'HOU': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 53.549484069404315, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.4375, 'PA': 12.67104078329645, 'Non-Conf': '0-0', 'Streak': 6, 'TD': 64, 'L': 9, 'Net Pts': 40.87844328610787, 'W': 7, 'T': 0}, 'GB': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 35.41257631687237, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.125, 'PA': 80.46831918629591, 'Non-Conf': '0-0', 'Streak': 3, 'TD': 43, 'L': 14, 'Net Pts': -45.05574286942355, 'W': 2, 'T': 0}, 'DET': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 46.91166779547425, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.3125, 'PA': 7.577324303522737, 'Non-Conf': '0-0', 'Streak': 5, 'TD': 25, 'L': 11, 'Net Pts': 39.334343491951515, 'W': 5, 'T': 0}, 'CHI': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 16.181474405915573, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.75, 'PA': 34.49411381931993, 'Non-Conf': '0-0', 'Streak': 3, 'TD': 91, 'L': 4, 'Net Pts': -18.312639413404355, 'W': 12, 'T': 0}, 'LAR': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 1.2357985486113998, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.9375, 'PA': 7.378605887822564, 'Non-Conf': '0-0', 'Streak': 15, 'TD': 80, 'L': 1, 'Net Pts': -6.142807339211164, 'W': 15, 'T': 0}, 'NO': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 60.39886659805158, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0, 'PA': 37.19190361462223, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 89, 'L': 16, 'Net Pts': 23.206962983429356, 'W': 0, 'T': 0}, 'LAC': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 3.2938648673589976, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.4375, 'PA': 51.9244731485912, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 94, 'L': 9, 'Net Pts': -48.6306082812322, 'W': 7, 'T': 0}, 'CAR': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 39.4050015379659, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.375, 'PA': 43.947706931168064, 'Non-Conf': '0-0', 'Streak': 3, 'TD': 24, 'L': 10, 'Net Pts': -4.542705393202162, 'W': 6, 'T': 0}, 'KC': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 10.58482182602022, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.8125, 'PA': 97.30023618867429, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 27, 'L': 3, 'Net Pts': -86.71541436265407, 'W': 13, 'T': 0}, 'ARI': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 93.11526655058593, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.0625, 'PA': 39.51864995749621, 'Non-Conf': '0-0', 'Streak': 1, 'TD': 51, 'L': 15, 'Net Pts': 53.59661659308972, 'W': 1, 'T': 0}, 'NYJ': {'Pct_Div': '.000', 'Pct_Conf': '.000', 'PF': 70.26475529821165, 'Conf': '0-0', 'Home': '0-0', 'Last 5': '0-0', 'Road': '0-0', 'Div': '0-0', 'Pct': 0.9375, 'PA': 40.22974377964914, 'Non-Conf': '0-0', 'Streak': 9, 'TD': 29, 'L': 1, 'Net Pts': 30.035011518562513, 'W': 15, 'T': 0}}
#saved output:       
#team_schedule={'CIN': {1: 'BAL', 2: 'HOU', 3: '@GB', 4: '@CLE', 5: 'BUF', 6: 'BYE', 7: '@PIT', 8: 'IND', 9: '@JAC', 10: '@TEN', 11: '@DEN', 12: 'CLE', 13: 'PIT', 14: 'CHI', 15: '@MIN', 16: 'DET', 17: '@BAL'}, 'IND': {1: '@LAR', 2: 'ARI', 3: 'CLE', 4: '@SEA', 5: 'SF', 6: '@TEN', 7: 'JAC', 8: '@CIN', 9: '@HOU', 10: 'PIT', 11: 'BYE', 12: 'TEN', 13: '@JAC', 14: '@BUF', 15: 'DEN', 16: '@BAL', 17: 'HOU'}, 'SEA': {1: '@GB', 2: 'SF', 3: '@TEN', 4: 'IND', 5: '@LAR', 6: 'BYE', 7: '@NYG', 8: 'HOU', 9: 'WAS', 10: '@ARI', 11: 'ATL', 12: '@SF', 13: 'PHI', 14: '@JAC', 15: 'LAR', 16: '@DAL', 17: 'ARI'}, 'MIA': {1: 'TB', 2: '@LAC', 3: '@NYJ', 4: 'NO', 5: 'TEN', 6: '@ATL', 7: 'NYJ', 8: '@BAL', 9: 'OAK', 10: '@CAR', 11: 'BYE', 12: '@NE', 13: 'DEN', 14: 'NE', 15: '@BUF', 16: '@KC', 17: 'BUF'}, 'ATL': {1: '@CHI', 2: 'GB', 3: '@DET', 4: 'BUF', 5: 'BYE', 6: 'MIA', 7: '@NE', 8: '@NYJ', 9: '@CAR', 10: 'DAL', 11: '@SEA', 12: 'TB', 13: 'MIN', 14: 'NO', 15: '@TB', 16: '@NO', 17: 'CAR'}, 'PHI': {1: '@WAS', 2: '@KC', 3: 'NYG', 4: '@LAC', 5: 'ARI', 6: '@CAR', 7: 'WAS', 8: 'SF', 9: 'DEN', 10: 'BYE', 11: '@DAL', 12: 'CHI', 13: '@SEA', 14: '@LAR', 15: '@NYG', 16: 'OAK', 17: 'DAL'}, 'SF': {1: 'CAR', 2: '@SEA', 3: 'LAR', 4: '@ARI', 5: '@IND', 6: '@WAS', 7: 'DAL', 8: '@PHI', 9: 'ARI', 10: 'NYG', 11: 'BYE', 12: 'SEA', 13: '@CHI', 14: '@HOU', 15: 'TEN', 16: 'JAC', 17: '@LAR'}, 'NYG': {1: '@DAL', 2: 'DET', 3: '@PHI', 4: '@TB', 5: 'LAC', 6: '@DEN', 7: 'SEA', 8: 'BYE', 9: 'LAR', 10: '@SF', 11: 'KC', 12: '@WAS', 13: '@OAK', 14: 'DAL', 15: 'PHI', 16: '@ARI', 17: 'WAS'}, 'PIT': {1: '@CLE', 2: 'MIN', 3: '@CHI', 4: '@BAL', 5: 'JAC', 6: '@KC', 7: 'CIN', 8: '@DET', 9: 'BYE', 10: '@IND', 11: 'TEN', 12: 'GB', 13: '@CIN', 14: 'BAL', 15: 'NE', 16: '@HOU', 17: 'CLE'}, 'NE': {1: 'KC', 2: '@NO', 3: 'HOU', 4: 'CAR', 5: '@TB', 6: '@NYJ', 7: 'ATL', 8: 'LAC', 9: 'BYE', 10: '@DEN', 11: '@OAK', 12: 'MIA', 13: '@BUF', 14: '@MIA', 15: '@PIT', 16: 'BUF', 17: 'NYJ'}, 'WAS': {1: 'PHI', 2: '@LAR', 3: 'OAK', 4: '@KC', 5: 'BYE', 6: 'SF', 7: '@PHI', 8: 'DAL', 9: '@SEA', 10: 'MIN', 11: '@NO', 12: 'NYG', 13: '@DAL', 14: '@LAC', 15: 'ARI', 16: 'DEN', 17: '@NYG'}, 'JAC': {1: '@HOU', 2: 'TEN', 3: 'BAL', 4: '@NYJ', 5: '@PIT', 6: 'LAR', 7: '@IND', 8: 'BYE', 9: 'CIN', 10: 'LAC', 11: '@CLE', 12: '@ARI', 13: 'IND', 14: 'SEA', 15: 'HOU', 16: '@SF', 17: '@TEN'}, 'TB': {1: '@MIA', 2: 'CHI', 3: '@MIN', 4: 'NYG', 5: 'NE', 6: '@ARI', 7: '@BUF', 8: 'CAR', 9: '@NO', 10: 'NYJ', 11: 'BYE', 12: '@ATL', 13: '@GB', 14: 'DET', 15: 'ATL', 16: '@CAR', 17: 'NO'}, 'TEN': {1: 'OAK', 2: '@JAC', 3: 'SEA', 4: '@HOU', 5: '@MIA', 6: 'IND', 7: '@CLE', 8: 'BYE', 9: 'BAL', 10: 'CIN', 11: '@PIT', 12: '@IND', 13: 'HOU', 14: '@ARI', 15: '@SF', 16: 'LAR', 17: 'JAC'}, 'DAL': {1: 'NYG', 2: '@DEN', 3: '@ARI', 4: 'LAR', 5: 'GB', 6: 'BYE', 7: '@SF', 8: '@WAS', 9: 'KC', 10: '@ATL', 11: 'PHI', 12: 'LAC', 13: 'WAS', 14: '@NYG', 15: '@OAK', 16: 'SEA', 17: '@PHI'}, 'CLE': {1: 'PIT', 2: '@BAL', 3: '@IND', 4: 'CIN', 5: 'NYJ', 6: '@HOU', 7: 'TEN', 8: 'MIN', 9: 'BYE', 10: '@DET', 11: 'JAC', 12: '@CIN', 13: '@LAC', 14: 'GB', 15: 'BAL', 16: '@CHI', 17: '@PIT'}, 'DEN': {1: 'LAC', 2: 'DAL', 3: '@BUF', 4: 'OAK', 5: 'BYE', 6: 'NYG', 7: '@LAC', 8: '@KC', 9: '@PHI', 10: 'NE', 11: 'CIN', 12: '@OAK', 13: '@MIA', 14: 'NYJ', 15: '@IND', 16: '@WAS', 17: 'KC'}, 'MIN': {1: 'NO', 2: '@PIT', 3: 'TB', 4: 'DET', 5: '@CHI', 6: 'GB', 7: 'BAL', 8: '@CLE', 9: 'BYE', 10: '@WAS', 11: 'LAR', 12: '@DET', 13: '@ATL', 14: '@CAR', 15: 'CIN', 16: '@GB', 17: 'CHI'}, 'BUF': {1: 'NYJ', 2: '@CAR', 3: 'DEN', 4: '@ATL', 5: '@CIN', 6: 'BYE', 7: 'TB', 8: 'OAK', 9: '@NYJ', 10: 'NO', 11: '@LAC', 12: '@KC', 13: 'NE', 14: 'IND', 15: 'MIA', 16: '@NE', 17: '@MIA'}, 'BAL': {1: '@CIN', 2: 'CLE', 3: '@JAC', 4: 'PIT', 5: '@OAK', 6: 'CHI', 7: '@MIN', 8: 'MIA', 9: '@TEN', 10: 'BYE', 11: '@GB', 12: 'HOU', 13: 'DET', 14: '@PIT', 15: '@CLE', 16: 'IND', 17: 'CIN'}, 'OAK': {1: '@TEN', 2: 'NYJ', 3: '@WAS', 4: '@DEN', 5: 'BAL', 6: 'LAC', 7: 'KC', 8: '@BUF', 9: '@MIA', 10: 'BYE', 11: 'NE', 12: 'DEN', 13: 'NYG', 14: '@KC', 15: 'DAL', 16: '@PHI', 17: '@LAC'}, 'HOU': {1: 'JAC', 2: '@CIN', 3: '@NE', 4: 'TEN', 5: 'KC', 6: 'CLE', 7: 'BYE', 8: '@SEA', 9: 'IND', 10: '@LAR', 11: 'ARI', 12: '@BAL', 13: '@TEN', 14: 'SF', 15: '@JAC', 16: 'PIT', 17: '@IND'}, 'GB': {1: 'SEA', 2: '@ATL', 3: 'CIN', 4: 'CHI', 5: '@DAL', 6: '@MIN', 7: 'NO', 8: 'BYE', 9: 'DET', 10: '@CHI', 11: 'BAL', 12: '@PIT', 13: 'TB', 14: '@CLE', 15: '@CAR', 16: 'MIN', 17: '@DET'}, 'DET': {1: 'ARI', 2: '@NYG', 3: 'ATL', 4: '@MIN', 5: 'CAR', 6: '@NO', 7: 'BYE', 8: 'PIT', 9: '@GB', 10: 'CLE', 11: '@CHI', 12: 'MIN', 13: '@BAL', 14: '@TB', 15: 'CHI', 16: '@CIN', 17: 'GB'}, 'CHI': {1: 'ATL', 2: '@TB', 3: 'PIT', 4: '@GB', 5: 'MIN', 6: '@BAL', 7: 'CAR', 8: '@NO', 9: 'BYE', 10: 'GB', 11: 'DET', 12: '@PHI', 13: 'SF', 14: '@CIN', 15: '@DET', 16: 'CLE', 17: '@MIN'}, 'NO': {1: '@MIN', 2: 'NE', 3: '@CAR', 4: '@MIA', 5: 'BYE', 6: 'DET', 7: '@GB', 8: 'CHI', 9: 'TB', 10: '@BUF', 11: 'WAS', 12: '@LAR', 13: 'CAR', 14: '@ATL', 15: 'NYJ', 16: 'ATL', 17: '@TB'}, 'LAC': {1: '@DEN', 2: 'MIA', 3: 'KC', 4: 'PHI', 5: '@NYG', 6: '@OAK', 7: 'DEN', 8: '@NE', 9: 'BYE', 10: '@JAC', 11: 'BUF', 12: '@DAL', 13: 'CLE', 14: 'WAS', 15: '@KC', 16: '@NYJ', 17: 'OAK'}, 'LAR': {1: 'IND', 2: 'WAS', 3: '@SF', 4: '@DAL', 5: 'SEA', 6: '@JAC', 7: 'ARI', 8: 'BYE', 9: '@NYG', 10: 'HOU', 11: '@MIN', 12: 'NO', 13: '@ARI', 14: 'PHI', 15: '@SEA', 16: '@TEN', 17: 'SF'}, 'CAR': {1: '@SF', 2: 'BUF', 3: 'NO', 4: '@NE', 5: '@DET', 6: 'PHI', 7: '@CHI', 8: '@TB', 9: 'ATL', 10: 'MIA', 11: 'BYE', 12: '@NYJ', 13: '@NO', 14: 'MIN', 15: 'GB', 16: 'TB', 17: '@ATL'}, 'KC': {1: '@NE', 2: 'PHI', 3: '@LAC', 4: 'WAS', 5: '@HOU', 6: 'PIT', 7: '@OAK', 8: 'DEN', 9: '@DAL', 10: 'BYE', 11: '@NYG', 12: 'BUF', 13: '@NYJ', 14: 'OAK', 15: 'LAC', 16: 'MIA', 17: '@DEN'}, 'ARI': {1: '@DET', 2: '@IND', 3: 'DAL', 4: 'SF', 5: '@PHI', 6: 'TB', 7: '@LAR', 8: 'BYE', 9: '@SF', 10: 'SEA', 11: '@HOU', 12: 'JAC', 13: 'LAR', 14: 'TEN', 15: '@WAS', 16: 'NYG', 17: '@SEA'}, 'NYJ': {1: '@BUF', 2: '@OAK', 3: 'MIA', 4: 'JAC', 5: '@CLE', 6: 'NE', 7: '@MIA', 8: 'ATL', 9: 'BUF', 10: '@TB', 11: 'BYE', 12: 'CAR', 13: 'KC', 14: '@DEN', 15: '@NO', 16: 'LAC', 17: '@NE'}}

results = []
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

filename = "/home/hpeter/Documents/Football/picks_week{}.tex".format(week)
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
    f.write("{\\large Henry Peterson } \\par\n")
    #colomn spacing
    f.write("\\setlength{\\tabcolsep}{2em}\n")
    #row spacing
    f.write("{\\renewcommand{\\arraystretch}{2}\n")
    #put picks in table
    f.write("\\begin{tabular}{ l l }\n")
    for r in results:
        #box the winner and put match/bet in separate columns
        if r["Winner"] == r["Home"]:
            f.write(r["Away"] + " @ $\\boxed{ \\text{" + r["Home"] + \
                  "} }$ & " + r["Bet"] + " \\\ \n")
        else:
            f.write("$\\boxed{ \\text{" + r["Away"] + "} }$ @ " + \
                    r["Home"] + " & " + r["Bet"] + " \\\ \n")
    #end (don't forget row spacing end)
    f.write("\\end{tabular}}\n")
    f.write("\\end{document}\n")


os.system("pdflatex -output-directory /home/hpeter/Documents/Football/ {}".format(filename))

to = "cptrsn@comcast.net"
cc = "slptrsn@gmail.com,stv.ptrsn9@gmail.com"
subject = "Picks Week " + str(week)
body = "Here are my picks.\n\nHP"
attachment = "/home/hpeter/Documents/Football/picks_week" + str(week) + ".pdf"
os.system("thunderbird -compose \"to='{}',cc='{}',subject='{}',body='{}',attachment='{}'\"".format(to,cc,subject,body,attachment))


