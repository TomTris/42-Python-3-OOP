from abc import ABC, abstractmethod


class Character(ABC):
	"""My Abstract class"""
	def __init__(self, first_name, is_alive = True):
		"""Init first_name required, is_alive by default = True"""
		self.first_name = first_name
		self.is_alive = is_alive
	
	@abstractmethod
	def die(self):
		"""Change is_alive to False"""
		pass


class Stark(Character):
	"""A Drived Class"""
	
	def die(self):
		"""Change is_alive to False"""
		self.is_alive = False
