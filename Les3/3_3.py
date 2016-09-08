lengte = eval(input('voer je lente in(in cm): '))

def langGenoeg(lengteCm):

    if type(lengte) == int:
        if lengte >= 120:
            return 'je bent lang genoeg voor de atractie'
        else:
            return 'je bent te klein voor de atractie'
    else:
        return 'alleen cijfers'

print(langGenoeg(lengte))