class Form:
    def __init__(self, login = 'bot', passw = 'lemmepass', url = '', three=''):
        self.login= login
        self.passw = passw
        self.url = url
        self.three = three


    def printAll(self):
        return "{}'s password is {}".format(self.login, self.passw)