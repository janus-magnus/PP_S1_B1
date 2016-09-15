

def maand(maandNum):
    maandInt = eval(maandNum)
    if maandInt >= 12 and maandInt <= 2:
        return 'Winter'
    elif maandInt >= 3 and maandInt <= 5:
        return 'spring'
    elif maandInt >= 6 and maandInt <= 8:
        return 'spring'
    elif maandInt >= 9 and maandInt <= 11:
        return 'spring'

print(maand(input("voer maandummer in: ")))