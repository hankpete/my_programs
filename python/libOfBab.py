# a page out of one of the books in
# library of babylon

# 08/15/16 HGP

import random as r

# vars
pagesPerBook = 410
letsPerLine = 80
linesPerPage = 40
lets = "qwertyuiopasdfghjklzxcvbnm,. "
#lets = "אבגדהוזחטיכךלמםנןסעפףצץקרשת,. "
numLets = len(lets)
pageContent = ""

# loop
for i in range(pagesPerBook):
    for j in range(linesPerPage):
        for k in range(letsPerLine):
            pageContent += lets[ r.randrange( numLets ) ]
        pageContent += "\n"
    pageContent += "\n\n\n------------------------------------------\n\n\n"

# open file
file = open("libOfBabPage.txt", "w")
file.write(pageContent)
file.close()
        
