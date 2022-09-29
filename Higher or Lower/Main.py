from GameData import data
import random
from Game import game

terminar = False
while terminar == False:
	perdio = game()
	while perdio:
		rta = input("Desea jugar otra vez: Y/N \n").lower()
		if rta.lower() == 'y':
			perdio = game()
		else:
			print("fin")
			perdio = False
	terminar = True		




