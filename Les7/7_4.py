import csv

valueslist = [['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'],[121, 'ABC123','Highlight pen', 231, 0.56],
              [123, 'PQR678', 'Nietmachine', 587, 9.99],[128, 'ZYX163', 'Bureaulamp', 34, 19.95],
              [137, 'MLK709', 'Monitorstandaard', 66, 32.50],[271, 'TRS665', 'Ipad hoes', 155, 19.01]]

with open('article.csv', 'w',newline='\n') as atf:
    artklWriter = csv.writer(atf)
    artklWriter.writerows(valueslist)
    atf.close()

with open('article.csv', 'r', newline='\n') as atf:
    artklReader = csv.reader(atf)

    valuesInList = []

    for line in artklReader:
        valuesInList.append(line)

    valuesInList.pop(0)
    minPrijs = 10000000
    minVoor = 100000000.0
    sumVoor = 0

    print(valuesInList)

    for artk in valuesInList:
        if minPrijs > eval(artk[4]):
            minPrijs = eval(artk[4])
        if minVoor > eval(artk[3]):
            minVoor = eval(artk[3])

        sumVoor =+ eval(artk[3])

        for artk in valuesInList:
            if minPrijs == eval(artk[4]):
                naam = str(artk[2])
                prijs = str(artk[4])
                s1 = 'Het duurste artikel is {} en die kost {} Euro'.format(naam,prijs)
            if minVoor == int(artk[3]):
                aantal = str(artk[3])
                pNum = str(artk[0])
                s2 = 'Er zijn slechts {} exemplaren in voorraad van het product ' \
                        'met nummer {}'.format(aantal,pNum)
        s3 = 'In totaal hebben wij {} producten in ons magazijn liggen'.format(sumVoor)

    print(s1,s2,s3,sep='\n')

atf.close()