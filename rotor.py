#rotor


class Rotor:


	def __init__(self, version, position, offset):
		self.version = version
		self.position = position
		self.offset = offset
		self.rotor = self.assign_rotor()

	def assign_rotor(self):
		Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		rotor = {}
		for i in range(26):
			rotor.setdefault(Alphabet[i], self.version[0][i])
		return rotor

	def rotate(self):
		self.offset += 1

	def get_key(self, letter):
		temp_letter = ord(letter) + offset
		if (temp_letter - 64) > 26:
			temp_letter -= 26
