# Импорт класса для перечисления
from enum import Enum

class Variants(Enum):
	ROCK = 1
	PAPER = 2
	SCICCORS = 3

	def getValue(self):
		return self.value

