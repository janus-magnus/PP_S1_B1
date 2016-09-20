import random

def monopolyworp():
    doubleCount = 0
    count = 0
    while True:
        worp1 = random.randint(1, 6)
        worp2 = random.randint(1, 6)
        result = worp1+worp2
        note = ''


        if worp1 == worp2:
            doubleCount = doubleCount + 1
            note = 'dubbel'

            if doubleCount == 3:
                note = 'direct naar de gevangenis'
                print('{} + {} = {} ({})\n'.format(worp1, worp2, result, note))
                return False# dit is voor de while loop onderaan
                break

            print('{} + {} = {} ({})'.format(worp1, worp2, result, note))

        else:
            print('{} + {} = {} ({})\n'.format(worp1,worp2,result,note))
            break



#loopt de methode tot dat er de uitkomst 'naar de gevangenis is'
while True:
    monopolyworp()
    if monopolyworp()==False:
        break