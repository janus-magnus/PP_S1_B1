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

    print(anulList)
    for rit in ritList:
        geannuleerd = False
        for anul in anulList:
            if anul in rit:
                geannuleerd = True

        if not geannuleerd:
            herzienFile.write(str(rit) + '\n')
    anulFile.close()
    herzienFile.close()
    ritenFile.close()


herzien()