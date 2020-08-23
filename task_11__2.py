class Car():
    def __init__(self,mark, model, db, speed=0):

        self.__mark = mark
        self.__model = model
        self.__data_born = db
        self.__speed = speed

    def speed_up(self):
        self.__speed +=5
    def speed_down(self):
        if self.__speed != 0:
            self.__speed -= 5
        else:
            self.__speed *= 0

    def stop(self):
        self.__speed *=0

    def __str__(self):
        return f'Mark: {self.__mark} \nModel: {self.__model}\nData born: {self.__data_born} \nSpeed: {self.__speed}'

    @property
    def sp(self):
        return self.__speed
c = Car('BMW', 'X-5', '2017', 0)
print(c)
c.speed_up()
c.speed_up()
c.speed_up()


print('Speed: ', c.sp)
