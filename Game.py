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
		print grid
		player1 = Player("Player1")
		player2 = Player("Player2")

	def is_finished(self):
		#Checks whether the game has ended. Also sets the Winner
		pass

	def getInput(self):
		#Get user input for proceeding in the game
		pass

