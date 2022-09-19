import random

def listaAString(t):
	string=""
	for i in range(0,len(t)):
		string+=t[i]
	return string	

#Back
def start():
	# #Generar Palabra
	palabras =["CASA","RATON","AUTO","COMPUTADORA"]
	palabraSeleccionada = random.choice(palabras)
	cantidadLetras = len(palabraSeleccionada)
	espacios=[]

	for i in range(0,cantidadLetras):
		espacios.append("_")

	print(listaAString(espacios))
	vidas=6
	while vidas!=0:
		encontre=False
		letra=str(input("Ingrese una letra: "))
		if letra == palabraSeleccionada:
			print("Ganaste")
			vidas=0
		else:
			for x in range(0,cantidadLetras):
				if letra == palabraSeleccionada[x]:
					espacios[x]=letra
					encontre=True
			
			print(listaAString(espacios))
			if listaAString(espacios)==palabraSeleccionada:
				print("Ganaste")
				vidas=0
				
			if encontre==False:
				vidas=vidas-1
				print(f"Te quedan: {vidas} vidas")
				if vidas == 0:
					print("Perdiste")

start()

print("Game Over")
