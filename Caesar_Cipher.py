def encrypt(alphabet):
	text = str(input("Type your message:\n").lower())
	shift = int(input("Type the shift number:\n"))
	cipher=" "
	for i in text:
		if i == " ":
			cipher+=" "
		else:
			position= alphabet.index(i)
			new_position = position + shift
			new_letter = alphabet[new_position]
			cipher+=new_letter
	print("The message is: "+cipher)


def decrypt(alphabet):
	text = input("Enter your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	descipher=""
	for i in text:
		if i == " ":
			descipher+=" "
		if i!=" ":
			position= alphabet.index(i)
			new_position = position - shift
			new_letter = alphabet[new_position]
			descipher+=new_letter
	print("The message is: "+descipher)


def start():
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	while direction != "no":
		if direction =="encode":
			encrypt(alphabet)
			direction = input("Type 'encode' to encrypt, type 'decode' to decrypt. If u want to exit type no: \n")

	
		if direction =="decode":
			decrypt(alphabet)
			direction = input("Type 'encode' to encrypt, type 'decode' to decrypt. If u want to exit type no: \n")

start()
