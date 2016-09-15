file = open('Kaartnummers.txt', 'r')

def fileReader():
    for line in file:
        quickList = line.split(sep=',')
        quickList[1] = quickList[1].rstrip('\n')
        print(quickList[1]+' heeft kaartnummer: '+str(quickList[0]))

fileReader()
file.close()