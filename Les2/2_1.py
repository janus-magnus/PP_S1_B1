import sys
uurloonIn = input('Wat verdien je per uur: ')

try:
    uurloon = float(uurloonIn)
except ValueError:
    print('voer alleen cijfers in')
    sys.exit('begin opnieuw')

uurenGewerktIn = input('Hoeveel uur heb je gewerkt: ')

try:
    uurenGewerkt = float(uurenGewerktIn)
except ValueError:
    print('voer alleen cijfers in')
    sys.exit('begin opnieuw')

loon = uurloon * uurenGewerkt
print(str(uurenGewerkt) + ' uur werken levert ' + str(loon) + '  Euro op')