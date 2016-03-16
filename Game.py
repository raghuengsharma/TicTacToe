from Player import Player
from Grid import Grid

class Game(object):
	#This is main class

	numMoves = 0 	# Number of moves.. At least 5 moves should have been passed
				# before checking the result..
	turn = None #turn can be set to Player1 or Player2's turn

	def run(self):
		#The game starts here
		grid = Grid()

		self.get_player_names()
		print "Hello %s and %s. " % (self.player1, self.player2)
		self.turn = self.player1

		#print grid



	def get_player_names(self):
		print "Welcome to my version of Tic Tac Toe.\
		\nThis is a 2 player game.\
		\nDo you want to enter player names now?\n"

		input = raw_input("Names?> ").upper()

		if input in ["Y", "YES"]:
			self.player1 = Player(raw_input("Player1 Name> "))
			self.player2 = Player(raw_input("Player2 Name> "))

		else:
			if input in ["N", "NO"]:
				print "That's ok."

			else:
				print "Invalid input."

			self.player1 = Player("Player1")
			self.player2 = Player("Player2")

	def toggle_turn(self, turn):
		#This must be called after every successful input
		if turn == self.player1:
			self.turn = self.player2
		elif turn == self.player2:
			self.turn = self.player2

	def is_finished(self):
		#Checks whether the game has ended. Also sets the Winner
		pass



