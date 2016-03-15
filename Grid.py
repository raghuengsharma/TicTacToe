#The TicTacToe Grid
class Grid(object):
	# A grid has 9 (3x3) boxes.
	def __init__(self):
		#Initializing the Grid.
		self.boxes = [[],[],[]]
		for i in range(3):
			for j in range(3):
				self.boxes[i].append(Box("%s%s" % (i, j) ))

	def __repr__(self):
		boxString = ""
		for i in self.boxes:
			boxString += "\n"
			for j in i:
				boxString += "%s\t" % j
		return boxString

#The grid consists of these Boxes
class Box(object):
	possibleValue = {'X':0, 'O': 1}
	value = None
	immutable = False

	def __init__(self, value = None):
		self.setValue(value)

	#String representation of Box for Python interactive shell
	def __repr__(self):
		return self.value


	# String representation of Box;
	# Since __repr__ is already defined,
	# we don't explicitely need to define this method.
	# It will just override that... Will remove this later..
	def __str__(self):
		return self.value

	def setValue(self, value):
		self.value = value

	def getValue(self):
		return self.value

	# Box should only be updated if its not immutable (Except for initial values)
	def is_immutable(self):
		return self.immutable
