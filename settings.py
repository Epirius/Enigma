

rotor1 = 	("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
rotor2 = 	("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
rotor3 = 	("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
rotor4 = 	("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
rotor5 = 	("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

ReflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
ReflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"




#############################
###### change settings ######
#############################

message = "hello"

#choose between rotor1 ... rotor5
position1 = rotor1
position2 = rotor5
position3 = rotor3

#choose notch starting position (0..25)
offset1 = 0
offset2 = 0
offset3 = 0

#choose the reflector (B or C)
reflector = ReflectorB

#choose plug pairs
plug_pairs = {"A":"H", "L":"R"}

#############################






position_settings = [(position1, offset1), (position2, offset2), (position3, offset3)]
reflector_settings = reflector