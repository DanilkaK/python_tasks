lst1 = [1,3,5,7]
lst2 = []
while True:
    lst2.append(lst1[0] * (-2))
    lst2.append(lst1[1] * (-2))
    lst2.append(lst1[2] * (-2))
    lst2.append(lst1[3] * (-2))
    break
print(lst2)


lst3 = [0,1,2,3,4,5,6,7,11,21]
lst4 = []
for i in lst3:
    lst4.append(i * (-2))
print(lst4)