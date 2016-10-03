import xmltodict

with open('Stations.xml','r') as stationXML:
    stationContent = stationXML.read()
    stationDict = xmltodict.parse(stationContent)

stations =  stationDict['Stations']['Station']


print('Dit zijn de codes, types en landcodes van de 4 stations:')
for stat in stations:
    s = '{} - {} - {}'.format(stat['Code'],stat['Type'],stat['Land'])
    print(s)

print('\nDit zijn alle stations met een of meer synoniemen:')
for stat in stations:
    if stat['Synoniemen'] is not None:
        print('{} - {}'.format(stat['Code'], stat['Synoniemen']['Synoniem']))

print('\nDit is de lange naam van elk station:')
for stat in stations:
    s = '{} - {}'.format(stat['Code'],stat['Namen']['Lang'])
    print(s)

print('\nDit is de middellange naam van elk station:')
for stat in stations:
    s = '{} - {}'.format(stat['Code'],stat['Namen']['Middel'])
    print(s)

print('\nDit is de korte naam van elk station:')
for stat in stations:
    s = '{} - {}'.format(stat['Code'],stat['Namen']['Kort'])
    print(s)
