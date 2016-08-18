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


def makeBook():
    pageContent = ""
    # loop
    for i in range(pagesPerBook):
        for j in range(linesPerPage):
            pageContent += str(i*(linesPerPage+6) + j + 1) + " "
            for k in range(letsPerLine):
                pageContent += lets[ r.randrange( numLets ) ]
            pageContent += "\n"
        pageContent += "\n\n\n------------------------------------------\n\n\n"

    # open file
    file = open("libOfBabPage.txt", "w")
    file.write(pageContent)
    file.close()

def findWords():
    # now to check for words
    wordBank = []
    with open("words.txt", "r") as f:
        for word in f:
            if len(word)>4:
                wordBank.append(word)
                
    with open("libOfBabPage.txt", "r") as f:
        lines = f.readlines()
 
    for word in wordBank:
        for line in lines:
            if word in line:
                print(word + " can be found on line " + str(lines.index(line)))

def debug():
    wordBank = []
    with open("words.txt", "r") as f:
        for word in f:
            if len(word)>4:
                print(word.remove("\n")
    
    
    
# run 
#makeBook()
#findWords()
debug()
