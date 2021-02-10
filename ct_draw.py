import curses as crs
"""
Data for piece geometry and color
"""
pieceSchema = {
	'C': {
		"color": 3,
		"dims": [4, 2],
		"sprites": {
			"" : [
				[1, 1, 1, 1],
				[1, 1, 1, 1]]
		}
	}, 'S': {
		"color": 2,
		"dims": [6, 3],
		"sprites": {
			'H': [
				[0, 0, 0, 0, 0, 0],
				[0, 0, 1, 1, 1, 1],
				[1, 1, 1, 1, 0, 0]],
			'V': [
				[1, 1, 0, 0, 0, 0],
				[1, 1, 1, 1, 0, 0],
				[0, 0, 1, 1, 0, 0]]
		}
	}, 'Z': {
		"color": 1,
		"dims": [6, 3],
		"sprites": {
			'H': [
				[0, 0, 0, 0, 0, 0],
				[1, 1, 1, 1, 0, 0],
				[0, 0, 1, 1, 1, 1]],
			'V': [
				[0, 0, 1, 1, 0, 0],
				[1, 1, 1, 1, 0, 0],
				[1, 1, 0, 0, 0, 0]]
		}
	}, 'L': {
		"color": 7,
		"dims": [6, 3],
		"sprites": {
			'H': [
				[0, 0, 1, 1, 0, 0],
				[0, 0, 1, 1, 0, 0],
				[0, 0, 1, 1, 1, 1]],
			'V': [
				[0, 0, 0, 0, 0, 0],
				[1, 1, 1, 1, 1, 1],
				[1, 1, 0, 0, 0, 0]],
			'HP': [
				[1, 1, 1, 1, 0, 0],
				[0, 0, 1, 1, 0, 0],
				[0, 0, 1, 1, 0, 0]],
			'VP': [
				[0, 0, 0, 0, 1, 1],
				[1, 1, 1, 1, 1, 1],
				[0, 0, 0, 0, 0, 0]]
		}
	}, 'R': {
		"color": 4,
		"dims": [6, 3],
		"sprites": {
			'H': [
				[0, 0, 1, 1, 0, 0],
				[0, 0, 1, 1, 0, 0],
				[1, 1, 1, 1, 0, 0]],
			'V': [
				[1, 1, 0, 0, 0, 0],
				[1, 1, 1, 1, 1, 1],
				[0, 0, 0, 0, 0, 0]],
			'HP': [
				[0, 0, 1, 1, 1, 1],
				[0, 0, 1, 1, 0, 0],
				[0, 0, 1, 1, 0, 0]],
			'VP': [
				[0, 0, 0, 0, 0, 0],
				[1, 1, 1, 1, 1, 1],
				[0, 0, 0, 0, 1, 1]]
		}
	}, 'I': {
		"color": 6,
		"dims": [8, 4],
		"sprites": {
			'H': [
				[0, 0, 1, 1, 0, 0, 0, 0],
				[0, 0, 1, 1, 0, 0, 0, 0],
				[0, 0, 1, 1, 0, 0, 0, 0],
				[0, 0, 1, 1, 0, 0, 0, 0]],
			'V': [
				[0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0],
				[1, 1, 1, 1, 1, 1, 1, 1],
				[0, 0, 0, 0, 0, 0, 0, 0]]
		}
	}, 'T': {
		"color": 5,
		"dims": [6, 3],
		"sprites": {
			'H': [
				[0, 0, 0, 0, 0, 0],
				[1, 1, 1, 1, 1, 1],
				[0, 0, 1, 1, 0, 0]],
			'V': [
				[0, 0, 1, 1, 0, 0],
				[1, 1, 1, 1, 0, 0],
				[0, 0, 1, 1, 0, 0]],
			'HP': [
				[0, 0, 1, 1, 0, 0],
				[1, 1, 1, 1, 1, 1],
				[0, 0, 0, 0, 0, 0]],
			'VP': [
				[0, 0, 1, 1, 0, 0],
				[0, 0, 1, 1, 1, 1],
				[0, 0, 1, 1, 0, 0]]
		}
	}
}
"""
Draws an alignment grid in the board window
"""
def drawGrid(board):
	for x in range(1, 21):
		for y in range(1, 21):
			board.addch(y, x, '.' if x % 2 != 0 else ' ')
"""
Erases the alignment grid in the board window
"""
def undrawGrid(board):
	for x in range(1, 21):
		for y in range(1, 21):
			board.addch(y, x, " ")
"""
Draws the bottom border in the board window
"""
def drawBoardBorder(board):
	board.addch(21, 0, crs.ACS_LTEE)
	for x in range(1, 21):
		board.addch(21, x, crs.ACS_HLINE)
	board.addch(21, 21, crs.ACS_RTEE)
"""
Checks if a character is in the play area of wBoard
"""
def isCharInBounds(y, x):
	return y > 0 and y < 21 and x > 0 and x < 21
"""
Draws a piece to a window (use wBoard or wNextP only!)

In order to allow for erasure a.k.a. undrawing of pieces,
the characters argument must either be a string or list,
and the character variable is actually a function;
When undrawing, the grid pattern is ". ", which are
two distinct characters, thus a two-member tuple
with indices 0 and 1 (False and True) can be used and
kept in sync with the x position of the cursor

The check is equals 0, hence even, because the board
starts at an x value of 1. Thus, if ['.', ' '] is passed
in for characters arg. (or ". " since strings are subscriptable),
the odd character cells will get a '.' from int(False)
and even cells will get a ' ' from int(True)

See README.md or check the bottom of this file for details on block behavoir
"""
def drawPiece(y, x, orient, piece, window, characters):
	doColor = False
	if len(characters) == 1:
		character = lambda x : characters[0]
		doColor = True
	elif len(characters) == 2:
		character = lambda x : characters[int(x % 2 == 0)]
	else:
		return None

	for i in range(x, x + pieceSchema[piece]["dims"][0]):
		for j in range(y, y + pieceSchema[piece]["dims"][1]):
			if isCharInBounds(j, i) \
				and bool(
					pieceSchema[piece]["sprites"][orient][j - y][i - x]
				):
					window.addch(
						j, i, character(i),
						crs.color_pair(pieceSchema[piece]["color"]) if doColor
						else crs.color_pair(0)
					)
"""
Redraws characters in a window.

Given a target character (B), and a region from
(xi, yi) to (xf, yf) where xi < xf and yi < yf,
any instances of the target char. in the window
will be overwritten with the result character (A)
"""
def changeTexture(yi, xi, yf, xf, characterA, characterB, window):
	if not (xi <= xf and yi <= yf):
		return None
	for i in range(xi, xf + 1):
		for j in range(yi, yf + 1):
			if type(characterB) is str and window.inch(j, i) == ord(characterB) \
				or type(characterB) is int and window.inch(j, i) % 0x100 == characterB % 0x100:
				window.addch(j, i, characterA)

