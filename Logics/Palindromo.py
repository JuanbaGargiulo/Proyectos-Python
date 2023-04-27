#Desarrollar un programa que detecte palabras palindromas, es decir, que se lean de igual de adelante que de atras


def Palindromo(word):
	drow = ''.join(reversed(word))
	if word == drow:
		print("Es una palabra palindroma")
	else:
		print("No es una palabra palindroma")
	
	print("Palabra original: ",word)
	print("Palabra al reves: ",drow)

word = str(input("Ingrese la palabra a analizar: "))

a = 0
while a == 0:
	if word.isalpha() == False:
		print("Ingrese una palabra sin numeros\n")
		word = str(input("Ingrese la palabra a analizar: "))
	else:	
		Palindromo(word)
		a=1
