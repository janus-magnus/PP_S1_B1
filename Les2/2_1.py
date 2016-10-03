while True:
    uurloonIn = input('Wat verdien je per uur: ')
    try:
        global uurloon
        uurloon = float(uurloonIn)
        break
    except ValueError:
        print('voer alleen cijfers in')

while True:
    uurenGewerktIn = input('Hoeveel uur heb je gewerkt: ')
    try:
        global uurenGewerkt
        uurenGewerkt = float(uurenGewerktIn)
        break
    except ValueError:
        print('voer alleen cijfers in')

loon = uurloon * uurenGewerkt
print(str(uurenGewerkt) + ' uur werken levert ' + str(loon) + '  Euro op')


