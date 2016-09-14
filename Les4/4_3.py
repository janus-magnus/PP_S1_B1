file = open('Kaartnummers.txt', 'r')




def fileReader():
    lineCounter = 0
    for line in file:
        lineCounter+=1
    print('Deze file telt ' + str(lineCounter) + ' regels')


fileReader()

