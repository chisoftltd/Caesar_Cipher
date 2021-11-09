alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ciper = '''
        d8b        888                     
        Y8P        888                     
                   888                     
 .d8888b88888888b. 88888b.  .d88b. 888d888 
d88P"   888888 "88b888 "88bd8P  Y8b888P"   
888     888888  888888  88888888888888     
Y88b.   888888 d88P888  888Y8b.    888     
 "Y8888P88888888P" 888  888 "Y8888 888     
           888                             
           888                             
           888                   
'''
print(ciper)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def Caesar_Cipher(plain_text, shift_amount, cipher_direction):
	cipher_text = ""
	for letter in plain_text:
		position = alphabet.index(letter)
		if cipher_direction == 'encode':
			new_position = position + shift_amount
			cipher_text += alphabet[new_position]
		elif cipher_direction == 'decode':
			new_position = position - shift_amount
			cipher_text += alphabet[new_position]
		else:
			print("You have choosen wrong direction - encode or decode")
	print(f"The {cipher_direction} text is \'{cipher_text}\'")


Caesar_Cipher(plain_text=text, shift_amount=shift, cipher_direction=direction)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.