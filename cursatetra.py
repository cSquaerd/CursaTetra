# SECTION: IMPORTS
import curses as crs
import os
import time
import random as rnd
import sys
import json
# SECTION: VERSION CHECK
if sys.version_info[0] < 3:
	print("This game requires Python 3. Please install it and/or run this file with it.")
	exit()
# SECTION: FUNCTIONS
"""
Draws an alignment grid in the board window
"""
def drawGrid():
	for x in range(1, 21):
		for y in range(1, 21):
			wBoard.addch(y, x, '.' if x % 2 != 0 else ' ')
"""
Erases the alignment grid in the board window
"""
def undrawGrid():
	for x in range(1, 21):
		for y in range(1, 21):
			wBoard.addch(y, x, " ")
"""
Draws the bottom border in the board window
"""
def drawBoardBorder():
	wBoard.addch(21, 0, crs.ACS_LTEE)
	for x in range(1, 21):
		wBoard.addch(21, x, crs.ACS_HLINE)
	wBoard.addch(21, 21, crs.ACS_RTEE)
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
	COLOR_C = 1
	COLOR_S = 2
	COLOR_Z = 3
	COLOR_L = 4
	COLOR_R = 5
	COLOR_I = 6
	COLOR_T = 7
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
"""
Returns the number of base-10 digits in a number (n)
"""
def numDigits(n):
	if n == 0:
		return 1
	m = 0;
	while n >= 10 ** m:
		m += 1
	return m
# Tuple containing score label IDs for score functions
scoreLabels = ('', "SCORE", "LINES", '', "STATC", "STATS", "STATZ", \
	"STATL", "STATR", "STATI", "STATT", '', "STAT1", "STAT2", \
	"STAT3", "STAT4")
"""
Writes a score value to a score label, listed above
"""
def writeScore(score, scoreType):
	scoreIndex = scoreLabels.index(scoreType)
	if scoreIndex < 3:
		wScore.addstr(scoreIndex, 16 - numDigits(score), str(score))
	else:
		wStats.addstr(scoreIndex, 18 - numDigits(score), str(score))
"""
Clears a score label
"""
def clearScore(scoreType):
	scoreIndex = scoreLabels.index(scoreType)
	if scoreIndex < 3:
		wScore.addstr(scoreIndex, 9, "      0")
	else:
		wStats.addstr(scoreIndex, 11, "      0")

"""
Writes a label to the lower section of the board;

The label can be left, center, or right aligned;
If the align argument is a string representation of
an integer, then the label will be written starting at
the numbered cell and will wrap around, allowing
for scrolling labels with repeated calls
"""
def writeBoardLabel(align, label):
	if align == 'L':
		x = 1
	elif align == 'C':
		x = (20 - len(label)) // 2 + 1
	elif align == 'R':
		x = 21 - len(label)
	else:
		x = int(align) - 1
		for c in label:
			wBoard.addch(22, x % 20 + 1, c)
			x += 1
		return None

	wBoard.addstr(22, x, label)
	wBoard.refresh()
"""
Clears the lower section of the board
"""
def clearBoardLabel():
	wBoard.addstr(22, 1, 20 * ' ')
"""
Gets the character value (as an int) of a cell in the board;

As blocks take up two curses-coordinate spaces,
a cell is defined as such, and its identifying
symbol will be in the righthand space;
In theory, the cell will either be empty (". "),
have an old block (two ACS_BLOCK chars),
or have an active block (two ACS_CKBOARD chars)
"""
def getCellValue(y, x):
	return wBoard.inch(y, 2 * x)
"""
Sets the character values of a cell in the board
"""
def setCellValue(y, x, val):
	values = { \
		"EMPTY": '. ', \
		"ACTIVE": (crs.ACS_CKBOARD, crs.ACS_CKBOARD) \
	}
	colors = { \
		"ACTIVE-C": 1, \
		"ACTIVE-S": 2, \
		"ACTIVE-Z": 3, \
		"ACTIVE-L": 4, \
		"ACTIVE-R": 5, \
		"ACTIVE-I": 6, \
		"ACTIVE-T": 7 \
	}
	if val == "EMPTY":
		v = val
	else:
		v = "ACTIVE"
	i = 2 * x - 1
	for c in values[v]:
		if v != "ACTIVE":
			wBoard.addch(y, i, c)
		else:
			wBoard.addch(y, i, c, crs.color_pair(colors[val]))
		i += 1
# String that contains the ghost piece characters
ghostChars = "[]"
# Boolean that enables the ghost piece
# (Werid stuff happens if it changes during a game)
doGhost = True
"""
Returns True if the indicated cell is empty
"""
def isCellEmpty(y, x):
	return y < 1 or getCellValue(y, x) in (ord(' '), ord(ghostChars[1]))
"""
Returns True if the indicated cell is a valid board space
"""
def isCellInBounds(y, x):
	return y < 21 and x > 0 and x < 11
"""
Return a list of y-addresses that are full of blocks
"""
def getFullLines():
	fullLines = []
	for y in range(20, 0, -1):
		full = True
		for x in range(1, 11):
			if isCellEmpty(y, x):
				full = False
				break
		if full:
			fullLines.append(y)
	return fullLines
