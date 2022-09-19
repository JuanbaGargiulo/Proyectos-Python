import random
from typing import List

#Pruebas
# randomint =random.randint(1,10)
# print(randomint)

# randomfloat = random.random() *5
# print(randomfloat)

# love_score = random.randint(1,100)
# print(f"Tu escore de amor es {love_score}")

#Cara o Cruz?

# numran= random.randint(0,1)
# if (numran == 0):
# 	print("Cruz")
# else:
# 	print("Cara")

#Quien paga la factura?
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# ram=random.randint(0,len(names)-1)
# persona=names[ram]
# print(persona + "is going to buy the meal today!")

#Mapa del tesoro
# row1 = ["??","??","??"]
# row2 = ["??","??","??"]
# row3 = ["??","??","??"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("where do you want to put the treasure? ")
# f=int(position[0])
# c=int(position[1])

# map[c-1][f-1]="x"
# print(f"{row1}\n{row2}\n{row3}")

#Piedra, papel o tijeras
rock = '''
rock 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    ______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
opciones=[rock,paper,scissors]

ramdom=opciones[random.randint(0,2)]
personchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("Sistem choice: \n", ramdom)
#Rock
if personchoice == 0 and ramdom == scissors:
	print("Your choice: \n",opciones[0])
	print("Win")
if personchoice == 0 and ramdom == rock:
	print("Your choice: \n",opciones[0])
	print("draw")
if personchoice == 0 and ramdom == paper:
	print("Your choice: \n",opciones[0])
	print("Lose")

#Paper
if personchoice == 1 and ramdom == rock:
	print("Your choice: \n",opciones[1])
	print("Win")
if personchoice == 1 and ramdom == paper:
	print("Your choice: \n",opciones[1])
	print("draw")
if personchoice == 1 and ramdom == scissors:
	print("Your choice: \n",opciones[1])
	print("Lose")

#Scissors
if personchoice == 2 and ramdom == paper:
	print("Your choice: \n",opciones[2])
	print("Win")
if personchoice == 2 and ramdom == scissors:
	print("Your choice: \n",opciones[2])
	print("draw")
if personchoice == 2 and ramdom == rock:
	print("Your choice: \n",opciones[2])
	print("Lose")
