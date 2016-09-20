def namen():
    nameDict = {}
    while True:
        name = input('Voer naam in :')
        if name == '':
            break
        else:
            if name in nameDict:
                nameDict[name] = int(nameDict[name])+1
            else:
                nameDict[name] = 1
    for k in nameDict.keys():
        if nameDict[k] == 1:
            s1 = 'is'
            s2 = 'student'
        else:
            s1 = 'zijn'
            s2 = 'studenten'
        print('Er {} {} {} met de naam {}'.format(s1,nameDict[k],s2,k))

namen()