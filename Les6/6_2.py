


def ticker(filename):
    tickerFile = open(filename, 'r')

    quicklist = []
    tickerDict = {}

    for line in tickerFile:
        quicklist = line.split(sep=':')
        tickerDict[quicklist[0].strip()] = quicklist[1].strip()

    print(tickerDict)
    return tickerDict

def search(dict):
    bedrijfName = input('Voer bedrijfsnaam in: ').upper()

    print(dict[bedrijfName])

    bedrijfTick = input('Voer Ticker symbool in: ').upper()

    for k in dict.keys():
        print(dict[k])
        if dict[k] == bedrijfTick:
            print(k)


search(ticker('Ticker.txt'))