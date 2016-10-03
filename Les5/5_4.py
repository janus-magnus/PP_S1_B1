def tillZero():
    while True:
        try:
            inputStr = (input('voer een nummer in : '))
            if int(inputStr) == 0:
                break
        except ValueError:
            print('een nummer graag')
tillZero()