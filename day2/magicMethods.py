print(dir(int))

num = 10
print(num + 5)
#__add__ когда вы пытаетесь тобавить обьекту что от через плюс
print(num.__add__(7))
#__ge__  : greater equal __lt__ : less than
#__pow__ ккогда возводишь что то в квадрат
#__abs__  : absolute

class Some:

    name = 'John'
    number  = 20

    def __add__(self, str):
        print("some " + str)

  #  def __new__(self):
    #    self.__add__(self, 'new')
    #    self.__init__(self)
    def __init__(self):
        print("Init Started")

    def __str__(self): #вызывается когда хочеш инфу на жкран про обьект
        return "Name: " + self.name

    def __le__(self, x):
        if(self.number >= x):
            return True
        else:
            return False

    def __del__(self):
        print("deleted object")

obj = Some()
print(obj)
print(obj <= 5)
print(dir(obj))
