class Mammal:
	def __init__(self, eyes, ears, limbs):
		self.eyes = eyes # not right approach, public
		self._ears = ears # also not right approach 
		self.__limbs = limbs # private, the way we do
	def get_eyes(self):
		return self.eyes 
	def get_ears(self):
		return self._ears 
	def get_limbs(self):
		return self.__limbs 

lamb = Mammal(2, 2, 4) # lamb is my instance, object
#print('Eyes: ', lamb.eyes)
print('Eyes: ', lamb.get_eyes())
print('Ears: ', lamb._ears)
#print('Limbs', lamb.__limbs)
print('Limbs: ', lamb.get_limbs())
