N = int(input('Введите число: '))
N +=1



a_r = range(2, N)




Sum = 1

el = 0
for el in a_r:
	a = 1/a_r[0]

	Sum += 1/el
	el +=1

print(Sum)