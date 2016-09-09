def standaardtarief(km):
    prijs = float(0)
    if km >= 0:
        if km > 50:
            prijs = km * 0.60 + 15
        else:
            prijs = km * 0.60
    else:
        prijs = 0
    return prijs

def ritprijs(leeftijd,wkndRit,km):
    prijs = standaardtarief(km)

   # if type(leeftijd) == int and type(wkndRit) == bool and type(km) == int:
    if leeftijd <= 12 or leeftijd >= 65:
        if wkndRit == True:
            prijs -= (prijs / 100 * 35)
        else:
            prijs -= (prijs / 100 * 30)
    elif wkndRit == True:
        prijs -= (prijs / 100 * 40)


    return prijs

print(ritprijs(11,True,100))
print(ritprijs(12,True,100))
print(ritprijs(13,True,100))
print(ritprijs(11,False,100))
print(ritprijs(12,False,100))
print(ritprijs(13,False,100))

print(ritprijs(64,True,100))
print(ritprijs(65,True,100))
print(ritprijs(66,True,100))
print(ritprijs(64,False,100))
print(ritprijs(65,False,100))
print(ritprijs(66,False,100))

print(ritprijs(30,True,100))
print(ritprijs(30,False,100))