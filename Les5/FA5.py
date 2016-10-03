stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', "s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']

def station():

    while True:
        beginStation = input('Wat is je beginstation?: ').capitalize()
        if beginStation in stations:
            break
        else:
            print('Deze trein komt niet in {}'.format(beginStation))

    while True:
        eindStation = input('Wat is je eindstation?: ').capitalize()
        if eindStation in stations:
            break
        else:
            print('Deze trein komt niet in {}'.format(eindStation))

    bIndex = stations.index(beginStation)
    bSNum = bIndex + 1
    eIndex = stations.index(eindStation)
    eSNum = eIndex + 1
    sAfstand = eIndex - bIndex
    prijs = 5 * sAfstand

    print('Het beginstation {} is station nummer {} station in het traject \nHet eindstation {} is station nummer {} station in het traject \nDe afstand is {} station(s) '
              '\nDe prijs van het kaartje is {} euro. \nJij stapt in de trein op: {}'.format(beginStation, bSNum, eindStation, eSNum, sAfstand, prijs, beginStation))

    for i in range(bIndex + 1, eIndex, 1):
        print('-' + str(stations[i]))

    print('Jij stapt uit op: {}'.format(eindStation))

station()