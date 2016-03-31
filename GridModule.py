import string

#The TicTacToe Grid
class Grid(object):
	# A grid has 9 (3x3) boxes.
	def __init__(self):
		#Initializing the Grid.
		self.boxes = [[],[],[]]
		for i in range(3):
			for j in range(3):
				self.boxes[i].append(Box("%s%s" % (i, j) ))
		self.map_input_to_box()

	def __repr__(self):
		boxString = ""
		for i in self.boxes:
			boxString += "\n"
			for j in i:
				boxString += "%s\t" % j
		return boxString

	def map_input_to_box(self):
		self.input_to_box = {}
		self.input_to_box["00"] = self.boxes[0][0]
		self.input_to_box["01"] = self.boxes[0][1]
		self.input_to_box["02"] = self.boxes[0][2]
		self.input_to_box["10"] = self.boxes[1][0]
		self.input_to_box["11"] = self.boxes[1][1]
		self.input_to_box["12"] = self.boxes[1][2]
		self.input_to_box["20"] = self.boxes[2][0]
		self.input_to_box["21"] = self.boxes[2][1]
		self.input_to_box["22"] = self.boxes[2][2]
		self.available_boxes = self.input_to_box.copy()

	def get_input(self, turn):
		#Get user input for proceeding in the game.
		#Don't return untill input is not valid.
		#Return input
		input_validity = False
		while not input_validity:
			current_input = raw_input(turn.get_prompt())
			if self.is_valid_input(current_input):
				#if box is empty, set input_validity "True" and return input
				current_box = self.input_to_box[current_input]
				if current_box.is_empty():
					current_box.set_filled()
					current_box.set_value(turn.get_weapon())
					input_validity = True
					self.available_boxes.pop(current_input)
					#return current_box
				else:
					print "Box is filled."
			else:
				print "Input is invalid. Try again."

	def is_valid_input(self, input):
		result = False
		if len(input) == 2:
			a = list(input)
			if a[0] in string.digits and a[1] in string.digits:
				if int(a[0]) < 3 and int(a[1]) < 3: #This means its a valid box.
					result = True
		return result

	def row_complete(self):
		for i in range(3):
			if self.boxes[i][0].get_value() == self.boxes[i][1].get_value()\
			 and self.boxes[i][1].get_value() == self.boxes[i][2].get_value():
				return True
		else:
			return False

	def column_complete(self):
		for j in range(3):
			if self.boxes[0][j].get_value() == self.boxes[1][j].get_value()\
			 and self.boxes[1][j].get_value() == self.boxes[2][j].get_value():
				return True
		else:
			return False

	def diagonal_complete(self):
		if self.boxes[0][0].get_value() == self.boxes[1][1].get_value()\
		 and self.boxes[1][1].get_value() == self.boxes[2][2].get_value():
			return True
		elif self.boxes[2][0].get_value() == self.boxes[1][1].get_value()\
		 and self.boxes[1][1].get_value() == self.boxes[0][2].get_value():
			return True
		else:
			return False


	def filled(self):
		if not self.available_boxes:
			return True
		else:
			return False


#The grid consists of these Boxes
class Box(object):
	value = None
	empty = True

	def __init__(self, value = None):
		self.set_value(value)

	#String representation of Box for Python interactive shell
	def __repr__(self):
		return self.value

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	# Box should only be updated if its empty (Except for initial values)
	def is_empty(self):
		return self.empty

	def set_filled(self):
		self.empty = False
