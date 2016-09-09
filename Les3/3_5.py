testList = [1,2,9,6,0,-7]

def kwadraten_som(grongetalen):
    returnList = []
    if type(grongetalen) == list:
        for gg in grongetalen:
            if gg >= 0:
                returnList.append(gg*gg)
    return returnList

print(kwadraten_som(testList))