cijferlist = {'Jan':[3.4,9.2,5.5,6.6],'Dindu':[9.8,8.7,6.0,2.4],'Mies':[7.7,1.1,1.3,1.4],
              'Wilma':[4.4,9.9,10.0,8.8]}

for key in cijferlist:
    cijfers = []
    for c in cijferlist.get(key):
        if c >= 9:
            cijfers.append(c)
    s = '{} : {}'.format(key,cijfers)
    print(s)