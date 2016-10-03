def namen():
    nameDict = {}
    while True:
        name = input('Voer naam in :')
        if name == '':#stopt als er geen input wordt meegegeven
            break
        else:
            if name in nameDict:
                nameDict[name] = int(nameDict[name])+1
            else:
                nameDict[name] = 1
    for k in nameDict.keys():
        if nameDict[k] == 1:#het onderstaande if-statment wordt gebruikt om de juiste text mee te geven voor het aantal studenten
            s1 = 'is'
            s2 = 'student'
        else:
            s1 = 'zijn'
            s2 = 'studenten'
        print('Er {} {} {} met de naam {}'.format(s1,nameDict[k],s2,k))

namen()