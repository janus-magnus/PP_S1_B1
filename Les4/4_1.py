def convert(tempC):
    tempF = tempC * 1.8+32
    return tempF

def table():
    tempList = [-30,-20,-10,0,10,20,30,40]
    print('F\t\tC')
    for i in tempList:
        print(str(convert(i))+'\t'+str(tempList.index(i)))

table()