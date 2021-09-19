#enigma M3 (army, navy)
#https://www.cryptomuseum.com/crypto/enigma/index.htm
#https://piotte13.github.io/enigma-cipher/

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Rotor1 = ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
Rotor2 = ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
Rotor3 = ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
Rotor4 = ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
Rotor5 = ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

ReflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
ReflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


reflector_dict = {}
def create_reflector(version):
	for i in range(26):
		reflector_dict.setdefault(Alphabet[i], version[i])


#TODO: make this non hardcoded!!!
create_reflector(ReflectorB)