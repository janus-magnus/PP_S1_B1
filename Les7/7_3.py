import csv

with open('gamers.csv', 'r') as gamerFile:

    gfreader = csv.reader(gamerFile)

    for line in gfreader:
        gamerList = []
        gamerList.append(line[0].split(sep=';'))
 #       print(line[0].split(sep=';'))
        print(len(gamerList))

    highscore = 0

    for g in gamerList:
        print(highscore)
       # if highscore < eval(g[2]):
        #    highscore = eval(g[2])

 #   print(highscore)

    for g in gamerList:
  #      print(len(gamerList))
  #      print(g[2])
        if highscore == g[2]:
            print('De hoogste score is: {} op {} behaald door {}'.format(g[2],g[0].g[1]))

    gamerFile.close()



