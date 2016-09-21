import csv

with open('gamers.csv', 'r') as gamerFile:

    gfreader = csv.reader(gamerFile)

    for line in gfreader:
        scoreList = []
        scoreList.append(line)
        print(type(line))


    highscore = 0


    for g in scoreList:
        print('ss')
        if highscore < eval(g[2]):
            highscore = eval(g[2])

    for g in scoreList:
        if highscore == g[2]:
            print('De hoogste score is: {} op {} behaald door {}'.format(g[2],g[0].g[1]))

    gamerFile.close()



