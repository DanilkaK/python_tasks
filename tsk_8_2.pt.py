 # Opredelaem slova-palindrom

def pol(lst):
  # Vvedenoe slovo
    ls = lst

    b = ls



    lst1 = list(b)

  # Razbivaem na simvol and sozdaem slovari s ih elementami
    standart_lst = [i for i in ls]
    reversed_lst = [el for el in b]
  # Perevorachevaem spisok s elementami
    reversed_lst.reverse()

    print(standart_lst)
    print( reversed_lst)

  # Sravnivaem ih
    if standart_lst == reversed_lst:
        print('Slovo-palindrom')
    else:
        print('Ne palindrom')


word = input('Vvedite slovo: ')

pol(word)
