import random
def Repartir(list):
	cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
	if len(list)==0:
			for i in range(2):
				list.append(random.choice(cards))
	else:
		list.append(random.choice(cards))
	

def ganador(user,computer):
	totalC=0
	totalU=0
	Asu=False
	Asc=False
	
	for i in user:
		totalU+=i
		if i == 11:
			Asu=True
	for i in computer:
		totalC+=i
		if i == 11:
			Asc=True

	if totalU >21 and Asu==True:
		for i in user:
			if i ==11:
				user[i]=1
				totalU=(totalU-11)+1
	
	if totalC >21 and Asc==True:
		for i in computer:
			if i ==11:
				a=computer.index(i)
				computer[a]=1
				totalC=(totalC-11)+1
	
	if totalU == totalC:
		print("Draw")
	if totalU>21 and totalC>21:
		print("Draw")
	elif totalU > 21 and totalC<21:
		print(f"Computer wins with {totalC}")
	elif totalC > 21 and totalU<21:
		print(f"User wins  with {totalU}")
	elif 21-totalC>21-totalU:
		print(f"User Wins with {totalU}")
	elif 21-totalC<21-totalU:
		print(f"Computer Wins with {totalC}")
	

def juego():
	print("Bienvenido a BlackJack")
	total=0
	user=[]
	computer=[]
	Repartir(user)
	Repartir(computer)	
	print("User",user)
	print("Computer",computer)
	
	oneMore=str(input("Desea agarrar otra carta? y o n"))
	if oneMore == "y":
		Repartir(user)
		print("User",user)

	for i in computer:
		total+=i
	if total<17:
		while total<17:
			Repartir(computer)
			for i in computer:
				total+=i
			total
	print("Computer",computer)

	ganador(user,computer)

juego()
