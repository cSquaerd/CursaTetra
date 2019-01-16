#SECTION: IMPORTS
import curses as crs

#SECTION: FUNCTIONS
"""
Draws an alignment grid in the board window
"""
def drawGrid():
	for x in range(1, 21, 2):
		for y in range(1, 21):
			wBoard.addch(y, x, '.')
"""
Draws the bottom border in the board window
"""
def drawBoardBorder():
	wBoard.addch(21, 0, crs.ACS_LTEE)
	for x in range(1, 21):
		wBoard.addch(21, x, crs.ACS_HLINE)
	wBoard.addch(21, 21, crs.ACS_RTEE)
"""
Draws a piece to a window (use wBoard or wNextP only!)

See README.md or check the bottom of this file for details on block behavoir
"""
def drawPiece(y, x, orient, piece, window, character):
	if piece == 'C':
		for i in range(x, x + 4):
			for j in range(y, y + 2):
				window.addch(j, i, character)
	elif piece == 'S':
		if orient == 'H':
			for i in range(x + 2, x + 6):
				window.addch(y + 1, i, character)
			for i in range(x, x + 4):
				window.addch(y + 2, i, character)
		else:
			for i in range(x, x + 2):
				for j in range(y, y + 2):
					window.addch(j, i, character)
			for i in range(x + 2, x + 4):
				for j in range(y + 1, y + 3):
					window.addch(j, i, character)
	elif piece == 'Z':
		if orient == 'H':
			for i in range(x, x + 4):
				window.addch(y + 1, i, character)
			for i in range(x + 2, x + 6):
				window.addch(y + 2, i, character)
		else:
			for i in range(x, x + 2):
				for j in range(y + 1, y + 3):
					window.addch(j, i, character)
			for i in range(x + 2, x + 4):
				for j in range(y, y + 2):
					window.addch(j, i, character)
	elif piece == 'L':
		if orient == 'H':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, character)
			for i in range(x + 4, x + 6):
				window.addch(y + 2, i, character)
		elif orient == 'V':
			for i in range(x, x + 6):
				window.addch(y + 1, i, character)
			for i in range(x, x + 2):
				window.addch(y + 2, i, character)
		elif orient == 'HP':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, character)
			for i in range(x, x + 2):
				window.addch(y, i, character)
		elif orient == 'VP':
			for i in range(x, x + 6):
				window.addch(y + 1, i, character)
			for i in range(x + 4, x + 6):
				window.addch(y, i, character)
	elif piece == 'R':
		if orient == 'H':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, character)
			for i in range(x, x + 2):
				window.addch(y + 2, i, character)
		elif orient == 'V':
			for i in range(x, x + 6):
				window.addch(y + 1, i, character)
			for i in range(x, x + 2):
				window.addch(y, i, character)
		elif orient == 'HP':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, character)
			for i in range(x + 4, x + 6):
				window.addch(y, i, character)
		elif orient == 'VP':
			for i in range(x, x + 6):
				window.addch(y + 1, i, character)
			for i in range(x + 4, x + 6):
				window.addch(y + 2, i, character)
	elif piece == 'I':
		if orient == 'H':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 4):
					window.addch(j, i, character)
		else:
			for i in range(x, x + 8):
				window.addch(y + 2, i, character)
	elif piece == 'T':
		if orient == 'H':
			for i in range(x, x + 6):
				window.addch(y + 1, i, character)
			for i in range(x + 2, x + 4):
				window.addch(y + 2, i, character)
		elif orient == 'V':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, character)
			for i in range(x, x + 2):
				window.addch(y + 1, i, character)
		elif orient == 'HP':
			for i in range(x, x + 6):
				window.addch(y + 1, i, character)
			for i in range(x + 2, x + 4):
				window.addch(y, i, character)
		elif orient == 'VP':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, character)
			for i in range(x + 4, x + 6):
				window.addch(y + 1, i, character)
