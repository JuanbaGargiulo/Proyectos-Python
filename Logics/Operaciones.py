#Crear un programa en el al ingresar 2 numeros calcule la suma, resta, multiplicacion de dichos numeros


nro1 = float(input("Ingrese el primer numero: "))
nro2 = float(input("Ingrese el segundo numero: "))

def Suma(x,y):
	return print("La suma de los numeros es: ",x+y)

def Resta(x,y):
	return print("La resta de los numeros es: ",x-y)

def Multiplicacion(x,y):
	return print("La multiplicacion de los numeros es: ",x*y)

Suma(nro1,nro2)
Resta(nro1,nro2)
Multiplicacion(nro1,nro2)
