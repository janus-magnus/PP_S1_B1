def convert(tempC):
    tempF = tempC * 1.8+32
    return tempF

def table():
    tempList = [-30,-20,-10,0,10,20,30,40]
    print('{:9}{:15}'.format('F','C'))
    for i in tempList:
        temp = tempList.index(i)
        print('{:5}{:5}'.format(convert(i),temp))
table()