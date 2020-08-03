p_sum_num = input('Введите числа :') #Второй вариант дз т.к в первом сделал неправильно :0
lst1 = list(p_sum_num)#Преобразуем числа в список
lst2 = []
#Переменная рзиции элементов в списке
h_m = len(lst1) - 1

while h_m >= 0 :
    lst2.append(lst1[h_m] * -2)

    h_m -= 1
lst2.reverse()

print(lst2)
