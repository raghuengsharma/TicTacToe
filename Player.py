class Player(object):
	name = ""

	def __init__(self, name):
		self.setName(name)

	def getName(self):
		return name

	def setName(self, name):
		self.name = name
