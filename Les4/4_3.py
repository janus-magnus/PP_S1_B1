file = open('Kaartnummers.txt', 'r')

def fileReader():
    lineList = []
    lineCounter = 0
    for line in file:
        lineCounter+=1
        quickList = line.split(sep=', ')
        lineList.append(quickList[0])
    print('Deze file telt {} regels'.format(lineCounter))

    maxNum = max(lineList)
    maxNumLine = lineList.index(max(lineList))+1
    print('het grootste kaartnummer is: {} en dat staat op regel {}'.format(maxNum,maxNumLine))
    file.close()

fileReader()