"""
Returns True if the indicated line has no blocks in it
"""
def isLineEmpty(y):
	for x in range(1, 11):
		if isCellEmpty(y, x):
			continue
		else:
			return False
	return True
"""
Class for active block data

* Valid Constructor Values:
	* y: [1, 19]
		* Smallest block height-wise is Square, S, and Z; All take up two cells vertically
	* x: [1, 10]
	* pID: {'C', 'S', 'Z', 'L', 'R', 'I', 'T'}
	* orient: {'', 'H', 'V', 'HP', 'VP'}
		* Null-orientation is only valid for the Square

* Methods & Valid Values:
	* draw(): Draws the piece on the board
	* undraw(): Erases the piece from the board
	* getGhostDepth(): Determines the y-position of the ghost piece
	* drawGhost(): Draws the ghost piece on the board
	* undrawGhost(): Erases the ghost piece from the board
	* getNewOrient(rotDir): Gets the new orientation for the piece based on rot. dir.
		* rotDir: {'CW', 'CCW'}
			* Clockwise or Counter-Clockwise
			* Only needed for L, R, and T pieces
	* rotate(rotDir): Rotates the piece in the indicated rot. dir.
		* rotDir: See notes in getNewOrient
	* move(direction): Moves the piece in the indicated direction
		* direction: {'L', 'R', 'D'}
			* Left, Right, or Down
	* canRotate(rotDir): Returns True if the piece can rotate in the indicated rot. dir.
		* rotDir: See notes in getNewOrient
	* canMove(direction): Returns True if the piece can move in the indicated direction
		* direction: See notes in move
"""
class Piece:
	def __init__(self, y, x, p, o):
		self.y = y
		self.x = x
		self.pID = p
		self.orient = o
		self.hasLanded = False
		self.ghostDepth = 0
		self.drawGhost()
		self.draw()
	def draw(self):
		drawPiece(self.y, 2 * self.x - 1, self.orient, self.pID, wBoard, [crs.ACS_CKBOARD])
	def undraw(self):
		drawPiece(self.y, 2 * self.x - 1, self.orient, self.pID, wBoard, ". ")
	def getGhostDepth(self):
		originalY = self.y
		while self.canMove('D'):
			self.y += 1
		self.ghostDepth = self.y
		self.y = originalY
	def drawGhost(self):
		if not doGhost:
			return None
		self.getGhostDepth()
		drawPiece( \
			self.ghostDepth, 2 * self.x - 1, \
			self.orient, self.pID, wBoard, \
			ghostChars \
		)
	def undrawGhost(self):
		if not doGhost:
			return None
		drawPiece(self.ghostDepth, 2 * self.x - 1, self.orient, self.pID, wBoard, ". ")
	def getNewOrient(self, rotDir):
		if self.pID == 'C':
			return ''
		elif self.pID in ('S', 'Z', 'I'):
			return 'V' if self.orient == 'H' else 'H'
		elif self.pID in ('L', 'R', 'T'):
			if self.orient == 'H':
				if rotDir == 'CW':
					return 'V'
				elif rotDir == 'CCW':
					return 'VP'
			elif self.orient == 'V':
				if rotDir == 'CW':
					return 'HP'
				elif rotDir == 'CCW':
					return 'H'
			elif self.orient == 'HP':
				if rotDir == 'CW':
					return 'VP'
				elif rotDir == 'CCW':
					return 'V'
			elif self.orient == 'VP':
				if rotDir == 'CW':
					return 'H'
				elif rotDir == 'CCW':
					return 'HP'
	def rotate(self, rotDir):
		self.undraw()
		self.undrawGhost()
		self.orient = self.getNewOrient(rotDir)
		self.drawGhost()
		self.draw()
	def move(self, direction):
		yShift = 1 if direction == 'D' else 0
		xShift = 1 if direction == 'R' else -1 if direction == 'L' else 0
		self.undraw()
		self.undrawGhost()
		self.y += yShift
		self.x += xShift
		self.drawGhost()
		self.draw()
	def canRotate(self, direction):
		if self.pID == 'S':
			if self.orient == 'H' and isCellEmpty(self.y, self.x) and \
				isCellEmpty(self.y + 1, self.x):
				return True
			elif self.orient == 'V' and isCellEmpty(self.y + 1, self.x + 2) and \
				isCellEmpty(self.y + 2, self.x) and \
				isCellInBounds(self.y + 2, self.x + 2):
				return True
		elif self.pID == 'Z':
			if self.orient == 'H' and isCellEmpty(self.y, self.x + 1) and \
				isCellEmpty(self.y + 2, self.x):
				return True
			elif self.orient == 'V' and isCellEmpty(self.y + 2, self.x + 1) and \
				isCellEmpty(self.y + 2, self.x + 2) and \
				isCellInBounds(self.y + 2, self.x + 2):
				return True
		elif self.pID == 'L':
			if self.orient == 'H':
				if direction == 'CW' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 1, self.x) and isCellEmpty(self.y + 2, self.x) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
				elif direction == 'CCW' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 1, self.x) and isCellEmpty(self.y, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
			elif self.orient == 'V':
				if direction == 'CW' and isCellEmpty(self.y, self.x) and \
					isCellEmpty(self.y, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 1):
					return True
				elif direction == 'CCW' and isCellEmpty(self.y, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
			elif self.orient == 'HP':
				if direction == 'CW' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x) and isCellEmpty(self.y, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
				elif direction == 'CCW' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x) and isCellEmpty(self.y + 2, self.x) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
			elif self.orient == 'VP':
				if direction == 'CW' and isCellEmpty(self.y, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
				elif direction == 'CCW' and isCellEmpty(self.y, self.x) and \
					isCellEmpty(self.y, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 1):
					return True
		elif self.pID == 'R':
			if self.orient == 'H':
				if direction == 'CW' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x) and isCellEmpty(self.y, self.x) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
				elif direction == 'CCW' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x) and isCellEmpty(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
			elif self.orient == 'V':
				if direction == 'CW' and isCellEmpty(self.y, self.x + 1) and \
					isCellEmpty(self.y, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 1):
					return True
				elif direction == 'CCW' and isCellEmpty(self.y, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x):
					return True
			elif self.orient == 'HP':
				if direction == 'CW' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 1, self.x) and isCellEmpty(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
				elif direction == 'CCW' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y, self.x) and isCellEmpty(self.y + 1, self.x) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
			elif self.orient == 'VP':
				if direction == 'CW' and isCellEmpty(self.y, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x + 1):
					return True
				elif direction == 'CCW' and isCellEmpty(self.y, self.x + 1) and \
					isCellEmpty(self.y, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 1):
					return True
		elif self.pID == 'I':
			if self.orient == 'H' and isCellInBounds(self.y + 3, self.x + 3) and \
				isCellInBounds(self.y + 3, self.x) and \
				isCellEmpty(self.y + 2, self.x) and \
				isCellEmpty(self.y + 2, self.x + 2) and \
				isCellEmpty(self.y + 2, self.x + 3):
				return True
			elif self.orient == 'V' and isCellInBounds(self.y + 3, self.x + 1) and \
				isCellEmpty(self.y, self.x + 1) and \
				isCellEmpty(self.y + 1, self.x + 1) and \
				isCellEmpty(self.y + 3, self.x + 1):
				return True
		elif self.pID == 'T':
			if self.orient == 'H' and isCellEmpty(self.y, self.x + 1):
				return True
			elif self.orient == 'V' and isCellEmpty(self.y + 1, self.x + 2) and \
				isCellInBounds(self.y + 2, self.x + 2):
				return True
			elif self.orient == 'HP' and isCellEmpty(self.y + 2, self.x + 1):
				return True
			elif self.orient == 'VP' and isCellEmpty(self.y + 1, self.x) and \
				isCellInBounds(self.y + 2, self.x):
				return True
		return False
	def canMove(self, direction):
		if self.pID == 'C':
			if direction == 'L' and isCellInBounds(self.y + 1, self.x - 1) and \
				isCellEmpty(self.y, self.x - 1) and \
				isCellEmpty(self.y + 1, self.x - 1):
				return True
			elif direction == 'R' and isCellInBounds(self.y + 1, self.x + 2) and \
				isCellEmpty(self.y, self.x + 2) and \
				isCellEmpty(self.y + 1, self.x + 2):
				return True
			elif direction == 'D' and isCellInBounds(self.y + 2, self.x) and \
				isCellEmpty(self.y + 2, self.x) and \
				isCellEmpty(self.y + 2, self.x + 1):
				return True
		elif self.pID == 'S':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 1):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x):
					return True
		elif self.pID == 'Z':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 1):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x) and \
					isCellEmpty(self.y + 2, self.x + 1):
					return True
		elif self.pID == 'L':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y, self.x) and \
					isCellEmpty(self.y + 1, self.x) and \
					isCellEmpty(self.y + 2, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 2):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x - 1):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y + 2, self.x + 1):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x) and \
					isCellEmpty(self.y + 2, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
			if self.orient == 'HP':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x) and \
					isCellEmpty(self.y + 2, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 1, self.x):
					return True
			elif self.orient == 'VP':
				if direction == 'L' and isCellInBounds(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y, self.x + 1):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
		elif self.pID == 'R':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x) and \
					isCellEmpty(self.y, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x + 1):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y, self.x + 1):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
			if self.orient == 'HP':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y, self.x) and \
					isCellEmpty(self.y + 1, self.x) and \
					isCellEmpty(self.y + 2, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y, self.x + 3) and \
					isCellEmpty(self.y, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 1, self.x + 2):
					return True
			elif self.orient == 'VP':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x + 1):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y + 2, self.x + 3):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 2) and \
					isCellEmpty(self.y + 3, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x):
					return True
		elif self.pID == 'I':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y, self.x) and \
					isCellEmpty(self.y + 1, self.x) and \
					isCellEmpty(self.y + 2, self.x) and \
					isCellEmpty(self.y + 3, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 3, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 3, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 4, self.x + 1) and \
					isCellEmpty(self.y + 4, self.x + 1):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x - 1):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 4) and \
					isCellEmpty(self.y + 2, self.x + 4):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 2) and \
					isCellEmpty(self.y + 3, self.x + 3):
					return True
		elif self.pID == 'T':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x) and \
					isCellEmpty(self.y, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x + 2) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x):
					return True
			elif self.orient == 'HP':
				if direction == 'L' and isCellInBounds(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
			elif self.orient == 'VP':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y, self.x) and \
					isCellEmpty(self.y + 1, self.x) and \
					isCellEmpty(self.y + 2, self.x):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 2, self.x + 2):
					return True
		return False
