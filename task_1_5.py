print('Найдем гипотенузу и площадь ')
from math import sqrt
x2 = float(input('Введети первый катет: '))
y2 = float(input('Введети второй катет: '))
x2_y2 = input('1 - Найдем гипотенузу , 2 - площадь треугольгика:  ')
w1 = (x2 * x2) + (y2 * y2)
if x2_y2 == '1':
    print('Ответ: ' +str(sqrt(w1)))
else:
    print('Ответ: ' +str( (x2 * y2 )/2))