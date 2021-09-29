#enigma M3 (army, navy)
#https://www.cryptomuseum.com/crypto/enigma/index.htm
#https://piotte13.github.io/enigma-cipher/

from rotor import Rotor

Alphabet =	 "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor1 = 	("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
rotor2 = 	("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
rotor3 = 	("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
rotor4 = 	("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
rotor5 = 	("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

ReflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
ReflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


reflector_dict = {}
def create_reflector(version):
	for i in range(26):
		reflector_dict.setdefault(Alphabet[i], version[i])

def reflect(letter):
	if isinstance(letter, int):
		letter = chr(letter + 65)
	letter = reflector_dict[letter]
	return Alphabet.index(letter)


#TODO: make this non hardcoded!!!
create_reflector(ReflectorB)


#test delete this TODO
r1 = Rotor(rotor1,0)
r2 = Rotor(rotor2,0)
r3 = Rotor(rotor3,0)

def enigma(text):
	output = ""

	text = ''.join(filter(str.isalpha, text))
	text = text.upper()

	for message in text:
		message = r1.get_key(message)
		message = r2.get_key(message)
		message = r3.get_key(message)
		message = reflect(message)
		message = r3.get_return_key(message)
		message = r2.get_return_key(message)
		message = r1.get_return_key(message)
		output += chr(message+65) + " "
	return output


x= "E Y J L Q H T D O Y A N V W P Y P D A V D D W Z D Y G T P J W L X M E L Y N G V Y Q J T R N M N F B K N K H N D Y A I U U N A H R W S B T D O H L I L I D G J A B V V J G J L L T M B B R K T W O Y O E Y C X W R G U H I O F K M T E O G B E C Z L S F W A J Q B U X X S G F L B R H I L S S G Z H Z Z J O G S Y A D B Q Y M B F H Z D B B B S R X M L V D Q Y X Z P F B P D T L L J U E Q L D W M J M K R S P D K L A W Y W J H I Q A W C V F X E B V Z P O O S Z E F J C F A Y L Q D N Q A V I P W E F N P X L B U W L S P C H Z N X C F F X E M J X K Z I O E D I Z A I K V M K D Y V J L Y J N M E V R K A Z F I T S K G L Q Z W N M D S I A L W Y Q E F U T M Y V T F J A D S V S S U G C U K Z G P G R I Q V C W O X H W F M Y Y B W X K S G M I O E Q I M K A K P W M T J L W X G I I P N U L C N L O E O C X P L T E Q F O I V F A I S K A C O Y O B U I G D X D C I L V F A A V V R K O Z S F C T M I F I D Y B O T V R P G I W K P Y U C Y O C M E P E E N M D C Q K D H Y F S L A V C Q M H Y R D U M S G J Y V Q N P U C H V X K G L X C D C F M I F S R Q U Z A A Q U X K Z P V P X R W F B T W P D H L V A Z H S L E G C F D C L X R W T U Z Y A Z E G V C R U M A F E D F H F Q J O F G M T L P M B C C C U D S G I V N W S K R T S I U C F S S T C D T I X S E N M C O R L I Z E E C L M O X F I S A V B P G D V A O U R H M F S Z D Y Z U V U M Y M G N V R T X I H J F G C R L U G E E I E N H X P G T C R G U E G C Q E W Z I"
test= enigma(x)
print(".............................")
print(test)
