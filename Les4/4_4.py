from pathlib import Path
import time
file = Path('hardlopers.txt')

if file.is_file():
    hardloopFile = open('hardlopers.txt', 'w')
    #print('1')
else:
    hardloopFile = open('hardlopers.txt', 'a')
    #print('2')

dateStr = time.strftime('%a %d %b %Y,')
runTimeStr = input("voer de gelopen tijd in: ")
nameStr = input("voer de naam in: ")

writeStr = dateStr + runTimeStr + ', '+ nameStr

hardloopFile.write(writeStr)
hardloopFile.close()