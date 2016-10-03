def standaardtarief(km):
    if km >= 0:
        if km > 50:
            standaard_prijs = km * 0.60 + 15
        else:
            standaard_prijs = km * 0.60
    else:
        standaard_prijs = 0
    return standaard_prijs

def ritprijs(leeftijd,wkndRit,km):
    rit_prijs = standaardtarief(km)

    if leeftijd <= 12 or leeftijd >= 65:
        if wkndRit == True:
            rit_prijs -= (rit_prijs / 100 * 35)
        else:
            rit_prijs -= (rit_prijs / 100 * 30)
    elif wkndRit == True:
        rit_prijs -= (rit_prijs / 100 * 40)
    return rit_prijs

#testCases
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