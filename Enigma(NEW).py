#enigma M3 (army, navy)
#https://www.cryptomuseum.com/crypto/enigma/index.htm
#https://piotte13.github.io/enigma-cipher/

from rotor import Rotor

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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


#TODO: make this non hardcoded!!!
create_reflector(ReflectorB)


#test delete this TODO
test = Rotor(rotor1,2,0)
print(test.get_key("A"))
print(test.get_key("B"))
#######