
while True:
    try:
        global leeftijd
        leeftijd = int(input('Geef je leeftijd: '))
        break
    except ValueError:
        print('Aleen cijfers')

while True:
    global paspoort
    paspoort = str(input('Nerderlands paspoort(ja/nee); '))
    if paspoort == 'ja' or paspoort =='nee':
        break
    else:
        print('Aleen ja of nee')


if leeftijd >= 18:
    if paspoort == 'ja':
        print('Gefeliciteerd, je mag stemmen!')
    else:
        print('Helaas, je mag niet stemmen')
else:
    print('Helaas, je mag niet stemmen')