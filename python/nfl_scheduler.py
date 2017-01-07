## read website to get nfl schedules for the year
## make latex pdf for the family to use in picks

#12-24-16

#%%
import urllib
import os

#%%
year = "2016"
site = "http://www.thehuddle.com/" + year + "/nfl/nfl-schedule-wk-txt.php"

with urllib.request.urlopen(site) as response:
   html = response.read()

#it comes as character codes. turn into letters
html_str = ""
for i in html:
    html_str += str(chr(i))
   
#print(html_str)

#%%
#find the part in the html with tables of schedules
#add just those to a text string 

#lists for checking 
weeks = []
for i in range(17):
    weeks.append("Week " + str(i+1))
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

text = ""
for i in range( len(html_str) ):
    if html_str[i:i+6] in weeks or html_str[i:i+7] in weeks:
        #new week, new page
        j = i + 5
        while html_str[j] != "<":
            j += 1
        #text += "\n\\newpage \\title{Football Picks: " + html_str[i:j] + "} \\date{" + year + "} \\maketitle"
        text += "\n\\newpage \\section*{\\Huge Football Picks " + year + ": " + html_str[i:j] + "}"
    
    elif html_str[i:i+4] == "<td>":
        #new element of list (matchup, time, day)
        if html_str[i+4] == "&":
            continue
        j = i + 4
        while html_str[j] != "<" and html_str[j] != "\n" and html_str[j] != "&":
            j += 1
        for time in ["a.m.","p.m."]:
            if time in html_str[i+4:j]:
                text += " " + html_str[i+4:j] +"\\par"
        for day in days:
            if day in html_str[i+4:j]: 
                text += "\n\\noindent \\Large \\textbf{" + html_str[i+4:j] + "} \\par"
        if "at" in html_str[i+4:j]:
            text += "\n" + html_str[i+4:j]

                
#put it all in a tex file
with open("nfl_schedule.tex","w") as f:
    f.write(
"""
\\documentclass[12pt, letterpaper]{article}
\\usepackage[margin=1in]{geometry}
\\usepackage[scaled]{helvet}
\\renewcommand\\familydefault{\\sfdefault} 
\\usepackage[T1]{fontenc}
\\pagenumbering{gobble}
\\begin{document}
\\setlength{\parindent}{2em}
\\setlength{\parskip}{0.75em}
"""
    )
    f.write(text)
    f.write("\\end{document}")

#%%
#make it
os.system("pdflatex nfl_schedule.tex")