leeftijd = int(input('Geef je leeftijd: '))
paspoort = str(input('Nerderlands paspoort(ja/nee); '))

if leeftijd >= 18:
    if paspoort == 'ja':
        print('Gefeliciteerd, je mag stemmen!')
    else:
        print('Helaas, je mag niet stemmen')
else:
    print('Helaas, je mag niet stemmen')