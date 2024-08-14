from S1E9 import Character

class Baratheon(Character):
	"""Representing the Baratheon family."""
	
	def __init__(self, name, is_alive = True):
		super().__init__(name, is_alive)
		self.family_name = "Baratheon"
		self.eyes = 'brown'
		self.hairs = 'dark'
	
	def die(self):
		"""Change is_alive to False"""
		self.is_alive = False

	def __str__(self):
		return(f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})")
	
	def __repr__(self):
		return(f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})")

class Lannister(Character):
	"""Representing the Baratheon family."""
	def __init__(self, name, is_alive = True):
		super().__init__(name, is_alive)
		self.family_name = "Lannister"
		self.eyes = 'blue'
		self.hairs = 'light'

	def die(self):
		"""Change is_alive to False"""
		self.is_alive = False
	
	@classmethod
	def create_lannister(cls, name, is_alive = True):
		"""Create an instance"""
		return (cls(name, is_alive))
	
	def __str__(self):
		return(f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})")
	
	def __repr__(self):
		return(f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})")

