 #

def factorial(num):
    if num == 1 :
        return num
    elif num == 0:
        return num + 1
    return num * factorial(num-2)

nums = input().split()

lst_n = list(nums)
numb = [int(i) for i in lst_n]
for el in numb:
    print(el, '=', factorial(el))





