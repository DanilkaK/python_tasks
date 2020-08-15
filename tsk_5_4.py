num2 = input('Введите число: ')
num2_list = list(num2)

sum_nun2 = 0
proiz_num2 = 1

for i in num2_list:
    sum_nun2 += int(i)
for i in num2_list:
    proiz_num2 *= int(i)

print('Сумма чисел: ', str(sum_nun2))
print('Произведение чисел: ', str(proiz_num2))
