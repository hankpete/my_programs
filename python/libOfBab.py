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
            word = word.replace("\n", "")
            if len(word)>=5:
                wordBank.append(word)
                
    with open("libOfBabPage.txt", "r") as f:
        lines = f.readlines()
 
    for word in wordBank:
        for line in lines:
            if word in line:
                print(word + " can be found on line " + str(lines.index(line) + 1))

def makeWordBook():
    letterCount = 0
    lineCount = 0
    pageCount = 0
    pageContent = ""
    # loop
    wordBank = []
    with open("words.txt", "r") as f:
        for word in f:
            word = word.replace("\n", "")
            wordBank.append(word)
    while pageCount < 410:
        newWord = wordBank[ r.randrange(len(wordBank)) ]
        letterCount += len(newWord)
        if letterCount > 80:
            letterCount = 0
            pageContent += "\n"
            lineCount += 1
        if lineCount > 40:
            lineCount = 0
            pageContent += "\n\n\n------------------------------------------\n\n\n"
            pageCount += 1
        pageContent += newWord + " "
    with open("wordBook.txt", "w") as f:
        f.write(pageContent)
         
# run 
#makeBook()
#findWords()
makeWordBook()
