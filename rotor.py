

class Rotor:

	class_offset = [0, 0, 0]
	position_list = []

	def __init__(self, version, offset):
		self.position = len(Rotor.position_list)
		Rotor.position_list.append(self)

		self.version = version
		Rotor.class_offset[self.position] += offset
		self.rotor = self.assign_rotor(1)
		self.reverse_rotor = self.assign_rotor(2)

	
	def assign_rotor(self, mode):
		#creates a dictionary with key = alphabet and value = version (rotor)
		Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		
		if mode == 1:
			rotor = {}
			for i in range(26):
				rotor.setdefault(Alphabet[i], self.version[0][i])
			return rotor

		if mode == 2:
			reverse_rotor = {}
			reverse_rotor.update({v: k for k, v in self.rotor.items()})
			return reverse_rotor

	
	def check_notch(self):
		#TODO: there may be an issue on the second rotor, where this gets called to erly or to late.

		#checking if the letter we just left was a notch
		if (sclass_offset[self.position]) == (ord(self.version[1]) - 65):
			if self.position < 2:
				Rotor.position_list[(self.position + 1)].rotate()


	def rotate(self):
		self.check_notch()
		# if self.position == 0:
		# 	self.offset += 1
		
		# if self.offset > 25:
		# 	self.offset -= 25

	
	def get_key(self, letter):
		self.letter = letter

		if isinstance(letter, str):
			self.letter = letter.upper()
			self.letter = ord(self.letter) - 65

		self.letter += Rotor.class_offset[self.position]
		if self.letter > 25:
			self.letter -= 25
		self.encrypted_letter = self.rotor[chr(self.letter + 65)]
		#returns position of the encrypted letter in the rotor
		print()
		print(self.encrypted_letter)
		print(f'{self.position} my position' )
		print()
		return self.version[0].index(self.encrypted_letter)





#######################################################3

		# #add the offset to the letter before using that letter in the rotor
		# self.temp_letter = ord(letter) + self.offset 
		# if (self.temp_letter - 64) > 26:
		# 	self.temp_letter -= 26
		# self.temp_letter = chr(self.temp_letter)

		# #if this is the first rotor, then it should move after every letter.
		# #but i call it anyway because of other logic that should happen always.
		# self.rotate()

		# #using the letter in the rotor
		# return self.rotor.get(self.temp_letter)


	#get the key going through the rotor in the opposite direction
	def get_return_key(self, letter):
		self.temp_return_letter = ord(letter) + Rotor.class_offset[self.position]
		if (self.temp_return_letter - 64) > 26:
			self.temp_return_letter -= 26
		if self.position == 0:
			# FIXIT: this -1 is a bad fix. there is an off by one error only on return rotor 1. and i can't find the bug so i just have it -= 1 here. but the bug might break otherthings aswell so this is not ideal.
			# FIXIT: this fix works for the first letter but causes an of by one error for the next ones. so i need to find out why it is wrong to begin with to continue.
			#self.temp_return_letter -= 1
			K=1
		self.temp_return_letter = chr(self.temp_return_letter)


		return self.reverse_rotor.get(self.temp_return_letter)