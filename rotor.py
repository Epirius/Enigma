#rotor


class Rotor:


	def __init__(self, version, position, offset):
		self.version = version
		self.position = position
		self.offset = offset
		self.rotor = self.assign_rotor()
		print(self.rotor)

	
	def assign_rotor(self):
		#creates a dictionary with key = alphabet and value = version (rotor)
		Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		rotor = {}
		for i in range(26):
			rotor.setdefault(Alphabet[i], self.version[0][i])
		return rotor

	
	def rotate(self):
		self.offset += 1

	
	def get_key(self, letter):
		#add the offset to the letter before using that letter in the rotor
		self.temp_letter = ord(letter) + self.offset
		if (self.temp_letter - 64) > 26:
			self.temp_letter -= 26
		self.temp_letter = chr(self.temp_letter)

		#if this is the first rotor, then it should move after every letter
		if self.position == 1:
			self.rotate()

		#using the letter in the rotor
		return self.rotor.get(self.temp_letter)