def Cuadrado(filas, columnas):
	board = []
	#Crear matriz
	for i in range(columnas):
		board.append([" "]*filas)

	for j in range(len(board[0])):
		for i in range(len(board)):
			if filas == columnas:	
				if j == 0 or j == columnas-1 or i==0 or i == filas-1:
					board[i][j] = "*"
	Imprimir(board)
	

def Imprimir(board):
	#Imprimir matriz
	for j in range(len(board[0])):
		for i in range(len(board)):
			print(board[j][i],end=' ')
		print()

columnas = int(input("Ingrese el largo de la forma: "))
filas = int(input("Ingrese el alto de la forma: "))

Cuadrado(filas,columnas)


