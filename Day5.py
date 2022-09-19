#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
# #Altura promedio
# student_heights = [156, 178, 165, 171, 187]

# total=0
# for i in student_heights:
# 	total=total+i

# Resultadofinal=total/len(student_heights)
# print(round(Resultadofinal))

#Mejor nota
# NotasEstudiantes = [78, 65, 89, 86, 55, 91, 64, 89]
# notamax=0
# for i in NotasEstudiantes:
# 	if i > notamax:
# 		notamax=i

# print(f"La nota mas alta es: {notamax}")

#Sumar todos los numeros pares que esten entre el 0 y 100

# total=0
# for i in range(2,101):
# 	if i%2==0:
# 		total=total+i

# print(total)

#FizzBuzz
# for i in range(1,101):
# 	if i%3==0 and i%5!=0:
# 		print("Fizz")
# 	if i%5==0 and i%3!=0:
# 		print("Buzz")
# 	if i%3==0 and i%5==0:
# 		print("FizzBuzz")
# 	if i%3!=0 and i%5!=0:
# 		print(i)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# for char in range(1, nr_letters+1):
# 	random_char= random.choice(letters)
# 	password = password + random_char

# for char in range(1, nr_numbers+1):
# 	random_char= random.choice(numbers)
# 	password = password + random_char

# for char in range(1, nr_symbols+1):
# 	random_char= random.choice(symbols)
# 	password = password + random_char

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwordhard=[]
for char in range(1, nr_letters+1):
	random_char= random.choice(letters)
	passwordhard.append(random_char)

for char in range(1, nr_numbers+1):
	random_char= random.choice(numbers)
	passwordhard.append(random_char)

for char in range(1, nr_symbols+1):
	random_char= random.choice(symbols)
	passwordhard.append(random_char)

password1=""
for char in passwordhard:
	password1+=char

print(f"Tu nueva contraseña es: {password1}")
