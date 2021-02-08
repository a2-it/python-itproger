class User:
    name = ''
    surname = ''
    age = 0
    email = ''
#constructor: срабатывает при создании обьекта
    def __init__(self, name, surname, age, email):
        print('Hi')
        self.name = name
        self.surnam = surname
        self.age = age
        self.email = email

    def set(self, name, surname, age):
        self.name = name
        self.surnam = surname
        self.age = age

    def printAll(self):
        print('User: ', self.name, 'age: ', self.age)



admin = User('Sherz', 'Sh', '21', '@mail.ru')
#admin.name ='Sherz' admin.age = 21  <---before set()
#admin.set('Sherz', 'Sh', '21')
#admin.email = '@mail.ru'
#print(admin.name)   <---before printAll()
admin.printAll()

bob = User('Bob', 'Snob', 25, 'email.com')
#bob.set('Bob', 'Snob', 25)
#bob.email = 'email.com'
#print(bob.name)
bob.printAll()
