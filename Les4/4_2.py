file = open('Kaartnummers.txt', 'r')

def fileReader():
    for line in file:
        quickList = line.split(sep=',')
        quickList[1] = quickList[1].rstrip('\n')
        print('{} heeft kaartnummer: {}'.format(quickList[1],quickList[0]))

fileReader()
file.close()