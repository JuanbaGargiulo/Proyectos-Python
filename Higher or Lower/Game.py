import random
from GameData import data
def format_data(account):
	nombreaccount = account["name"]
	descripcionaccount = account["description"]
	paisaccount = account["country"]
	return f"{nombreaccount},{descripcionaccount},{paisaccount}"

def format_data2(account):
	nombreaccount = account["name"]
	descripcionaccount = account["description"]
	paisaccount = account["country"]
	cantseguidores = account["follower_count"]
	return f"{nombreaccount},{descripcionaccount},{paisaccount},Cantidad de seguidores: {cantseguidores}"

def check(guess, cantfollowers1, cantfollowers2):
	if cantfollowers1 > cantfollowers2:
		return guess == "a"
	else:
		return guess == "b"


def game():
	lose=False
	score=0
	account1=random.choice(data)
	account2=random.choice(data)
	if account1 == account2:	
		account2= random.choice(data)
	while lose == False:
		if score >= 1:
			print(f"Compare A: {format_data2(account1)}.")
			print(f"Compare B: {format_data(account2)}.")
		else: 
			print(f"Compare A: {format_data(account1)}.")
			print(f"Compare B: {format_data(account2)}.")


		guess = input("Quien tiene mas followers? A o B\n").lower()
		while guess not in ("a","b"):
			print("Respuesta no valida")
			guess = input("Quien tiene mas followers? A o B\n").lower()

		cantfollowers1= account1["follower_count"]
		cantfollowers2= account2["follower_count"]

		is_correct = check(guess,cantfollowers1,cantfollowers2)
		if is_correct:
			score +=1
			print(f"Muy bien! Score: {score}")
			account1=account2
			account2=random.choice(data)
		else:
			print("Perdiste")
			print(f"Tu puntuacion fue: {score}")
			lose=True
	return True
