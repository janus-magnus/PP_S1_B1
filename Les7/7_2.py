import datetime
import csv

while True:
    naam = input("Wat is je achternaam? ")

    if naam == 'einde':
        infile.close()
        break

    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input('Wat is je e-mail adres?: ')

    today = datetime.date.today().strftime('%d-%m-%y')
    now = datetime.datetime.now().time().strftime('%H:%M:%S')

    datetimeStr = str(today)+' at '+str(now)

    with open('inloggers.csv','a', newline='\n') as infile:
        inlogWriter = csv.writer(infile, delimiter=';')
        s = [datetimeStr,naam,voorl,gbdatum,email]
        inlogWriter.writerow(s)
        print(s)

