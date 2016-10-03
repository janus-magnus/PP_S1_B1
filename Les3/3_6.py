lijst = ['a','b','c']

def wijzig(lst):#dit is misschien een beetje te geforceerde manier om dit te doen
    del lst[:]
    lst.append('d')
    lst.append('e')
    lst.append('f')

print(lijst)
wijzig(lijst)
print(lijst)