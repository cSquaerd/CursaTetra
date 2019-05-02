import curses as crs
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
	COLOR_C = 3
	COLOR_S = 2
	COLOR_Z = 1
	COLOR_L = 7
	COLOR_R = 4
	COLOR_I = 6
	COLOR_T = 5
	if len(characters) == 1:
		character = lambda x : characters[0]
	elif len(characters) == 2:
		character = lambda x : characters[int(x % 2 == 0)]
	else:
		return None
	if piece == 'C':
		for i in range(x, x + 4):
			for j in range(y, y + 2):
				if isCharInBounds(j, i):
					window.addch(j, i, character(i) , crs.color_pair(COLOR_C))
	elif piece == 'S':
		if orient == 'H':
			for i in range(x + 2, x + 6):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i) , crs.color_pair(COLOR_S))
			for i in range(x, x + 4):
				if isCharInBounds(y + 2, i):
					window.addch(y + 2, i, character(i) , crs.color_pair(COLOR_S))
		else:
			for i in range(x, x + 2):
				for j in range(y, y + 2):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i) , crs.color_pair(COLOR_S))
			for i in range(x + 2, x + 4):
				for j in range(y + 1, y + 3):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_S))
	elif piece == 'Z':
		if orient == 'H':
			for i in range(x, x + 4):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i), crs.color_pair(COLOR_Z))
			for i in range(x + 2, x + 6):
				if isCharInBounds(y + 2, i):
					window.addch(y + 2, i, character(i), crs.color_pair(COLOR_Z))
		else:
			for i in range(x, x + 2):
				for j in range(y + 1, y + 3):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_Z))
			for i in range(x + 2, x + 4):
				for j in range(y, y + 2):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_Z))
	elif piece == 'L':
		if orient == 'H':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_L))
			for i in range(x + 4, x + 6):
				if isCharInBounds(y + 2, i):
					window.addch(y + 2, i, character(i), crs.color_pair(COLOR_L))
		elif orient == 'V':
			for i in range(x, x + 6):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i), crs.color_pair(COLOR_L))
			for i in range(x, x + 2):
				if isCharInBounds(y + 2, i):
					window.addch(y + 2, i, character(i), crs.color_pair(COLOR_L))
		elif orient == 'HP':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_L))
			for i in range(x, x + 2):
				if isCharInBounds(y, i):
					window.addch(y, i, character(i), crs.color_pair(COLOR_L))
		elif orient == 'VP':
			for i in range(x, x + 6):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i), crs.color_pair(COLOR_L))
			for i in range(x + 4, x + 6):
				if isCharInBounds(y, i):
					window.addch(y, i, character(i), crs.color_pair(COLOR_L))
	elif piece == 'R':
		if orient == 'H':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_R))
			for i in range(x, x + 2):
				if isCharInBounds(y + 2, i):
					window.addch(y + 2, i, character(i), crs.color_pair(COLOR_R))
		elif orient == 'V':
			for i in range(x, x + 6):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i), crs.color_pair(COLOR_R))
			for i in range(x, x + 2):
				if isCharInBounds(y, i):
					window.addch(y, i, character(i), crs.color_pair(COLOR_R))
		elif orient == 'HP':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_R))
			for i in range(x + 4, x + 6):
				if isCharInBounds(y, i):
					window.addch(y, i, character(i), crs.color_pair(COLOR_R))
		elif orient == 'VP':
			for i in range(x, x + 6):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i), crs.color_pair(COLOR_R))
			for i in range(x + 4, x + 6):
				if isCharInBounds(y + 2, i):
					window.addch(y + 2, i, character(i), crs.color_pair(COLOR_R))
	elif piece == 'I':
		if orient == 'H':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 4):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_I))
		else:
			for i in range(x, x + 8):
				if isCharInBounds(y + 2, i):
					window.addch(y + 2, i, character(i), crs.color_pair(COLOR_I))
	elif piece == 'T':
		if orient == 'H':
			for i in range(x, x + 6):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i), crs.color_pair(COLOR_T))
			for i in range(x + 2, x + 4):
				if isCharInBounds(y + 2, i):
					window.addch(y + 2, i, character(i), crs.color_pair(COLOR_T))
		elif orient == 'V':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_T))
			for i in range(x, x + 2):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i), crs.color_pair(COLOR_T))
		elif orient == 'HP':
			for i in range(x, x + 6):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i), crs.color_pair(COLOR_T))
			for i in range(x + 2, x + 4):
				if isCharInBounds(y, i):
					window.addch(y, i, character(i), crs.color_pair(COLOR_T))
		elif orient == 'VP':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					if isCharInBounds(j, i):
						window.addch(j, i, character(i), crs.color_pair(COLOR_T))
			for i in range(x + 4, x + 6):
				if isCharInBounds(y + 1, i):
					window.addch(y + 1, i, character(i), crs.color_pair(COLOR_T))
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

