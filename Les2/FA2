stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', "s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

bStation = str(input('Wat is je beginstation?: '))

if bStation not in stations:
    print('Dit station is niet geldig, beginstation is: Schagen')
    bStation = 'Schagen'

bIndex = stations.index(bStation)
bSNum = bIndex+1

eStation = str(input('Wat is je eindstation?: '))

if eStation not in stations:
    print('Dit station is niet geldig, eindstation is: Maastricht')
    eStation = 'Maastricht'

eIndex = stations.index(eStation)
eSNum = eIndex+1
sAfstand = eIndex-bIndex

print('Het beginstation ' + str(bStation) + 'is station nummer ' + str(bSNum) + ' station in het traject')
print('Het eindstation ' + str(eStation) + 'is station nummer ' + str(eSNum) + ' station in het traject')
print('De afstand is ' + str(sAfstand) + ' station(s)')
print('De prijs van het kaartje is ' + str(5 * sAfstand) +' euro.')
print('Jij stapt in de trein op: ' + bStation)


for i in range(bIndex+1,eIndex,1):
    print('-' + str(stations[i]) )
    i+=1

print('Jij stapt uit op: ' + eStation)





