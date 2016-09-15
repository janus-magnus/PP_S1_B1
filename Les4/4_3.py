file = open('Kaartnummers.txt', 'r')




def fileReader():
    lineList = []
    lineCounter = 0
    for line in file:
        lineCounter+=1
        quickList = line.split(sep=', ')
        lineList.append(quickList[0])
    print('Deze file telt ' + str(lineCounter) + ' regels')


    maxNum = max(lineList)
    maxLine = lineList.index(max(lineList))+1
    print('het grootste kaartnummer is: '+str(maxNum)+' en dat staat op regel '+
    str(maxLine))
    file.close()


fileReader()

