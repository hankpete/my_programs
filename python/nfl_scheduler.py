## read website to get nfl schedules for the year
## make latex pdf for the family to use in picks

#12-24-16

#%%
import urllib
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
            week = html_str[i:j]

        text += "\n\\newpage \\section*{\\LARGE Football Picks " + year + ": " + html_str[i:j] + "}"
    
    elif html_str[i:i+4] == "<td>":
        #new element of list (matchup, time, day)
        j = i + 4
        while html_str[j] != "<":   
            #go until content done
            j += 1
        for time in ["a<","pm<"]:
            #gametime, convert to pacific
            if time in html_str[i+4:j+1]:
                k = i + 4
                while html_str[k] != ":":
                    k += 1
                try:
                    pacific_time = int(html_str[i+4:k]) - 3 
                    if pacific_time == 0:
                        pacific_time = str(12) + html_str[k:j] 
                    elif pacific_time < 0:
                        pacific_time = str(pacific_time % 12) + html_str[k:j-2] + "am"
                    else:
                        pacific_time = str(pacific_time) + html_str[k:j]
                    text += " (" + pacific_time + ")\\par"
                except:
                    continue
        for day in days:
            #new day, make title
            if day in html_str[i+4:j]: 
                text += "\n\\noindent \\normalsize \\textbf{" + html_str[i+4:j] + "} \\par"
        if " at " in html_str[i+4:j]:
            #new matchup
            text += "\n" + html_str[i+4:j].replace(" at ", " @ ")
        elif "Byes" in html_str[i+4:j]:
            #put the byes at the bottom
            text += "\n\\vfill{}"
            text += "\n" + html_str[i+4:j].replace(";", " ").replace(",", ", ")


                
#put it all in a tex file
with open("nfl_schedule.tex","w") as f:
    f.write(
"""
\\documentclass[11pt, letterpaper]{article}
\\usepackage[margin=0.9in]{geometry}
\\usepackage[scaled]{helvet}
\\renewcommand\\familydefault{\\sfdefault} 
\\usepackage[T1]{fontenc}
\\pagestyle{empty}
\\begin{document}
\\setlength{\parindent}{0.5em}
\\setlength{\parskip}{1.4em}
"""
    )
    f.write(text)
    f.write("\\end{document}")

#%%
#make it
os.system("pdflatex nfl_schedule.tex")