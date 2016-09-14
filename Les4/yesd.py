def anulList():
    anulStationList = []
    for line in anulFile:
        quickList = line.split(sep=': ')
        anulStationList.append(quickList[1].strip('\n'))
    return anulStationList

def ritList():
    ritList = []
    for line in ritenFile:
        ritList.append(line.strip('\n'))
    return ritList