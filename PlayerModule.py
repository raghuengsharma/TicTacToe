class Player(object):

	def __init__(self, name):
		self.set_name(name)

	def __repr__(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_prompt(self):
		return self.name + "> "

	def set_weapon(self, weapon):
		self.weapon = weapon

	def get_weapon(self):
		return self.weapon
