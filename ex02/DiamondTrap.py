from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	def __init__(self, name, is_alive = True):
		super().__init__(name, is_alive)

	def set_eyes(self, new: str):
		self.eyes = new

	def set_hairs(self, new: str):
		self.hairs = new
	
	def get_eyes(self):
		return self.eyes
	
	def get_hairs(self):
		return self.hairs