"""
Main function

Contains event loop for handling keypresses,
scoring and statistics variables, and other
vital functionality
"""
def ctMain():
	# SECTION: CONTORL DICTIONARIES AND TUPLES
	scoreData = { \
		"SCORE": 0, \
		"LINES": 0, \
		"STATC": 0, \
		"STATS": 0, \
		"STATZ": 0, \
		"STATL": 0, \
		"STATR": 0, \
		"STATI": 0, \
		"STATT": 0, \
		"STAT1": 0, \
		"STAT2": 0, \
		"STAT3": 0, \
		"STAT4": 0 \
	}
	keyCodes = { \
		crs.KEY_LEFT : 'L', \
		crs.KEY_RIGHT : 'R', \
		crs.KEY_UP : 'U', \
		crs.KEY_DOWN : 'D', \
		ord(' ') : "SPACE", \
		ord('\0') : "NULL", \
		27 : "ESC", \
		ord('Q') : 'Q', \
		ord('q') : 'Q' \
	}
	arrowCodes = ('L', 'R', 'D', 'U')
	rotateCodes = ("SPACE", "NULL")
	yesnoCodes = {ord('\n') : 'ENTER', ord('y') : 'y', ord('Y') : 'Y', \
		ord('n') : 'n', ord('N') : 'N'}
	yesCodes = {ord('\n') : 'ENTER', ord('y') : 'y', ord('Y') : 'Y'}
	noCodes = {ord('n') : 'n', ord('N') : 'N'}
	menuCodes = {27 : "ESC", ord('q') : 'Q', ord('Q') : 'Q', \
		ord('\n') : "ENTER", ord('G') : 'G', ord('g') : 'G'}
	startCodes = {ord('q') : 'Q', ord('Q') : 'Q', ord(' ') : "SPACE"}
	dropTimes = (0.75, 0.6, 0.5, 0.425, 0.35, 0.3, 0.25, 0.200, 0.15, 0.1)
	lineClearChars = (crs.ACS_S1, crs.ACS_S3, crs.ACS_S7, crs.ACS_S9)
	lineClearScores = (0, 40, 100, 300, 1200)
	lineClearDiffShifts = (10, 20, 30, 45, 60, 75, 95, 115, 140, 165)
	pieceInfo = { \
		'C': {'y': 1, 'x': 5, "orient" : '', "yn": 3, "xn": 5}, \
		'S': {'y': 0, 'x': 4, "orient" : 'H', "yn": 2, "xn": 5}, \
		'Z': {'y': 0, 'x': 4, "orient" : 'H', "yn": 2, "xn": 5}, \
		'L': {'y': 0, 'x': 4, "orient" : 'V', "yn": 2, "xn": 5}, \
		'R': {'y': 0, 'x': 4, "orient" : 'VP', "yn": 2, "xn": 5}, \
		'I': {'y': -1, 'x': 4, "orient" : 'V', "yn": 1, "xn": 3}, \
		'T': {'y': 0, 'x': 4, "orient" : 'H', "yn": 2, "xn": 5}, \
	}
	letters = tuple(range(0x41, 0x41 + 26)) + tuple(range(0x61, 0x61 + 26))
	# SECTION: CONTROL VARIABLES AND BOOLEANS
	cellValues = { \
		ord(' '): "EMPTY", \
		crs.ACS_CKBOARD + 0x100: "ACTIVE-C", \
		crs.ACS_CKBOARD + 0x200: "ACTIVE-S", \
		crs.ACS_CKBOARD + 0x300: "ACTIVE-Z", \
		crs.ACS_CKBOARD + 0x400: "ACTIVE-L", \
		crs.ACS_CKBOARD + 0x500: "ACTIVE-R", \
		crs.ACS_CKBOARD + 0x600: "ACTIVE-I", \
		crs.ACS_CKBOARD + 0x700: "ACTIVE-T" \
	}
	active = True
	playing = False
	paused = False
	pieceInPlay = False
	pieceToDrop = False
	pieceDropped = False
	dropDelay = True
	pieceJustSpawned = False
	difficulty = -1
	trueRandom = False
	pieceBag = list(pieceInfo.keys())
	rnd.shuffle(pieceBag)
	bagIndex = 0
	nextPID = pieceBag[bagIndex % 7]
	softDrops = 0
	checkScore = False
	scoreFileName = ".ctHiScrs.json"
	scoreFileWrite = False
	global doGhost
	# SECTION: HIGH SCORE PREP
	try:
		scoreFile = open(scoreFileName, 'r')
		highScores = json.loads(scoreFile.read())
		scoreFile.close()
		tempKeys = list(highScores.keys())
		for k in tempKeys:
			highScores[int(k)] = highScores[k]
			del highScores[k]
	except FileNotFoundError:
		highScores = {}
		for i in range(1, 11):
			highScores[i] = {"SCORE": 0, "NAME": "...", "LINES": 0}
		scoreFile = open(scoreFileName, 'w')
		scoreFile.write(json.dumps(highScores, sort_keys = True, indent = 2))
		scoreFile.close()
	# SECTION: HIGH SCORE WRITE FUNCTIONS
	def writeHighScores():
		if highScores[1]["SCORE"] == 0:
			return None
		wBoard.addch(4, 1, crs.ACS_LTEE)
		wBoard.addch(4, 20, crs.ACS_RTEE)
		for i in range(18):
			wBoard.addch(4, 2 + i, crs.ACS_HLINE)
		wBoard.addstr(4, 5, "HIGH SCORES:")
		i = 1
		while i <= 10 and highScores[i]["SCORE"] > 0:
			wBoard.addstr(4 + i, 1, 20 * ' ')
			wBoard.addstr( \
				4 + i, 1, \
				str(i) + ". " + highScores[i]["NAME"] + ":" + \
				str(highScores[i]["SCORE"]) + ", " + str(highScores[i]["LINES"]) \
			)
			i += 1
		wBoard.refresh()
	# SECTION: ACTIVE LOOP
	while active:
		# SUBSECTION: HIGH SCORE WRITE
		if checkScore:
			place = 11
			for i in range(10, 0, -1):
				if scoreData["SCORE"] > highScores[i]["SCORE"]:
					place = i
				else:
					break
			if place < 11:
				wBoard.nodelay(False)
				nameEntered = False
				while not nameEntered:
					undrawGrid()
					wBoard.addstr(1, 1, "CONGRATULATIONS!")
					wBoard.addstr(2, 1, "YOUR SCORE PUTS YOU")
					wBoard.addstr(3, 1, "AT RANK " + str(place) + "!")
					wBoard.addstr(4, 1, "PLEASE ENTER YOUR")
					wBoard.addstr(5, 1, "INITIALS:")
					wBoard.refresh()
					k = -1
					l = 0
					s = ''
					while l < 3:
						while k not in letters:
							k = wBoard.getch()
						wBoard.addstr(5, 11 + l, chr(k))
						s += chr(k)
						wBoard.refresh()
						l += 1
						k = -1
					wBoard.addstr(6, 1, "ARE YOU INITIALS")
					wBoard.addstr(7, 1, "CORRECT? [Y/N]")
					wBoard.refresh()
					k = -1
					while k not in yesnoCodes:
						k = wBoard.getch()
					if k in yesCodes:
						wBoard.addstr(8, 1, "SAVING SCORE...")
						wBoard.refresh()
						crs.delay_output(1000)
						nameEntered = True
						wBoard.nodelay(True)
						continue
					else:
						wBoard.addstr(8, 1, "OKAY, ENTER AGAIN.")
						wBoard.refresh()
						crs.delay_output(500)
						continue
				tempEntry = {}
				tempEntry["SCORE"] = scoreData["SCORE"]
				tempEntry["NAME"] = s
				tempEntry["LINES"] = scoreData["LINES"]
				for j in range(10, place, -1):
					highScores[j] = highScores[j - 1]
				highScores[place] = tempEntry
				scoreFileWrite = True
			else:
				checkScore = False
				continue
			if scoreFileWrite:
				scoreFile = open(scoreFileName, 'w')
				scoreFile.write(json.dumps(highScores, sort_keys = True, indent = 2))
				scoreFile.close()
				undrawGrid()
				wBoard.addstr(1, 1, "SAVED! PRESS SPACE")
				wBoard.addstr(2, 1, "FOR A NEW GAME, OR Q")
				wBoard.addstr(3, 1, "TO QUIT.")
				wBoard.refresh()
				scoreFileWrite = False
				checkScore = False
		# SUBSECTION: STARTUP CONTROL
		if not playing:
			writeHighScores()
			# Wait for a keypress
			wBoard.nodelay(False)
			k = -1
			while k not in startCodes:
				k = wBoard.getch()
			# Quit the game
			if startCodes[k] == 'Q':
				clearBoardLabel()
				writeBoardLabel('C', "QUITTING...")
				crs.delay_output(750)
				active = False
				continue
			# Start the game
			playing = True
			clearBoardLabel()
			writeBoardLabel('L', "DIFFICULTY SELECTION")
			crs.delay_output(500)
			sure = False
			# Select randomizer and difficulty
			while not sure:
				undrawGrid()
				wBoard.addstr(1, 1, "PRESS \'B\' FOR 7-BAG")
				wBoard.addstr(2, 1, "RANDOMIZER OR \'R\'")
				wBoard.addstr(3, 1, "FOR TRUE RANDOMIZER")
				wBoard.refresh()
				r = 0
				while r not in (ord('B'), ord('b'), ord('R'), ord('r')):
					r = wBoard.getch()
				if chr(r).upper() == 'R':
					trueRandom = True
				elif chr(r).upper() == 'B':
					trueRandom = False
				wBoard.addstr(4, 1, "PRESS A NUMBER 0-9")
				wBoard.addstr(5, 1, "TO SET DIFFICULTY:")
				wBoard.refresh()
				# The ASCII number-key codes in hexidecimal
				# Have the number as the first digit
				k = 0
				while k < 0x30 or k > 0x39:
					k = wBoard.getch()
				difficulty = k - 0x30
				# Confirm difficulty
				wBoard.addstr(6, 1, "YOU CHOSE DIFF. " + str(difficulty))
				wBoard.addstr(7, 1, "AND RANDOMIZER " + chr(r).upper())
				wBoard.addstr(8, 1, "ARE YOU SURE? [Y/N]")
				wBoard.refresh()
				k = 0
				while k not in yesnoCodes:
					k = wBoard.getch()
				# Proceed to game start
				if k in yesCodes:
					sure = True
					wBoard.addstr(9, 1, "OKAY, GET READY!")
					wBoard.refresh()
					crs.delay_output(500)
				# Retry difficulty selection
				else:
					undrawGrid()
					wBoard.addstr(1, 1, "OKAY, CHOOSE AGAIN.")
					wBoard.refresh()
				crs.delay_output(1000)
				drawGrid()
			clearBoardLabel()
			writeBoardLabel('C', "BEGINNING GAME...")
			crs.delay_output(750)
			# Clear old scores
			for s in scoreData.keys():
				scoreData[s] = 0
				clearScore(s)
			wScore.refresh()
			wStats.refresh()
			clearBoardLabel()
			writeBoardLabel('C', "LEVEL " + str(difficulty))
			wBoard.nodelay(True)
			continue
		# SUBSECTION: PAUSE MENU CONTROL
		if paused:
			# Get a key and either quit, toggle the ghost piece, or continue
			wBoard.nodelay(False)
			k = -1
			while k not in menuCodes :
				k = wBoard.getch()
			keypress = menuCodes[k]
			# Quit the game
			if keypress == 'Q':
				clearBoardLabel()
				writeBoardLabel('C', "PRESS ENTER TO QUIT")
				# To avoid accidental quits, confirm with enter key
				if wBoard.getch() == ord('\n'):
					clearBoardLabel()
					writeBoardLabel('C', "QUITTING...")
					crs.delay_output(750)
					active = False
					continue
				clearBoardLabel()
				writeBoardLabel('C', "PAUSED")
				continue
			elif keypress == "ENTER":
				continue
			elif keypress == 'G':
				if doGhost:
					piece.undrawGhost()
				doGhost = not doGhost
				if doGhost:
					piece.drawGhost()
				continue
			# If neither the enter nor q key are pressed, it must be ESC,
			# Which means unpause
			clearBoardLabel()
			writeBoardLabel('C', "LEVEL " + str(difficulty))
			wBoard.nodelay(True)
			paused = False
			continue
		# SUBSECTION: PIECE GENERATION
		if not pieceInPlay:
			# Create new piece object
			piece = Piece( \
				pieceInfo[nextPID]['y'], \
				pieceInfo[nextPID]['x'], \
				nextPID, \
				pieceInfo[nextPID]["orient"] \
			)
			pieceJustSpawned = True
			# Go to the next piece and check if the bag needs shuffling
			# if using the bag randomizer
			if trueRandom:
				bagIndex = rnd.randint(0, 6)
			else:
				bagIndex += 1
				if bagIndex % 7 < (bagIndex - 1) % 7:
					rnd.shuffle(pieceBag)
			nextPID = pieceBag[bagIndex % 7]
			# Clear the next piece window and draw the next piece
			changeTexture(2, 1, 5, 12, ' ', crs.ACS_CKBOARD, wNextP)
			drawPiece( \
				pieceInfo[nextPID]["yn"], pieceInfo[nextPID]["xn"], \
				pieceInfo[nextPID]["orient"], nextPID, wNextP, [crs.ACS_CKBOARD] \
			)
			wNextP.refresh()
			pieceInPlay = True
			# Set the autodrop timer
			pieceDropTime = time.time()
			continue
		# SUBSECTION: PIECE AUTODROP, GAME OVER, AND LINE CLEAR
		if time.time() - pieceDropTime > dropTimes[difficulty] or pieceDropped:
			# Under normal circumstances
			if piece.canMove('D'):
				piece.move('D')
				pieceDropTime = time.time()
				pieceJustSpawned = False
			# When the piece it at the bottom
			else:
				if pieceDropped:
					dropDelay = False
				pieceInPlay = False
				pieceDropped = False
				# Game over check
				if pieceJustSpawned:
					for n in range(4):
						crs.flash()
						crs.delay_output(125)
					clearBoardLabel()
					writeBoardLabel('C', "GAME OVER!")
					crs.delay_output(2000)
					playing = False
					checkScore = True
					continue
				pieceJustSpawned = False
				wBoard.refresh()
				# Add softDrops to score and update piece statistics
				scoreData["SCORE"] += softDrops
				softDrops = 0
				writeScore(scoreData["SCORE"], "SCORE")
				wScore.refresh()
				scoreData["STAT" + piece.pID] += 1
				writeScore(scoreData["STAT" + piece.pID], "STAT" + piece.pID)
				wStats.refresh()
				# Erase old piece object
				del piece
				# Check if lines can be cleared
				lines = getFullLines()
				if len(lines) > 0:
					# Animate the lines to clear
					for f in range(20):
						for y in lines:
							if f == 0:
								changeTexture( \
									y, 1, y, 21, lineClearChars[f % 4], \
									crs.ACS_CKBOARD, wBoard \
								)
							else:
								changeTexture( \
									y, 1, y, 21, lineClearChars[f % 4], \
									lineClearChars[(f - 1) % 4], wBoard \
								)
						wBoard.refresh()
						crs.delay_output(50)
					# Clear the lines
					for y in lines:
						for x in range(1, 11):
							setCellValue(y, x, "EMPTY")
					# From the topmost line, drop down the remaining blocks
					for y in reversed(lines):
						j = y
						while not isLineEmpty(j - 1):
							for x in range(1, 11):
								setCellValue(j, x, cellValues[getCellValue(j - 1, x)])
								setCellValue(j - 1, x, "EMPTY")
							j -= 1
						wBoard.refresh()
						crs.delay_output(50)
					# Update scoreData and score labels
					scoreData["LINES"] += len(lines)
					scoreData["SCORE"] += lineClearScores[len(lines)] * (difficulty + 1)
					writeScore(scoreData["LINES"], "LINES")
					writeScore(scoreData["SCORE"], "SCORE")
					wScore.refresh()
					scoreData["STAT" + str(len(lines))] += 1
					writeScore(scoreData["STAT" + str(len(lines))], "STAT" + str(len(lines)))
					wStats.refresh()
					# Update difficulty check
					if lineClearDiffShifts[difficulty] <= scoreData["LINES"] and \
						difficulty < 9:
						difficulty += 1
						clearBoardLabel()
						writeBoardLabel('C', "LEVEL " + str(difficulty))
				# Sleep to delay before next piece spawns
				if dropDelay:
					crs.napms(333)
				dropDelay = True
				continue
		# SUBSECTION: KEY INPUT HANDLING
		k = wBoard.getch()
		if k not in keyCodes:
			crs.napms(10)
			continue
		keypress = keyCodes[k]
		# SUBSECTION: KEY INPUT PROCESSING
		if (keypress in arrowCodes or keypress in rotateCodes) and \
			pieceInPlay:
			pieceJustSpawned = False
		if keypress in arrowCodes and pieceInPlay:
			if keypress != 'U':
				pieceToDrop = False
				if piece.canMove(keypress):
					piece.move(keypress)
					if keypress == 'D':
						pieceDropTime = time.time()
						softDrops += 1
			# pieceToDrop Boolean is used to check for double press of up arrow key
			else:
				if not pieceToDrop:
					pieceToDrop = True
					continue
			#	if piece.canMove('D') and pieceJustSpawned:
			#		pieceJustSpawned = False
				while piece.canMove('D'):
					piece.move('D')
					softDrops += 1
				pieceToDrop = False
				pieceDropped = True
		elif keypress in rotateCodes and pieceInPlay:
			rotDir = "CW" if keypress == "SPACE" else "CCW"
			if piece.canRotate(rotDir):
				piece.rotate(rotDir)
		elif keypress == "ESC":
			paused = True
			clearBoardLabel()
			writeBoardLabel('C', "PAUSED")
	return None

