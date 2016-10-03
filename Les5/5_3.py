invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

splitList = invoer.split('-')
convertedList = [int(i) for i in splitList]

listSort = sorted(convertedList)
listMax = max(convertedList)
listMin = min(convertedList)
listLen = len(convertedList)
listSum = sum(convertedList)
listAvg = listSum/listLen

outStr = 'Gesorteerde list van ints: {}\nGrootste getal: {} en Kleinste getal: {}\nAantal getallen: {} ' \
         'en Som van de getallen: {}\nGemiddeldeL {}'.format(listSort,listMax,listMin,listLen,listSum,listAvg)

print(outStr)