#INHERITANCE
class Car:
     color = ''
     #_color : означает что вы хотите эту переменную хотите оставить ащищенной
                #не хотите использовать вне класса
     weight = 0

     def set(self, color, weight):
         self.color = color
         self.weight = weight

class BMW (Car):  #this is inheritance from Car
    isM_model = False

#POLYMORFISM : это переопределение метода

    def set(self, color, weight, isM_model): #plymorfism belike
        self.color = color                   #это переопределение метода
        self.weight = weight
        self.isM_model = isM_model

x3 = BMW()
x3.set('White', 2400, False)
print(x3.color)

m3 = BMW()
m3.set("Grey", 1400, True)
print(m3.isM_model)