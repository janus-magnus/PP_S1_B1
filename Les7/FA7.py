import csv
import random

with open('kluizen.txt','r') as kluizen:
    klReader = csv.reader(kluizen)
    kluizenLijst = []
    for line in klReader:
        kluizenLijst.append(line)
    print(kluizenLijst)

def newKl():
    for kluis in kluizenLijst:
        if eval(kluis[2]) == True:
            c1=str(random.randint(0,9))
            c2=str(random.randint(0,9))
            c3=str(random.randint(0,9))
            c4=str(random.randint(0,9))
            print(c1,c2,c3,c4)
            code = c1+c2+c3+c4
            #code = random.randint(0,9999)
            kluis[2]= 'False'
            kluis[1]= code
            kluisNr=str(kluis[0])
            print('Je kluisnummer is: {}\nJe code is: {}'.format(kluisNr,code))
            break

    print('geen vrije kluizen beschickbaar')

    with open('kluizen.txt','w', newline='\n') as kluizen:
        kWriter = csv.writer(kluizen)
        kWriter.writerows(kluizenLijst)


def openKl(kluisNr,kluisCode):
    for kluis in kluizenLijst:
        if kluis[0] == kluisNr and kluis[1] == kluisCode and eval(kluis[2])==False:
            print('Je Kluis is open')

def delKl(kluisNr,kluisCode):
    for kluis in kluizenLijst:
        if kluis[0] == kluisNr and kluis[1]== kluisCode:
            code = '0000'
            kluis[2] = 'True'
            kluis[1] = code
            kluisNr = str(kluis[0])
            print('De kluis met het nummer {} is terug gegeven'.format(kluisNr))
            break
        else:
            print('toegang geweigerd')

    with open('kluizen.txt', 'w', newline='\n') as kluizen:
        kWriter = csv.writer(kluizen)
        kWriter.writerows(kluizenLijst)

def vrijKl():
    counter = 0
    for kluis in kluizenLijst:
        print(kluis[2])
        if eval(kluis[2])==True:
            counter+=1
    print(counter)

def secret():
    for kluis in kluizenLijst:
            code = '0000'
            kluis[2] = 'True'
            kluis[1] = code
    print('reset')
    print(kluizenLijst)

    with open('kluizen.txt', 'w', newline='\n') as kluizen:
        kWriter = csv.writer(kluizen)
        kWriter.writerows(kluizenLijst)

while True:
    print('1: Ik wil een nieuwe kluis\n2: Ik wil mijn kluis openen\n3: Ik geef mijn kluis terug'
          '\n4: Ik wil weten hoeveel kluizen nog vrij zijn\n5: Ik wil stoppen\n')
    choice = eval(input(''))
    if choice == 1:
        newKl()
    elif choice == 2:
        klNr = input('voer kluisnummer in:')
        klCode = input('voer kluiscode in:')
        openKl(klNr, klCode)
    elif choice == 3:
        klNr = input('voer kluisnummer in:')
        klCode = input('voer kluiscode in:')
        delKl(klNr,klCode)
    elif choice == 4:
        vrijKl()
    elif choice == 5:
        break
    elif choice == 6:
        secret()
    else:
        print('voer alleen nummers tussen de 1-5 in')

