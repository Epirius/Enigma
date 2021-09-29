#enigma M3 (army, navy)
from rotor import Rotor
import settings


Alphabet =	 "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

reflector_dict = {}
def create_reflector(version):
	for i in range(26):
		reflector_dict.setdefault(Alphabet[i], version[i])

def reflect(letter):
	if isinstance(letter, int):
		letter = chr(letter + 65)
	letter = reflector_dict[letter]
	return Alphabet.index(letter)


def create_plug_board(plug_settings):
    plug_dict = plug_settings #{}
    # makes the dict 2-way
    plug_dict.update({v : k for k, v in plug_dict.items()})
    return plug_dict


def plug_board(char, plug_dict):
    if char in plug_dict:
        return plug_dict[char]
    else:
        return char


def enigma(text, plug_dict):
	output = ""

	text = ''.join(filter(str.isalpha, text))
	text = text.upper()

	for message in text:
		message = plug_board(message, plug_dict)
		message = r1.get_key(message)
		message = r2.get_key(message)
		message = r3.get_key(message)
		message = reflect(message)
		message = r3.get_return_key(message)
		message = r2.get_return_key(message)
		message = r1.get_return_key(message)
		message = chr(message+65)
		message = plug_board(message, plug_dict)
		output += message
	return output


create_reflector(settings.reflector_settings)

r1 = Rotor(settings.position_settings[0][0], settings.position_settings[0][1])
r2 = Rotor(settings.position_settings[1][0], settings.position_settings[1][1])
r3 = Rotor(settings.position_settings[2][0], settings.position_settings[2][1])

#creating plug_dict
plug_settings = settings.plug_pairs
plug_dict = create_plug_board(plug_settings)

#############################################

message = enigma(settings.message, plug_dict)
# print(".............................")
print(message)

