# Alphabet ="  ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# rotor1 = ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
# rotor2 = ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
# rotor3 = ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
# rotor4 = ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
# rotor5 = ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

# ReflectorB = "  YRUHQSLDPXNGOKMIEBFZCWVJAT"
# ReflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

# print (Alphabet)
# print(rotor1)
# print(rotor2)
# print(rotor3)
# print(ReflectorB)

offset = 2
a="Y"

letter = ord(a) + offset
if (letter - 64) > 26:
	letter -= 26
letter = chr(letter)

print (letter)
###
###
