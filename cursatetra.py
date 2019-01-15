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
def drawPiece(y, x, orient, piece, window):
	if piece == 'C':
		for i in range(x, x + 4):
			for j in range(y, y + 2):
				window.addch(j, i, crs.ACS_CKBOARD)
	elif piece == 'S':
		if orient == 'H':
			for i in range(x + 2, x + 6):
				window.addch(y + 1, i, crs.ACS_CKBOARD)
			for i in range(x, x + 4):
				window.addch(y + 2, i, crs.ACS_CKBOARD)
		else:
			for i in range(x, x + 2):
				for j in range(y, y + 2):
					window.addch(j, i, crs.ACS_CKBOARD)
			for i in range(x + 2, x + 4):
				for j in range(y + 1, y + 3):
					window.addch(j, i, crs.ACS_CKBOARD)
	elif piece == 'Z':
		if orient == 'H':
			for i in range(x, x + 4):
				window.addch(y + 1, i, crs.ACS_CKBOARD)
			for i in range(x + 2, x + 6):
				window.addch(y + 2, i, crs.ACS_CKBOARD)
		else:
			for i in range(x, x + 2):
				for j in range(y + 1, y + 3):
					window.addch(j, i, crs.ACS_CKBOARD)
			for i in range(x + 2, x + 4):
				for j in range(y, y + 2):
					window.addch(j, i, crs.ACS_CKBOARD)
	elif piece == 'L':
		if orient == 'H':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, crs.ACS_CKBOARD)
			for i in range(x + 4, x + 6):
				window.addch(y + 2, i, crs.ACS_CKBOARD)
		elif orient == 'V':
			for i in range(x, x + 6):
				window.addch(y + 1, i, crs.ACS_CKBOARD)
			for i in range(x, x + 2):
				window.addch(y + 2, i, crs.ACS_CKBOARD)
		elif orient == 'HP':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, crs.ACS_CKBOARD)
			for i in range(x, x + 2):
				window.addch(y, i, crs.ACS_CKBOARD)
		elif orient == 'VP':
			for i in range(x, x + 6):
				window.addch(y + 1, i, crs.ACS_CKBOARD)
			for i in range(x + 4, x + 6):
				window.addch(y, i, crs.ACS_CKBOARD)
	elif piece == 'R':
		if orient == 'H':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, crs.ACS_CKBOARD)
			for i in range(x, x + 2):
				window.addch(y + 2, i, crs.ACS_CKBOARD)
		elif orient == 'V':
			for i in range(x, x + 6):
				window.addch(y + 1, i, crs.ACS_CKBOARD)
			for i in range(x, x + 2):
				window.addch(y, i, crs.ACS_CKBOARD)
		elif orient == 'HP':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, crs.ACS_CKBOARD)
			for i in range(x + 4, x + 6):
				window.addch(y, i, crs.ACS_CKBOARD)
		elif orient == 'VP':
			for i in range(x, x + 6):
				window.addch(y + 1, i, crs.ACS_CKBOARD)
			for i in range(x + 4, x + 6):
				window.addch(y + 2, i, crs.ACS_CKBOARD)
	elif piece == 'I':
		if orient == 'H':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 4):
					window.addch(j, i, crs.ACS_CKBOARD)
		else:
			for i in range(x, x + 8):
				window.addch(y + 2, i, crs.ACS_CKBOARD)
	elif piece == 'T':
		if orient == 'H':
			for i in range(x, x + 6):
				window.addch(y + 1, i, crs.ACS_CKBOARD)
			for i in range(x + 2, x + 4):
				window.addch(y + 2, i, crs.ACS_CKBOARD)
		elif orient == 'V':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, crs.ACS_CKBOARD)
			for i in range(x, x + 2):
				window.addch(y + 1, i, crs.ACS_CKBOARD)
		elif orient == 'HP':
			for i in range(x, x + 6):
				window.addch(y + 1, i, crs.ACS_CKBOARD)
			for i in range(x + 2, x + 4):
				window.addch(y, i, crs.ACS_CKBOARD)
		elif orient == 'VP':
			for i in range(x + 2, x + 4):
				for j in range(y, y + 3):
					window.addch(j, i, crs.ACS_CKBOARD)
			for i in range(x + 4, x + 6):
				window.addch(y + 1, i, crs.ACS_CKBOARD)

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
wScore = crs.newwin(4, 17, 8, 5)
wCntrl = crs.newwin(10, 23, 12, 2)
wBoard = crs.newwin(24, 22, 0, 28)
wNextP = crs.newwin(7, 15, 4, 52)
#Draw boarders of windows
wTitle.border()
wScore.border()
wCntrl.border()
wBoard.border()
wNextP.border()
#Write titles and labels
wTitle.addstr(1, 4, "Cursa Tetra")
wTitle.addstr(2, 1, 17 * '-')
wTitle.addstr(3, 2, "By Charlie Cook")
wScore.addstr(1, 1, "SCORE:")
drawGrid()
wNextP.addstr(1, 2, "NEXT PIECE:")
drawPiece(1, 1, '', 'C', wBoard)
drawPiece(1, 15, 'H', 'I', wBoard)
drawPiece(0, 7, 'V', 'I', wBoard)
drawPiece(4, 1, 'H', 'S', wBoard)
drawPiece(4, 9, 'V', 'S', wBoard)
drawPiece(8, 1, 'H', 'Z', wBoard)
drawPiece(8, 9, 'V', 'Z', wBoard)
drawPiece(12, 1, 'H', 'L', wBoard)
drawPiece(12, 9, 'V', 'L', wBoard)
drawPiece(12, 17, 'HP', 'L', wBoard)
drawPiece(16, 1, 'H', 'R', wBoard)
drawPiece(16, 9, 'V', 'R', wBoard)
drawPiece(16, 15, 'HP', 'R', wBoard)
drawPiece(20, 1, 'H', 'T', wBoard)
drawPiece(20, 9, 'V', 'T', wBoard)
drawPiece(20, 15, 'HP', 'T', wBoard)
#Make windows visible
wTitle.refresh()
wScore.refresh()
wCntrl.refresh()
wBoard.refresh()
wNextP.refresh()

#Wait
crs.delay_output(2000)

#Unset proper key settings
screen.keypad(False)
crs.nocbreak()
crs.echo()
#Close screen
crs.endwin()
