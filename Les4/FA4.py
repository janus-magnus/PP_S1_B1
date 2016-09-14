anulFile = open('anul.txt','r')
ritenFile = open('riten.txt','r')
herzienFile = open('herzienRit.txt','w')



def herzien():
    anulList = []
    for line in anulFile:
        quickList = line.split(sep=': ')
        anulList.append(quickList[1].strip('\n'))

    ritList = []
    for line in ritenFile:
        ritList.append(line.strip('\n'))

    for rit in ritList:
        for anul in anulList:
            if anul not in rit:
                herzienFile.write(str(rit)+'\n')


#print(anulList())
#print(ritList())

herzien()