"""
Redraws characters in a window.

Given a target character (B), and a region from
(xi, yi) to (xf, yf) where xi < xf and yi < yf,
any instances of the target char. in the window
will be overwritten with the result character (A)
"""
def changeTexture(yi, xi, yf, xf, characterA, characterB, window):
	if not (xi < xf and yi < yf):
		return None
	for i in range(xi, xf + 1):
		for j in range(yi, yf + 1):
			if type(characterB) is str and window.inch(j, i) == ord(characterB) \
				or type(characterB) is int and window.inch(j, i) == characterB:
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
"""
Writes a score value to a score label, listed below
"""
def writeScore(score, scoreType):
	scoreLabels = ('', "SCORE", "LINES", "STATC", "STATS", "STATZ", \
		"STATL", "STATR", "STATI", "STATT", '', "STAT1", "STAT2", \
		"STAT3", "STAT4")
	scoreIndex = scoreLabels.index(scoreType)
	if scoreIndex < 3:
		wScore.addstr(scoreIndex, 16 - numDigits(score), str(score))
	else:
		wStats.addstr(scoreIndex, 18 - numDigits(score), str(score))
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
"""
Clears the lower section of the board
"""
def clearBoardLabel():
	wBoard.addstr(22, 1, 20 * ' ')
"""
Main function

Contains event loop for handling keypresses,
scoring and statistics variables, and other
vital functionality
"""
def ctMain():
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

#SECTION: MAIN
#Initialize screen
screen = crs.initscr()
#Set proper key settings
crs.noecho()
crs.cbreak()
screen.keypad(True)
crs.curs_set(0)
#Initialize windows
wTitle = crs.newwin(6, 19, 0, 4)
wScore = crs.newwin(4, 17, 6, 5)
wCntrl = crs.newwin(10, 23, 10, 2)
wBoard = crs.newwin(24, 22, 0, 28)
wNextP = crs.newwin(7, 15, 0, 54)
wStats = crs.newwin(16, 19, 7, 52)
#Draw boarders of windows
wTitle.border()
wScore.border()
wCntrl.border()
wBoard.border()
wNextP.border()
wStats.border()
#Write titles and labels
wTitle.addstr(1, 4, "Cursa Tetra")
wTitle.addstr(2, 1, 17 * '-')
wTitle.addstr(3, 4, "By C. Cook")
wTitle.addstr(4, 2, "Ded. A. Pajitnov")
wScore.addstr(1, 1, "SCORE:")
wScore.addstr(2, 1, "LINES:")
wCntrl.addstr(1, 6, "CONTROLS:")
wCntrl.addstr(2, 1, "L/R ARROWS: MOVE")
wCntrl.addstr(3, 1, "DOWN ARROW: DROP 1")
wCntrl.addstr(4, 1, "UP ARROW  : DROP ALL")
wCntrl.addstr(5, 1, "SPACE BAR : ROT. CW")
wCntrl.addstr(6, 1, "CTRL+SPACE: ROT. CCW")
wCntrl.addstr(7, 1, "ESC       : PAUSE")
wCntrl.addstr(8, 1, "Q         : QUIT")
drawGrid()
drawBoardBorder()
writeBoardLabel('15', "FOOBAR")
wNextP.addstr(1, 2, "NEXT PIECE:")
wStats.addstr(1, 4, "STATISTICS:")
wStats.addstr(2, 1, ":PIECES::")
wStats.addstr(3, 1, "SQUARES :")
wStats.addstr(4, 1, "S-PIECES:")
wStats.addstr(5, 1, "Z-PIECES:")
wStats.addstr(6, 1, "L-PIECES:")
#wStats.addstr(7, 1, chr(0x2143) + "-BLOCKS:")
wStats.addstr(7, 1, chr(0xac) + "-PIECES:")
wStats.addstr(8, 1, "I-PIECES:")
wStats.addstr(9, 1, "T-PIECES:")
wStats.addstr(10, 1, ":LINES:::")
wStats.addstr(11, 1, "SINGLES :")
wStats.addstr(12, 1, "DOUBLES :")
wStats.addstr(13, 1, "TRIPLES :")
wStats.addstr(14, 1, "TETRI   :")
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
#Pieces demo (comment out later)
drawPiece(1, 1, '', 'C', wBoard, crs.ACS_CKBOARD)
drawPiece(1, 15, 'H', 'I', wBoard, crs.ACS_CKBOARD)
drawPiece(0, 7, 'V', 'I', wBoard, crs.ACS_CKBOARD)
drawPiece(3, 1, 'H', 'S', wBoard, crs.ACS_CKBOARD)
drawPiece(4, 9, 'V', 'S', wBoard, crs.ACS_CKBOARD)
drawPiece(7, 1, 'H', 'Z', wBoard, crs.ACS_CKBOARD)
drawPiece(8, 9, 'V', 'Z', wBoard, crs.ACS_CKBOARD)
drawPiece(11, 1, 'H', 'L', wBoard, crs.ACS_CKBOARD)
drawPiece(11, 9, 'V', 'L', wBoard, crs.ACS_CKBOARD)
drawPiece(10, 17, 'HP', 'L', wBoard, crs.ACS_CKBOARD)
drawPiece(15, 1, 'H', 'R', wBoard, crs.ACS_CKBOARD)
drawPiece(15, 9, 'V', 'R', wBoard, crs.ACS_CKBOARD)
drawPiece(14, 15, 'HP', 'R', wBoard, crs.ACS_CKBOARD)
drawPiece(18, 1, 'H', 'T', wBoard, crs.ACS_CKBOARD)
drawPiece(18, 9, 'V', 'T', wBoard, crs.ACS_CKBOARD)
drawPiece(18, 15, 'HP', 'T', wBoard, crs.ACS_CKBOARD)
#Make windows visible
wTitle.refresh()
wScore.refresh()
wCntrl.refresh()
wBoard.refresh()
wNextP.refresh()
wStats.refresh()
#Main function call
#ctMain()
#Wait
crs.delay_output(2000)
#Label demo (comment out later)
changeTexture(1, 1, 23, 20, crs.ACS_BLOCK, crs.ACS_CKBOARD, wBoard)
clearBoardLabel()
writeBoardLabel('15', "PONTIFEX MX")
wBoard.refresh()
crs.delay_output(2000)

