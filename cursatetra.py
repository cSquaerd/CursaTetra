#SECTION: IMPORTS
import curses as crs

#SECTION: FUNCTIONS
"""
Draws an alignment grid in the board window
"""
def drawGrid():
	for x in range(1, 21):
		for y in range(1, 23):
			wBoard.addch(y, x, '.')

"""
# Block designations

* C : Square
* S : S-piece
* Z : Z-piece
* L : L-piece
* R : Reversed L-piece
* I : Line
* T : T-piece

# Orientations

* H : horizontal (default)
* V : vertical
* HP : horizontal, pi radians around (180 deg)
* VP : vertical, pi radians around (180 deg)
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

def changeTexture(yi, xi, yf, xf, characterA, characterB, window):
	if not (xi < xf and yi < yf):
		return None
	for i in range(xi, xf + 1):
		for j in range(yi, yf + 1):
			if type(characterB) is str and window.inch(j, i) == ord(characterB) \
				or type(characterB) is int and window.inch(j, i) == characterB:
				window.addch(j, i, characterA)

def numDigits(n):
	if n == 0:
		return 1
	m = 0;
	while n >= 10 ** m:
		m += 1
	return m

def writeScore(score, scoreType):
	scoreLabels = ('', "SCORE", "LINES", "STATC", "STATS", "STATZ", \
		"STATL", "STATR", "STATI", "STATT", '', "STAT1", "STAT2", \
		"STAT3", "STAT4")
	scoreIndex = scoreLabels.index(scoreType)
	if scoreIndex < 3:
		wScore.addstr(scoreIndex, 16 - numDigits(score), str(score))
	else:
		wStats.addstr(scoreIndex, 18 - numDigits(score), str(score))

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

writeScore(100, "SCORE")
writeScore(200, "LINES")
writeScore(300, "STATC")
writeScore(400, "STATS")
writeScore(500, "STATZ")
writeScore(600, "STATL")
writeScore(700, "STATR")
writeScore(800, "STATI")
writeScore(900, "STATT")
writeScore(1000, "STAT1")
writeScore(1100, "STAT2")
writeScore(1200, "STAT3")
writeScore(1300, "STAT4")

drawPiece(1, 1, '', 'C', wBoard, crs.ACS_CKBOARD)
drawPiece(1, 15, 'H', 'I', wBoard, crs.ACS_CKBOARD)
drawPiece(0, 7, 'V', 'I', wBoard, crs.ACS_CKBOARD)
drawPiece(4, 1, 'H', 'S', wBoard, crs.ACS_CKBOARD)
drawPiece(4, 9, 'V', 'S', wBoard, crs.ACS_CKBOARD)
drawPiece(8, 1, 'H', 'Z', wBoard, crs.ACS_CKBOARD)
drawPiece(8, 9, 'V', 'Z', wBoard, crs.ACS_CKBOARD)
drawPiece(12, 1, 'H', 'L', wBoard, crs.ACS_CKBOARD)
drawPiece(12, 9, 'V', 'L', wBoard, crs.ACS_CKBOARD)
drawPiece(12, 17, 'HP', 'L', wBoard, crs.ACS_CKBOARD)
drawPiece(16, 1, 'H', 'R', wBoard, crs.ACS_CKBOARD)
drawPiece(16, 9, 'V', 'R', wBoard, crs.ACS_CKBOARD)
drawPiece(16, 15, 'HP', 'R', wBoard, crs.ACS_CKBOARD)
drawPiece(20, 1, 'H', 'T', wBoard, crs.ACS_CKBOARD)
drawPiece(20, 9, 'V', 'T', wBoard, crs.ACS_CKBOARD)
drawPiece(20, 15, 'HP', 'T', wBoard, crs.ACS_CKBOARD)
#Make windows visible
wTitle.refresh()
wScore.refresh()
wCntrl.refresh()
wBoard.refresh()
wNextP.refresh()
wStats.refresh()

#Wait
crs.delay_output(2000)

changeTexture(1, 1, 23, 20, crs.ACS_BLOCK, crs.ACS_CKBOARD, wBoard)
wBoard.refresh()
crs.delay_output(2000)

#Unset proper key settings
screen.keypad(False)
crs.nocbreak()
crs.echo()
#Close screen
crs.endwin()
