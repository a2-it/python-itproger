# Импорт файлов и классов из них
from variants import Variants
from player import Player

# Создаем объекты на основе класса Player
bot = Player()
# При создании можем не передавать значения или же
# можем передать выбор (камень, ножницы или бумага), а также имя
alex = Player(Variants.SCICCORS, "Alex")
#alex.printPlayerInfo()
#bob = Player(Variants.ROCK, "Bob")
#bob.printPlayerInfo()
# далее через объект можем обратить к функции whoWins
# и мы узнаем кто победил
#print(bot.whoWins(bot, alex))

print(alex.whoWins(bot))