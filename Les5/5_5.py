def tillFourhead():
    while True:
        inputStr = (input('voer een strig van 4 letters in : '))
        inLen = len(inputStr)
        if inLen == 4:
            print('inlezen is gelukt')
            break
        else:
            print('{} is {} leters lang'.format(inputStr, inLen))
tillFourhead()