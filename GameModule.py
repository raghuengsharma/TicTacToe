from PlayerModule import Player
from GridModule import Grid

class Game(object):
	#This is main class

	def __init__(self):
		self.num_moves = 0 	# Number of moves.. At least 5 moves should have been passed
					# before checking the result..
		self.turn = None #turn can be set to Player1 or Player2's turn

	def run(self):
		#The game starts here
		self.grid = Grid()

		self.get_player_names()
		print "Hello %s and %s. " % (self.player1, self.player2)
		self.turn = self.player1
		while True:
			print self.grid
			print "Moves: ", self.num_moves
			self.grid.get_input(self.turn)
			self.num_moves += 1
			if self.num_moves >= 5:
				if self.is_finished():
					break
			self.toggle_turn()

		print self.grid
		print "%s wins." % self.winner


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

		self.player1.set_weapon("X")
		self.player2.set_weapon("O")

	def toggle_turn(self):
		#This must be called after every successful input
		if self.turn == self.player1:
			self.turn = self.player2
		elif self.turn == self.player2:
			self.turn = self.player1

	def is_finished(self):
		#Checks whether the game has ended. Also sets the Winner
		game_over = False
		if self.grid.row_complete()\
		 or self.grid.column_complete()\
		 or self.grid.diagonal_complete():
			game_over = True
			self.winner = self.turn
		if self.grid.filled():
			game_over = True
			self.winner = None
		return game_over
