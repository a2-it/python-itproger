from variants import Variants

class Player():
    name = 'Bot'
    var = Variants.PAPER

    def __init__(self, var = Variants.PAPER, name = "Bot"):
        self.var = var
        self.name = name


    def set(self, var, name):
        self.name = name
        self.var = var

    def printPlayerInfo(self):
        print("User name: {}, he chose: {}".format(self.name, self.var))

    def whoWins(player1, player2):
        if player1.var.value == 1:
            if player2.var.value == 1:
                return 'ничья'
            elif player2.var.value == 2:
                return '{} выиграл'.format(player2.name)
            else:
                return '{} выиграл'.format(player1.name)
        if player1.var.value == 2:
            if player2.var.value == 1:
                return '{} выиграл'.format(player1.name)
            elif player2.var.value == 2:
                return 'ничья'
            else:
                return '{} выиграл'.format(player2.name)
        if player1.var.value == 3:
            if player2.var.value == 1:
                return '{} выиграл'.format(player2.name)
            elif player2.var.value == 2:
                return '{} выиграл'.format(player1.name)
            else:
                return 'ничья'








