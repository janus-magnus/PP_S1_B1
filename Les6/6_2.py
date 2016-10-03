def ticker(filename):
    tickerFile = open(filename, 'r')
    tickerDict = {}

    for line in tickerFile:
        quicklist = line.split(sep=':')#de waardes van de line wordt hier tijdelijk opgeslagen in lijst
        tickerDict[quicklist[0].strip()] = quicklist[1].strip()
    print(tickerDict)# dit print statement de Dict in de console zodat de test makelijker uitvoerbaar is
    return tickerDict

def search(dict):
    bedrijfName = input('Voer bedrijfsnaam in: ')

    print(dict[bedrijfName])

    bedrijfTick = input('Voer Ticker symbool in: ').upper()

    for k in dict.keys():
        if dict[k] == bedrijfTick:
            print(k)

search(ticker('Ticker.txt'))