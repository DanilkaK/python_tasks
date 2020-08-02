num = input('')
num_list = list(num)
print(num_list)
list_d2 = []
cl_vo_num = 0
el = 0
while el < len(num_list):
    if int(num_list[el]) % 2 == 0:
        list_d2.append(num_list[el])
        cl_vo_num =+ 1
    el += 1
print('Количество четных чисел: ' + str(cl_vo_num))
print("Список четных чисел" + str(list_d2))



num2 = input('ВВедите числа: ')
num2_list = list(num2)
print(num_list)
cl_vo_num2 = 0

for i in num2_list:
    if int(i) % 2 ==0:
        cl_vo_num2 +=1


print('Кол-во четных чисел : ' + str(cl_vo_num2))
