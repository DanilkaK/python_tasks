class Class1:
    def __init__(self, obj, lenght, width, height):
        self.__object = obj
        self.__lenght = lenght
        self.__witdh = width
        self.__height = height

    def setPorametrs(self, o, l, w, h):
        self.__object = o
        self.__lenght = l
        self.__witdh = w
        self.__geight = h

    def getPorametrs(self):
        return self.__object, self.__lenght, self.__witdh,  self.__height

    def action(self):
        print('Sohnet')
    def anoter_action(self):
        print('stands')
p = Class1('Table',12,54,17)
print(p.getPorametrs())
p.action()


class Class2:

    def __init__(self, people, height, age, weight):
        self.__people = people
        self.__height = height
        self.__age = age
        self.__weight = weight
    def setPeoplePorametrs(self, p, h, a, w):
        self.__people = p
        self.__height = h
        self.__age = a
        self.__weight = w
    def getPeoplePorametrs(self):
        return f"{self.__people} Height: {self.__height} Age: {self.__age} Weight: {self.__weight} "

    def PeopleAction(self):
        print('Dumaet')

    def AnoterPeopleAction(self):
        print('Mechtaet')


p1 = Class2('Vova',12,54,17)
print(p1.getPeoplePorametrs())
p1.PeopleAction()


class Class3:

    def __init__(self, animal, height, age, weight):
        self.__animal = animal
        self.__height = height
        self.__age = age
        self.__weight = weight
    def setPeoplePorametrs(self, a, h, ag, w):
        self.__animal = a
        self.__height = h
        self.__age = ag
        self.__weight = w
    def getPeoplePorametrs(self):
        return f"{self.__animal} Height: {self.__height} Age: {self.__age} Weight: {self.__weight} "

    def AnimalAction(self):
        print('Hochet est')

    def AnoterAnimalAction(self):
        print('est')
p2 = Class3('Dog',12,3,7)
print(p2.getPeoplePorametrs())
p2.AnoterAnimalAction()