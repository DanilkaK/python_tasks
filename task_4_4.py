lst5 = [1,2,3,4,5,6,7]
print(lst5)
while 1 == 1:
    lst5.append(lst5[0])
    lst5.remove(lst5[0])

    break

print(lst5)

lst6 = [7,6,5,4,3,2,1]
print(lst6)

for i in lst6:
    lst7 = lst6
    lst7.append(lst6[0])
    lst7.remove(lst6[0])

    print(lst7)
    break