def tillZero():
    while True:
        inputStr = (input('voer een nummer in : '))
        try:
            inEval = int(inputStr)
            if int(inputStr) == 0:
                break
        except ValueError:
            print('een nummer graag')
tillZero()