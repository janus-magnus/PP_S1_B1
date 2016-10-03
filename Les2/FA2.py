
stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', "s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']

while True:
    beginStation = input('Wat is je beginstation?: ').capitalize()
    print(beginStation)
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
bSNum = bIndex+1
eIndex = stations.index(eindStation)
eSNum = eIndex+1
sAfstand = eIndex-bIndex

print('Het beginstation {} is station nummer {} station in het traject'.format(beginStation,bSNum))
print('Het eindstation  {} is station nummer {} station in het traject'.format(eindStation,eSNum))
print('De afstand is {} station(s)'.format(sAfstand))
print('De prijs van het kaartje is {} euro.'.format(str(5 * sAfstand)))
print('Jij stapt in de trein op: {}'.format(beginStation))


for i in range(bIndex+1,eIndex,1):
    print('-' + str(stations[i]) )


print('Jij stapt uit op: {}'.format(eindStation))





