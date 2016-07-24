class user():

    def __init__(self, name, symbol=None):
        self.username = name
        self.symbol = symbol
    def getUsername():
        return self.username
    def setSymbol(self, symbol):
        self.symbol = symbol
    def getSymbol(self):
        return self.symbol

class gameboard:

	def __init__(self):
		self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	def changeboard(self, square, sym):
		self.board[square - 1] = sym
	def getSpace(self, square):
		return self.board[square - 1]
	def reset(self):
		self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']