import curses as crs
"""
Gets the character value (as an int) of a cell in the board;

As blocks take up two curses-coordinate spaces,
a cell is defined as such, and its identifying
symbol will be in the righthand space;
In theory, the cell will either be empty (". "),
have an old block (two ACS_BLOCK chars),
or have an active block (two ACS_CKBOARD chars)
"""
def getCellValue(y, x, board):
	return board.inch(y, 2 * x)
"""
Sets the character values of a cell in the board
"""
def setCellValue(y, x, val, board):
	values = { \
		"EMPTY": '. ', \
		"ACTIVE": (crs.ACS_CKBOARD, crs.ACS_CKBOARD) \
	}
	colors = { \
		"ACTIVE-C": 3, \
		"ACTIVE-S": 2, \
		"ACTIVE-Z": 1, \
		"ACTIVE-L": 7, \
		"ACTIVE-R": 4, \
		"ACTIVE-I": 6, \
		"ACTIVE-T": 5 \
	}
	if val == "EMPTY":
		v = val
	else:
		v = "ACTIVE"
	i = 2 * x - 1
	for c in values[v]:
		if v != "ACTIVE":
			board.addch(y, i, c)
		else:
			board.addch(y, i, c, crs.color_pair(colors[val]))
		i += 1
# String that contains the ghost piece characters
ghostChars = "[]"
"""
Returns True if the indicated cell is empty
"""
def isCellEmpty(y, x, board):
	return y < 1 or getCellValue(y, x, board) in (ord(' '), ord(ghostChars[1]))
"""
Returns True if the indicated cell is a valid board space
"""
def isCellInBounds(y, x):
	return y < 21 and x > 0 and x < 11
"""
Return a list of y-addresses that are full of blocks
"""
def getFullLines(board):
	fullLines = []
	for y in range(20, 0, -1):
		full = True
		for x in range(1, 11):
			if isCellEmpty(y, x, board):
				full = False
				break
		if full:
			fullLines.append(y)
	return fullLines
"""
Returns True if the indicated line has no blocks in it
"""
def isLineEmpty(y, board):
	for x in range(1, 11):
		if isCellEmpty(y, x, board):
			continue
		else:
			return False
	return True

