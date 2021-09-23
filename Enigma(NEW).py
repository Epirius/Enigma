#enigma M3 (army, navy)
#https://www.cryptomuseum.com/crypto/enigma/index.htm
#https://piotte13.github.io/enigma-cipher/

from rotor import Rotor

Alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor1 = ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
rotor2 = ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
rotor3 = ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
rotor4 = ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
rotor5 = ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

ReflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
ReflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


reflector_dict = {}
def create_reflector(version):
	for i in range(26):
		reflector_dict.setdefault(Alphabet[i], version[i])

def reflect(letter):
	letter = chr(letter + 65)
	letter = reflector_dict[letter]
	return Alphabet.index(letter)


#TODO: make this non hardcoded!!!
create_reflector(ReflectorB)


#test delete this TODO
r1 = Rotor(rotor1,0)
r2 = Rotor(rotor2,0)
r3 = Rotor(rotor3,0)

def enigma(message):
	message = message.upper()
	print(message)
	# print(rotor1)
	# print(Rotor.class_offset)
	message = r1.get_key(message)
	print(message)
	# print(rotor2)
	# print(Rotor.class_offset)
	message = r2.get_key(message)
	print(message)
	# # print(rotor3)
	# # print(Rotor.class_offset)
	message = r3.get_key(message)
	print(f'before rotor: {message}')
	message = reflect(message)
	print(f'after rotor: {message}')
	message = r3.get_return_key(message)
	print(message)
	message = r2.get_return_key(message)
	print(message)
	# message = r1.get_return_key(message)
	# message = Alphabet[message]
	# print(f"end: {message}")
	# # print()
	# # print()
	# # print()
	# # print()
	# # print()
	return message


enigma("a")
# print('-----------------------------')
# enigma("a")
# print('-----------------------------')
# enigma("a")
