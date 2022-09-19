#Ejecicio de practica
# def greet(name):
# 	print("Hello "+name)
# 	print("How re u "+name+"?")

# nombre=str(input("Enter your name: "))
#greet(nombre)
# def greet_2(name,location):
# 	print("Hello "+name)
# 	print(f"Do u live in {location}?")

# nombre=str(input("Enter your name: "))
# location=str(input("Enter your location: "))
# greet_2(nombre,location)

#Calculadora de latas de pintura
# def paint_calc(height,width,cover):
# 	total=(height*width)/cover
# 	print(round(total))


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#Es numero primo?
def num_prime(numero):
	esPrimo=True
	for i in range(2,numero):
		if numero%i==0:
			esPrimo=False
	if esPrimo == True:
		print(f"El numero {numero} es primo")
	else:
		print(f"El numero {numero} no es primo")

numero=int(input("ingrese un numero: "))
num_prime(numero)
