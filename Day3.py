#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
from typing import List
# peso=float(input("Ingrese su peso: "))
# altura=float(input("Ingrese su altura: "))

#Calculadora IMC 2.0
# bmi=peso/(altura*altura)
# if bmi <18.5:
# 	print("underweight")
# elif bmi > 18.5 and bmi < 25:
# 	print("Normal weight")
# elif bmi > 25 and bmi < 30:
# 	print("Overweight")
# elif bmi > 30 and bmi < 35:
# 	print("Obese")
# elif bmi > 35:
# 	print("Clinically obese")

# Año Bisiesto?
# año=int(input("Ingrese año: "))
# if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
# 	print("Es bisiesto")
# else:
# 	print("No es bisiesto")

# Pizza Time
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# total=0
# if size == "S":
# 	total+=15
# elif size =="M":
# 	total+=20
# elif size =="L":
# 	total+=25

# if add_pepperoni =="Y" and size =="S":
# 	total+=2
# elif add_pepperoni =="Y" and size =="M" or size =="L":
# 	total+=3

# if extra_cheese=="Y":
# 	total+=1

# print("Costo: ",total)

# #Love Calculator
# name1=input("Ingrese nombre 1: ")
# name2=input("Ingrese nombre 2: ")

# nombresjuntos=name1+name2
# nombrep=nombresjuntos.lower()

# t=nombrep.count("t")
# r=nombrep.count("r")
# u=nombrep.count("u")
# e=nombrep.count("e")

# true=t+r+u+e
# l=nombrep.count("l")
# o=nombrep.count("o")
# v=nombrep.count("v")
# e=nombrep.count("e")

# love=l+o+v+e

# score=int(str(true)+str(love))

# if score <10 or score>90:
# 	print(f"Your score is {score}, you go together like coke and mentos")
# elif score >40 and score<50:
# 	print(f"Your score is {score}, you are alright together.")
# else:
# 	print(f"Your score is {score}")

# Treasure Island
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

# respuesta=input("You\'re at a crossroad. Where do you want to go? Type left or right\n")
# if respuesta =="left":
# 	respuesta=input("You\'ve come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across\n")
# 	if respuesta =="wait":
# 		respuesta=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
# 		if respuesta =="red":
# 			print("It's a room full of fire. Game Over.")
# 		elif respuesta =="yellow":
# 			print("You found the treasure! You Win!")
# 		elif respuesta =="blue":
# 			print("You enter a room of beasts. Game Over.")
# 		else:
# 			print("You chose a door that doesn't exist. Game Over.")
# 	else:
# 		print("Game Over, you re dead")
# else:
# 	print("Game Over, you re dead")



