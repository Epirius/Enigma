

class Rotor:

	class_offset = [0, 0, 0]
	position_list = []
	Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def __init__(self, version, offset):
		self.position = len(Rotor.position_list)
		Rotor.position_list.append(self)

		self.version = version
		Rotor.class_offset[self.position] += offset
		self.rotor = self.assign_rotor(1)
		self.reverse_rotor = self.assign_rotor(2)
		self.notch = self.version[1]

	
	def out_of_range(self, number):
		if number > 25:
			number -= 26
		if number < 0:
			number += 26
		return number


	def assign_rotor(self, mode):
		#creates a dictionary with key = alphabet and value = version (rotor)
		
		
		if mode == 1:
			rotor = {}
			for i in range(26):
				rotor.setdefault(Rotor.Alphabet[i], self.version[0][i])
			return rotor

		if mode == 2:
			reverse_rotor = {}
			reverse_rotor.update({v: k for k, v in self.rotor.items()})
			return reverse_rotor

	
	def check_notch(self):
		#if a rotor rotates past it's notch, rotate the next rotor
		#TODO: this only works from position 1 to 2. fix it so we also check rotor 2!!!
		if self.position < len(Rotor.position_list) - 1:
			if ord(self.notch) - 65 == Rotor.class_offset[self.position]:
				Rotor.class_offset[self.position + 1] += 1

	
	def rotate(self):
		if self.position == 0:
			self.check_notch()
			print('---------')
			print(Rotor.class_offset)
			Rotor.class_offset[self.position] += 1
			print(Rotor.class_offset)
			print('---------')
			if Rotor.class_offset[self.position] > 25:
				Rotor.class_offset[self.position] -= 26
			if Rotor.class_offset[self.position] < 0:
				Rotor.class_offset[self.position] += 26


		#self.check_notch()
		# if self.position == 0:
		# 	self.offset += 1
		
		# if self.offset > 25:
		# 	self.offset -= 25

	
	def get_key(self, letter):
		self.rotate()
		self.letter = letter

		#making shure the input has the right format
		if isinstance(letter, str):
			self.letter = letter.upper()
			self.letter = ord(self.letter) - 65
			self.letter = self.out_of_range(self.letter)

		#adding offset
		self.letter += Rotor.class_offset[self.position]
		self.letter = self.out_of_range(self.letter)

		self.encrypted_letter = self.rotor[chr(self.letter + 65)]
		return Rotor.Alphabet.index(self.encrypted_letter)


	#get the key going through the rotor in the opposite direction
	def get_return_key(self, letter):
		self.letter = letter

		if isinstance(letter, str):
			self.letter = letter.upper()
			self.letter = ord(self.letter) - 65

		self.letter = self.out_of_range(self.letter)
		self.letter = self.reverse_rotor[chr(self.letter + 65)]
		self.letter = Rotor.Alphabet.index(self.letter)
		self.letter -= Rotor.class_offset[self.position]
		self.letter = self.out_of_range(self.letter)
		return self.letter
