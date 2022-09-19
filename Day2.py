#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# a=len(input("Ingresa una palabra: "))
# print("Cantidad de letras: ",a)

# b=input("Ingrese un numero a sumar: ")
# c=int(b[0])+int(b[1])
# print(c)

# peso=int(input("ingrese su peso: "))
# altura=float(input("ingrese su altura: "))

# bmi=peso/(altura*altura)
# print(bmi)

# d=int(input("Cuantos años tenes?: "))
# v=90-d

# dias=365*v
# semanas=52*v
# meses=12*v

# print(f"Te quedan: {dias} dias, {semanas} semanas,{meses} meses")

print("Calculadora de pagos\n")
total=float(input("Cuanto es el total?: "))
propina=int(input("Cuanta propina queres dejar: 10,12,15%"))
personas=int(input("En cuantas personas se divide la cuenta?: "))

propina=propina/100
procentaje=round(total*propina,2)
total=round(total + procentaje,2)
totalfinal=total/personas
print("El total a pagar es: ",totalfinal)
