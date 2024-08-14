from S1E9 import Character

class Baratheon(Character):
	"""Representing the Baratheon family."""

	def __init__(self, name, is_alive = True):
		super().__init__(name, is_alive)
		self.family_name = "Baratheon"
		self.eyes = 'brown'
		self.hairs = 'dark'

class Lannister(Character):
	"""Representing the Baratheon family."""
	def __init__(self, name, is_alive = True):
		super().__init__(name, is_alive)
		self.family_name = "Lannister"
		self.eyes = 'blue'
		self.hairs = 'light'

	@classmethod
	def create_lannister(cls, name, is_alive = True):
		"""Create an instance"""
		return (cls(name, is_alive))
