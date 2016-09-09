lijst = ['a','b','c']

def wijzig(lst):
    del lst[:]
    lst.append('d')
    lst.append('e')
    lst.append('f')

print(lijst)
wijzig(lijst)
print(lijst)