a = {'test' : 'test_value' , 'europe' : 'eur' , 'dollar' : 'usd' , 'ruble' : 'rub' }

while 1 == 1:
     b = list(a.keys())
     c = len(b[0])
     d = len(b[1])
     e = len(b[2])
     f = len(b[3])

     break
a['test' + str(c)] = 'test_value'
a['europe' + str(d)] = 'eur'
a['dollar' + str(d)] = 'usd'
a['ruble' + str(d)] = 'rub'
del a['europe']
del a['test']
del a['dollar']
del a['ruble']

print(a)

a1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}


b1 = list(a.keys())
for el in b1:
    c1 = len(b1[0])
    d1 = len(b1[1])
    e1 = len(b1[2])
    f1 = len(b1[3])


a1['test' + str(c)] = 'test_value'
a1['europe' + str(d)] = 'eur'
a1['dollar' + str(d)] = 'usd'
a1['ruble' + str(d)] = 'rub'
del a1['europe']
del a1['test']
del a1['dollar']
del a1['ruble']

print(a1)