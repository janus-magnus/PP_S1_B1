import csv

with open('gamers.csv', 'r') as gamerFile:
    gfreader = csv.reader(gamerFile)
    gamerList = []

    for line in gfreader:
        gamerList.append(line[0].split(sep=';'))

    print(len(gamerList))
    print(gamerList)
    highscore = 0

    for g in gamerList:
        print('hscore:'+ str(highscore))
        print('G2:'+g[2])
        if highscore < eval(g[2]):
            highscore = eval(g[2])
            print('hscore:' + str(highscore)+'\n')

    for g in gamerList:
        if highscore == eval(g[2]):
            name = g[0]
            datum = g[1]
            print('De hoogste score is: {} op {} behaald door {}'.format(highscore,datum,name))

    gamerFile.close()



