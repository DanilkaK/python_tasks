print('Найдем объем(V) куба или площадь(S) боковой поверхности куба')
drk = float(input('Введите длинну ребра: '))
sho = input('Что ищем? : ')
if sho == 'V':
    print('Объем : ' + str( drk * drk * drk ))
else :
    print('лощадь(S) боковой поверхности куба: ' + str(drk * drk))