# SECTION: MAIN
#Set ESC key delay time
os.environ.setdefault('ESCDELAY', '25')
#Initialize screen
screen = crs.initscr()
crs.start_color()
crs.use_default_colors()
#Run screen checks
if crs.LINES < 24 or crs.COLS < 80:
	crs.endwin()
	print("Your terminal must be at least 80x24 to run this game.")
	print("Please adjust your terminal settings accordingly.")
	exit()
#Define colors
crs.init_color(1, 1000, 1000, 0)
crs.init_color(2, 0, 1000, 0)
crs.init_color(3, 1000, 0, 0)
crs.init_color(4, 1000, 750, 0)
crs.init_color(5, 0, 0, 1000)
crs.init_color(6, 500, 500, 1000)
crs.init_color(7, 1000, 500, 1000)
crs.init_pair(1, -1, 1)
crs.init_pair(2, -1, 2)
crs.init_pair(3, -1, 3)
crs.init_pair(4, -1, 4)
crs.init_pair(5, -1, 5)
crs.init_pair(6, -1, 6)
crs.init_pair(7, -1, 7)
#Set proper key settings
crs.noecho()
crs.cbreak()
crs.curs_set(0)
#Initialize windows
wTitle = crs.newwin(6, 19, 0, 4)
wScore = crs.newwin(4, 17, 6, 5)
wCntrl = crs.newwin(14, 23, 10, 2)
wBoard = crs.newwin(24, 22, 0, 28)
wBoard.keypad(True)
wBoard.nodelay(True)
wNextP = crs.newwin(7, 15, 0, 54)
wStats = crs.newwin(17, 19, 7, 52)
#Draw boarders of windows
wTitle.border()
wScore.border()
wCntrl.border()
wBoard.border()
wNextP.border()
wStats.border()
#Write titles and labels
wTitle.addstr(1, 4, "Cursa Tetra")
wTitle.addstr(2, 4, 11 * '-')
wTitle.addstr(3, 4, "By C. Cook")
wTitle.addstr(4, 2, "Ded. A. Pajitnov")
wScore.addstr(1, 1, "SCORE:")
wScore.addstr(2, 1, "LINES:")
wCntrl.addstr(1, 6, "CONTROLS:")
wCntrl.addstr(2, 1, "L/R ARROWS: MOVE")
wCntrl.addstr(3, 1, "DOWN ARROW: DROP 1")
wCntrl.addstr(4, 1, "UP ARROWx2: DROP ALL")
wCntrl.addstr(5, 1, "SPACE BAR : ROT. CW")
wCntrl.addstr(6, 1, "          : OR START")
wCntrl.addstr(7, 1, "CTRL+SPACE: ROT. CCW")
wCntrl.addstr(8, 1, "ESC       : PAUSE OR")
wCntrl.addstr(9, 1, "          : RESUME")
wCntrl.addstr(10, 6, "IF PAUSED:")
wCntrl.addstr(11, 1, "Q     : QUIT GAME")
wCntrl.addstr(12, 1, "G     : TOGGLE GHOST")
drawGrid()
drawBoardBorder()
writeBoardLabel('L', "PRESS SPACE TO START")
wNextP.addstr(1, 2, "NEXT PIECE:")
wNextP.addstr(2, 2, 11 * '-')
wStats.addstr(1, 4, "STATISTICS:")
wStats.addstr(2, 4, 11 * '-')
wStats.addstr(3, 1, "::PIECES" + 9 * ':')
wStats.addstr(4, 1, "SQUARES :")
wStats.addstr(5, 1, "S-PIECES:")
wStats.addstr(6, 1, "Z-PIECES:")
wStats.addstr(7, 1, "L-PIECES:")
#wStats.addstr(7, 1, chr(0x2143) + "-BLOCKS:")
#wStats.addstr(7, 1, chr(0xac) + "-PIECES:")
wStats.addstr(8, 1, "J-PIECES:")
wStats.addstr(9, 1, "I-PIECES:")
wStats.addstr(10, 1, "T-PIECES:")
wStats.addstr(11, 1, "::LINES" + 10 * ':')
wStats.addstr(12, 1, "SINGLES :")
wStats.addstr(13, 1, "DOUBLES :")
wStats.addstr(14, 1, "TRIPLES :")
wStats.addstr(15, 1, "TETRI   :")
#Write initial scores and statistics
writeScore(0, "SCORE")
writeScore(0, "LINES")
writeScore(0, "STATC")
writeScore(0, "STATS")
writeScore(0, "STATZ")
writeScore(0, "STATL")
writeScore(0, "STATR")
writeScore(0, "STATI")
writeScore(0, "STATT")
writeScore(0, "STAT1")
writeScore(0, "STAT2")
writeScore(0, "STAT3")
writeScore(0, "STAT4")
#Make windows visible
wTitle.refresh()
wScore.refresh()
wCntrl.refresh()
wBoard.refresh()
wNextP.refresh()
wStats.refresh()
#Main function call
ctMain()
#Move & Rotation demo
#rotations = {'C': ['']}
#rotations.update(dict.fromkeys(['S', 'Z', 'I'], ['H', 'V']))
#rotations.update(dict.fromkeys(['L', 'R', 'T'], ['H', 'V', 'HP', 'VP']))
#for id in ('C', 'S', 'Z', 'L', 'R', 'I', 'T'):
#	for r in rotations[id]:
#		p = Piece(1, 4, id, r)
#		clearBoardLabel()
#		wBoard.refresh()
#		crs.delay_output(250)
#		for i in range(8):
#			direction = ['CW', 'CCW'][int(i < 4)]
#			if p.canRotate(direction):
#				p.rotate(direction)
#				clearBoardLabel()
#				writeBoardLabel('L', "Rotated to " + p.orient)
#				wBoard.refresh()
#				crs.delay_output(100)
#		clearBoardLabel()
#		wBoard.refresh()
#		crs.delay_output(250)
#		for d in ('D', 'R', 'L'):
#			writeBoardLabel('L', "Moving " + d)
#			wBoard.refresh()
#			while p.canMove(d):
#				p.move(d)
#				wBoard.refresh()
#				crs.delay_output(50)
#		p.undraw()
#		del p
#		crs.delay_output(250)
#Unset proper key settings
wBoard.nodelay(False)
wBoard.keypad(False)
screen.keypad(False)
crs.nocbreak()
crs.echo()
#Close screen
crs.endwin()
