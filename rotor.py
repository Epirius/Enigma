

class Rotor:


	position_list = []

	def __init__(self, version, offset):
		self.position = len(Rotor.position_list)
		Rotor.position_list.append(self)

		self.version = version
		self.offset = offset
		self.rotor = self.assign_rotor()

	
	def assign_rotor(self):
		#creates a dictionary with key = alphabet and value = version (rotor)
		Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		rotor = {}
		for i in range(26):
			rotor.setdefault(Alphabet[i], self.version[0][i])
		return rotor

	
	def check_notch(self):
		#TODO: there may be an issue on the second rotor, where this gets called to erly or to late.

		#checking if the letter we just left was a notch
		if (self.offset) == (ord(self.version[1]) - 65):
			if self.position < 2:
				Rotor.position_list[(self.position + 1)].rotate()


	def rotate(self):
		self.check_notch()
		if self.position == 0:
			self.offset += 1
		
		if self.offset > 25:
			self.offset -= 25

	
	def get_key(self, letter):
		#add the offset to the letter before using that letter in the rotor
		self.temp_letter = ord(letter) + self.offset
		if (self.temp_letter - 64) > 26:
			self.temp_letter -= 26
		self.temp_letter = chr(self.temp_letter)

		#if this is the first rotor, then it should move after every letter.
		#but i call it anyway because of other logic that should happen always.
		self.rotate()

		#using the letter in the rotor
		return self.rotor.get(self.temp_letter)


	