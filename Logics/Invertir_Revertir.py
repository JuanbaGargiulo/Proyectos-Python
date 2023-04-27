#Dada una cadena de texto, darle la vuelta e invertir el orden de sus caracteres, sin usar metodos propios del lenguaje
#solo estructuras

word = str(input("Ingrese la palabra a invertir: "))

def invert(word):
	#listWord = list(word)
	listWord = []
	for i in word:
		listWord.append(i)
	
	drow = ''.join(reversed(listWord))
	
	
	return drow

print(invert(word))


