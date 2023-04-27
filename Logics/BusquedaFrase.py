#Dada una palabra y una frase, contar cuantas veces se repite la pablabra en la frase
#Tiene que ser en una funcion

word = str(input("Ingrese la palabra: "))
phase = str(input("Ingrese la frase: "))

def Search(word,phrase):

	return phase.lower().count(word.lower())

print("La cantidad de veces que se repite esa palabra es: ", Search(word,phase))