for n in range(41, 0, -1):
	clearBoardLabel()
	writeBoardLabel(str(n), "LOOK AT ME, MA!")
	wBoard.refresh()
	crs.delay_output(75)

#Unset proper key settings
screen.keypad(False)
crs.nocbreak()
crs.echo()
#Close screen
crs.endwin()

"""
# Piece orientations

* H : horizontal (default)
* V : vertical
* HP : horizontal, pi radians around (180 deg)
* VP : vertical, pi radians around (180 deg)

# Piece designations & diagrams
## Based on specification in Game Boy version

* Note: The orientation of the pieces may seem backwards at first glance;
Consider it in terms of the orientation of an underline
below the text character that identifies a piece

* C : Square
	* Diagram:
	```
	  012345
	0.[][]
	1.[][]
	2.
	```
* S : S-piece
	* Diagrams:
		* Horizontal
		```
		  012345
		0.  [][]
		1.[][]
		2.
		```
		* Vertical
		```
		  012345
		0.[]
		1.[][]
		2.  []
		```
	* Observations:
		* Rotates about (2:3, 1) Clockwise
* Z : Z-piece
	* Diagrams:
		* Horizontal
		```
		  012345
		0.[][]
		1.  [][]
		2.
		```
		* Vertical
		```
		  012345
		0.  []
		1.[][]
		2.[]
		```
	* Observations:
		* Rotates about (2:3, 1) Counter-Clockwise
* L : L-piece
	* Diagrams:
		* Horizontal
		```
		  012345
		0.  []
		1.  []
		2.  [][]
		```
		* Vertical
		```
		  012345
		0.
		1.[][][]
		2.[]
		```
		* Horizontal-Pi
		```
		  012345
		0.[][]
		1.  []
		2.  []
		```
		* Vertical-Pi
		```
		  012345
		0.    []
		1.[][][]
		2.
		```
	* Observations:
		* Rotates about (2:3, 1) Both Ways
* R : Reversed L-piece
	* Diagrams:
		* Horizontal
		```
		  012345
		0.  []
		1.  []
		2.[][]
		```
		* Vertical
		```
		  012345
		0.[]
		1.[][][]
		2.
		```
		* Horizontal-Pi
		```
		  012345
		0.  [][]
		1.  []
		2.  []
		```
		* Vertical-Pi
		```
		  012345
		0.
		1.[][][]
		2.    []
		```
	* Observations:
		* Rotates about (2:3, 1) Both Ways
* I : Line
	* Diagrams:
		* Horizontal
		```
		  01234567
		0.  []
		1.  []
		2.  []
		3.  []
		```
		* Vertical
		```
		  01234567
		0.
		1.
		2.[][][][]
		3.
		```
	* Observations:
		* Rotates about (2:3, 2) Clockwise
* T : T-piece
	* Diagrams:
		* Horizontal
		```
		  012345
		0.
		1.[][][]
		2.  []
		```
		* Vertical
		```
		  012345
		0.  []
		1.[][]
		2.  []
		```
		* Horizontal-Pi
		```
		  012345
		0.  []
		1.[][][]
		2.
		```
		* Vertical-Pi
		```
		  012345
		0.  []
		1.  [][]
		2.  []
		```
	* Observations:
		* Rotates about (2:3, 1) Both Ways
"""
