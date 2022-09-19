def people():
	bidder = str(input("Enter your name: "))
	bid = int(input("Enter you bid: "))
	bidders = {}
	bidders[bidder] = bid
	return bidders

def Auction(bidders):
	max=0
	ganador=""
	for i in bidders:
		if bidders[i]>max:
			max=bidders[i]
			ganador=i
	print(f"El ganador es {ganador} con {max}")
	
def start():
	rta=""
	while rta != "no":
		biders= people()
		rta=str(input("Someone else to bid? yes or no "))
	Auction(biders)

start()





