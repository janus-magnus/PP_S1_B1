stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', "s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']


def inlezen_beginpunt():
    while True:
        beginStation = input('Wat is je beginstation?: ')
        if beginStation in stations:
            return beginStation
        else:
            print('Deze trein komt niet in {}'.format(beginStation))

def inlezen_eindpunt(begin):
    while True:
        eindStation = input('Wat is je eindstation?: ')
        if eindStation in stations:
            if stations.index(begin) < stations.index(eindStation):
                return  eindStation
            else:
                print('Het eindstation mag niet voor het beginstation staan')
        else:
            print('Deze trein komt niet in {}'.format(eindStation))

def omroepen_reis(begin, eind):
    bIndex = stations.index(begin)
    bSNum = bIndex + 1
    eIndex = stations.index(eind)
    eSNum = eIndex + 1
    sAfstand = eIndex - bIndex
    prijs = 5 * sAfstand

    print(
        'Het beginstation {} is station nummer {} station in het traject \nHet eindstation {} is station nummer {} station in het traject \nDe afstand is {} station(s) '
        '\nDe prijs van het kaartje is {} euro. \nJij stapt in de trein op: {}'.format(begin, bSNum, eind,
                                                                                       eSNum, sAfstand, prijs,
                                                                                       begin))
    for i in range(bIndex + 1, eIndex, 1):
        print('-' + str(stations[i]))

    print('Jij stapt uit op: {}'.format(eind))

begin = inlezen_beginpunt()
eind = inlezen_eindpunt()
omroepen_reis(begin, eind)

