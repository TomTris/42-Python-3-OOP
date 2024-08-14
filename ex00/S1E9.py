from abc import ABC, abstractmethod


class Character(ABC):
	"""My Abstract class"""
	@abstractmethod
	def __init__(self, first_name, is_alive = True):
		self.first_name = first_name
		self.is_alive = is_alive
		"""Init first_name required, is_alive by default = True"""
	
	def die(self):
		"""Change is_alive to False"""
		pass


class Stark(Character):
	"""A Drived Class"""
	
	def __init__(self, first_name, is_alive = True):
		"""Change is_alive to False"""
		super().__init__(first_name, is_alive)
