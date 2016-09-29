from xml.etree import ElementTree
import xmltodict

stations = ElementTree.parse('Stations.xml')



code = stations.findall('Station/Code')
type = stations.findall('Station/Type')
naamL = stations.findall('Station/Namen/Lang')
naamM = stations.findall('Station/Namen/Middel')
naamK = stations.findall('Station/Namen/Kort')
land = stations.findall('Station/Land')
syno = stations.findall('Station/Synoniemen/Synoniem')

print(len(syno))

'''
print('Dit zijn de codes, types en landcodes van de 4 stations:')
for c, t, l in zip(code,type,land):
    s = '{} - {} - {}'.format(c.text,t.text,l.text)
    print(s)
'''


testStr = ''
print('\nDit zijn alle stations met een of meer synoniemen:')
for c in code:
    print(c.text, end=' - ')
    tst = ''
    for synoniem in syno:
        if synoniem is not None:
            tst = tst + synoniem.text + ' '
            print(tst)


'''
print('\nDit is de lange naam van elk station:')
for c, n in zip(code,naamL):
    s = '{} - {}'.format(c.text,n.text)
    print(s)

print('\nDit is de middellange naam van elk station:')
for c, n in zip(code,naamM):
    s = '{} - {}'.format(c.text,n.text)
    print(s)

print('\nDit is de korte naam van elk station:')
for c, n in zip(code,naamK):
    s = '{} - {}'.format(c.text,n.text)
    print(s)
'''