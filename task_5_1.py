while 1 == 1:

    sign = input('Что будем делать: (+, -, /,* , 0 - end) : ')
    if sign == '0':
        break

    else:

        X = int(input('Введите число: '))
        Y = int(input('Введите число: '))

        if sign == '+':
            Z = X + Y
            print(Z)

        elif sign == '-':
            Z = X - Y
            print(Z)
        elif sign == '/':
            if Y == 0:
                print('error')

            else:
                Z = X / Y
                print(Z)
        elif sign == '*':
            Z = X * Y
            print(Z)
        else:
            print('error')

print('end')