# SECTION: IMPORTS
import curses as crs
import os
import time
import random as rnd
import sys
import json
from ct_draw import *
from ct_label import *
from ct_cell import *
from Piece import *
resizedTooSmall = False
missingSettings = False
# SECTION: VERSION CHECK
if sys.version_info[0] < 3:
	print("This game requires Python 3. Please install it and/or run this file with it.")
	exit()
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
		ord('P') : "ESC", \
		ord('p') : "ESC", \
		ord('Q') : 'Q', \
		ord('q') : 'Q', \
		ord('h') : 'H', \
		ord('H') : 'H'
	}
	arrowCodes = ('L', 'R', 'D', 'U')
	rotateCodes = ("SPACE", "NULL")
	yesnoCodes = {ord('\n') : 'ENTER', ord('y') : 'y', ord('Y') : 'Y', \
		ord('n') : 'n', ord('N') : 'N'}
	yesCodes = {ord('\n') : 'ENTER', ord('y') : 'y', ord('Y') : 'Y'}
	noCodes = {ord('n') : 'n', ord('N') : 'N'}
	menuCodes = { \
		27 : "ESC", ord('q') : 'Q', ord('Q') : 'Q', \
		ord('P') : "ESC", ord('p') : "ESC", ord('\n') : "ENTER", \
		ord('G') : 'G', ord('g') : 'G' \
	}
	startCodes = {ord('q') : 'Q', ord('Q') : 'Q', ord(' ') : "SPACE"}
	dropTimes = (0.75, 0.6, 0.5, 0.425, 0.35, 0.3, 0.25, 0.200, 0.15, 0.1)
	lineClearChars = (crs.ACS_S1, crs.ACS_S3, crs.ACS_S7, crs.ACS_S9)
	lineClearScores = (0, 40, 100, 300, 1200)
	lineClearDiffShifts = (10, 20, 30, 45, 60, 75, 95, 115, 140, 165)
	pieceInfo = { \
		'C': {'y': 1, 'x': 5, "orient" : '', "yn": 1, "xn": 11}, \
		'S': {'y': 0, 'x': 4, "orient" : 'H', "yn": 0, "xn": 9}, \
		'Z': {'y': 0, 'x': 4, "orient" : 'H', "yn": 0, "xn": 9}, \
		'L': {'y': 0, 'x': 4, "orient" : 'V', "yn": 0, "xn": 9}, \
		'R': {'y': 0, 'x': 4, "orient" : 'VP', "yn": 0, "xn": 9}, \
		'I': {'y': -1, 'x': 4, "orient" : 'V', "yn": -1, "xn": 9}, \
		'T': {'y': 0, 'x': 4, "orient" : 'H', "yn": 0, "xn": 9}, \
	}
	letters = tuple(range(0x41, 0x41 + 26)) + tuple(range(0x61, 0x61 + 26))
	# SECTION: CONTROL VARIABLES AND BOOLEANS
	cellValues = { \
		ord(' '): "EMPTY", \
		crs.ACS_CKBOARD + 0x300: "ACTIVE-C", \
		crs.ACS_CKBOARD + 0x3000000: "ACTIVE-C", \
		crs.ACS_CKBOARD + 0x200: "ACTIVE-S", \
		crs.ACS_CKBOARD + 0x2000000: "ACTIVE-S", \
		crs.ACS_CKBOARD + 0x100: "ACTIVE-Z", \
		crs.ACS_CKBOARD + 0x1000000: "ACTIVE-Z", \
		crs.ACS_CKBOARD + 0x700: "ACTIVE-L", \
		crs.ACS_CKBOARD + 0x7000000: "ACTIVE-L", \
		crs.ACS_CKBOARD + 0x400: "ACTIVE-R", \
		crs.ACS_CKBOARD + 0x4000000: "ACTIVE-R", \
		crs.ACS_CKBOARD + 0x600: "ACTIVE-I", \
		crs.ACS_CKBOARD + 0x6000000: "ACTIVE-I", \
		crs.ACS_CKBOARD + 0x500: "ACTIVE-T", \
		crs.ACS_CKBOARD + 0x5000000: "ACTIVE-T" \
	}
	active = True
	playing = False
	paused = False
	global resizedTooSmall
	global missingSettings
	pieceInPlay = False
	pieceToDrop = False
	pieceDropped = False
	dropDelay = True
	pieceJustSpawned = False
	atBottom = False
	difficulty = -1
	randomizer = None
	pieceBag = list(pieceInfo.keys())
	rnd.shuffle(pieceBag)
	bagIndex = 0
	nextPID = pieceBag[bagIndex % 7]
	holdPID = ''
	canHold = True
	softDrops = 0
	tSpun = False
	checkScore = False
	settingsFileName = "settings.json"
	allowGhostToggle = True
	allowHoldFeature = True
	preferredDifficulty = 0
	preferredRandomizer = 'B'
	scoreFileName = ".ctHiScrs.json"
	scoreFileWrite = False
	global doGhost
	# SECTION: SETTINGS PREP
	try:
		settingsFile = open(settingsFileName, 'r')
		settings = json.loads(settingsFile.read())
		settingsFile.close()
		allowGhostToggle = settings["allowGhostToggle"]
		allowHoldFeature = settings["allowHoldFeature"]
		preferredDifficulty = settings["preferredDifficulty"]
		preferredRandomizer = settings["preferredRandomizer"]
	except FileNotFoundError:
		active = False
		missingSettings = True
	# SECTION: HIGH SCORE PREP
	try:
		# Assume the high score file exists
		scoreFile = open(scoreFileName, 'r')
		highScores = json.loads(scoreFile.read())
		scoreFile.close()
		tempKeys = list(highScores.keys())
		# Primary JSON Keys are always strings.
		# Convert them back to integers
		for k in tempKeys:
			highScores[int(k)] = highScores[k]
			del highScores[k]
	except FileNotFoundError:
		# Create the high score file as it doesn't exist
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
		wBoard.addch(4, 1, crs.ACS_ULCORNER)
		wBoard.addch(4, 20, crs.ACS_URCORNER)
		wBoard.addch(5, 1, crs.ACS_LTEE)
		wBoard.addch(5, 20, crs.ACS_RTEE)
		wBoard.addch(6, 1, crs.ACS_LLCORNER)
		wBoard.addch(6, 20, crs.ACS_LRCORNER)
		for i in range(18):
			wBoard.addch(4, 2 + i, crs.ACS_HLINE)
			wBoard.addch(5, 2 + i, crs.ACS_HLINE)
			wBoard.addch(6, 2 + i, crs.ACS_HLINE)
		wBoard.addch(6, 7, crs.ACS_TTEE)
		wBoard.addch(6, 15, crs.ACS_TTEE)
		wBoard.addstr(5, 5, " TOP SCORES ")
		wBoard.addstr(7, 1, "# NAME  SCORE  LINES")
		wBoard.addch(7, 7, crs.ACS_VLINE)
		wBoard.addch(7, 15, crs.ACS_VLINE)
		i = 1
		while i <= 10 and highScores[i]["SCORE"] > 0:
			wBoard.addstr(7 + i, 1, 20 * ' ')
			wBoard.addstr(7 + i, 1, str(i) + ".")
			wBoard.addstr(7 + i, 4, highScores[i]["NAME"])
			wBoard.addstr(7 + i, 8, "{:>7}".format(highScores[i]["SCORE"]))
			wBoard.addstr(7 + i, 16, "{:>5}".format(highScores[i]["LINES"]))
			wBoard.addch(7 + i, 7, crs.ACS_VLINE)
			wBoard.addch(7 + i, 15, crs.ACS_VLINE)
			i += 1
		wBoard.refresh()
	# SECTION: ACTIVE LOOP
	while active:
		# SUBSECTION: RESIZE CHECK
		crs.update_lines_cols()
		if crs.LINES < 24 or crs.COLS < 72:
			active = False
			resizedTooSmall = True
			continue
		# SUBSECTION: HIGH SCORE WRITE
		if checkScore:
			# Find where the user places in the list
			place = 11
			for i in range(10, 0, -1):
				if scoreData["SCORE"] > highScores[i]["SCORE"]:
					place = i
				else:
					break
			# If place has changed, the user should be added to the list
			if place < 11:
				wBoard.nodelay(False)
				nameEntered = False
				while not nameEntered:
					undrawGrid(wBoard)
					wBoard.addstr(1, 1, "CONGRATULATIONS!")
					wBoard.addstr(2, 1, "YOUR SCORE PUTS YOU")
					wBoard.addstr(3, 1, "AT RANK " + str(place) + "!")
					wBoard.addstr(4, 1, "PLEASE ENTER YOUR")
					wBoard.addstr(5, 1, "INITIALS:")
					wBoard.refresh()
					k = -1
					l = 0
					s = ''
					# Get the user's initials, letters only
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
						crs.napms(1000)
						nameEntered = True
						wBoard.nodelay(True)
						continue
					else:
						wBoard.addstr(8, 1, "OKAY, ENTER AGAIN.")
						wBoard.refresh()
						crs.napms(500)
						continue
				# Setup the new high score dict. object
				tempEntry = {}
				tempEntry["SCORE"] = scoreData["SCORE"]
				tempEntry["NAME"] = s
				tempEntry["LINES"] = scoreData["LINES"]
				# Shift all scores lower than new one down
				for j in range(10, place, -1):
					highScores[j] = highScores[j - 1]
				# Insert the new high score
				highScores[place] = tempEntry
				scoreFileWrite = True
			else:
				checkScore = False
				continue
			if scoreFileWrite:
				scoreFile = open(scoreFileName, 'w')
				scoreFile.write(json.dumps(highScores, sort_keys = True, indent = 2))
				scoreFile.close()
				undrawGrid(wBoard)
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
				clearBoardLabel(wBoard)
				writeBoardLabel('C', "QUITTING...", wBoard)
				crs.napms(750)
				active = False
				continue
			# Start the game
			playing = True
			clearBoardLabel(wBoard)
			writeBoardLabel('L', "DIFFICULTY SELECTION", wBoard)
			crs.napms(500)
			sure = False
			# Select randomizer and difficulty
			while not sure:
				undrawGrid(wBoard)
				wBoard.addstr(1, 1, "DO YOU WANT TO USE")
				wBoard.addstr(2, 1, "YOUR PREFERRED")
				wBoard.addstr(3, 1, "DIFFICULTY, " + str(preferredDifficulty) + ", &")
				wBoard.addstr(4, 1, "RANDOMIZER, " + preferredRandomizer + "? [Y/N]")
				yn = 0
				while yn not in yesnoCodes:
					yn = wBoard.getch()
				if yn in noCodes:
					undrawGrid(wBoard)
					wBoard.addstr(1, 1, "PRESS \'B\' FOR 7-BAG")
					wBoard.addstr(2, 1, "\'R\' FOR SHUFFLE,")
					wBoard.addstr(3, 1, "OR \'G\' FOR TGM")
					wBoard.addstr(4, 1, "RANDOMIZER:  ")
					wBoard.refresh()
					r = 0
					while r not in ( \
						ord('B'), ord('b'), ord('R'), ord('r'), ord('G'), ord('g') \
					):
						r = wBoard.getch()
					wBoard.addstr(5, 1, "PRESS A NUMBER 0-9")
					wBoard.addstr(6, 1, "TO SET DIFFICULTY:")
					wBoard.refresh()
					# The ASCII number-key codes in hexidecimal
					# Have the number as the first digit
					k = 0
					while k < 0x30 or k > 0x39:
						k = wBoard.getch()
					difficulty = k - 0x30
				elif yn in yesCodes:
					wBoard.addch(4, 17, 'Y', crs.A_REVERSE)
					r = ord(preferredRandomizer)
					difficulty = preferredDifficulty
				if chr(r).upper() == 'R':
					randomizer = "SHUFFLE"
				elif chr(r).upper() == 'B':
					randomizer = "BAG"
				elif chr(r).upper() == 'G':
					randomizer = "TGM"
					recentPieces = []
					nextPID = rnd.choice(('L', 'R', 'T', 'I'))
				# Show difficulty
				wBoard.addstr(8, 1, "YOU CHOSE DIFF. " + str(difficulty))
				wBoard.addstr(9, 1, "AND RANDOMIZER " + chr(r).upper())
				# Initialize the ghost piece (or don't)
				wBoard.addstr(11, 1, "DO YOU WANT TO USE")
				wBoard.addstr(12, 1, "THE GHOST PIECE?")
				wBoard.addstr(13, 1, "[Y/N]")
				wBoard.refresh()
				k = 0
				while k not in yesnoCodes:
					k = wBoard.getch()
				doGhost[0] = k in yesCodes
				if k in yesCodes:
					wBoard.addch(13, 2, 'Y', crs.A_REVERSE)
				else:
					wBoard.addch(13, 4, 'N', crs.A_REVERSE)
				# Confirm settings
				wBoard.addstr(15, 1, "ARE YOU ALL SET?")
				wBoard.addstr(16, 1, "[Y/N]")
				wBoard.refresh()
				k = 0
				while k not in yesnoCodes:
					k = wBoard.getch()
				# Proceed to game start
				if k in yesCodes:
					sure = True
					wBoard.addch(16, 2, 'Y', crs.A_REVERSE)
					wBoard.addstr(18, 1, "OKAY, GET READY!")
					wBoard.refresh()
					crs.napms(500)
				# Retry difficulty selection
				else:
					undrawGrid(wBoard)
					wBoard.addstr(1, 1, "OKAY, CHOOSE AGAIN.")
					wBoard.refresh()
				crs.napms(1000)
				drawGrid(wBoard)
			clearBoardLabel(wBoard)
			writeBoardLabel('C', "BEGINNING GAME...", wBoard)
			crs.napms(750)
			# Clear old scores
			for s in scoreData.keys():
				scoreData[s] = 0
				clearScore(s, wScore, wStats)
			wScore.refresh()
			wStats.refresh()
			clearBoardLabel(wBoard)
			writeBoardLabel('C', "LEVEL " + str(difficulty), wBoard)
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
				clearBoardLabel(wBoard)
				writeBoardLabel('C', "PRESS ENTER TO QUIT", wBoard)
				# To avoid accidental quits, confirm with enter key
				if wBoard.getch() == ord('\n'):
					clearBoardLabel(wBoard)
					writeBoardLabel('C', "QUITTING...", wBoard)
					crs.napms(750)
					active = False
					continue
				clearBoardLabel(wBoard)
				writeBoardLabel('C', "PAUSED", wBoard)
				continue
			elif keypress == "ENTER":
				continue
			elif keypress == 'G' and allowGhostToggle:
				if doGhost[0]:
					piece.undrawGhost(wBoard)
				doGhost[0] = not doGhost[0]
				if doGhost[0]:
					piece.drawGhost(wBoard)
				continue
			# If neither the enter nor q key are pressed, it must be ESC,
			# Which means unpause
			# (not true anymore since G can be ignored with settings)
			elif keypress == "ESC":
				clearBoardLabel(wBoard)
				writeBoardLabel('C', "LEVEL " + str(difficulty), wBoard)
				wBoard.nodelay(True)
				paused = False
				continue
			continue
		# SUBSECTION: PIECE GENERATION
		if not pieceInPlay:
			# Create new piece object
			piece = Piece( \
				pieceInfo[nextPID]['y'], \
				pieceInfo[nextPID]['x'], \
				nextPID, \
				pieceInfo[nextPID]["orient"], \
				wBoard \
			)
			pieceJustSpawned = True
			pieceToDrop = False
			# Go to the next piece and check if the bag needs shuffling
			# if using the bag randomizer
			if randomizer == "SHUFFLE":
				bagIndex = rnd.randint(0, 6)
			elif randomizer == "BAG":
				bagIndex += 1
				if bagIndex % 7 < (bagIndex - 1) % 7:
					rnd.shuffle(pieceBag)
			elif randomizer == "TGM":
				recentPieces.insert(0, nextPID)
				for n in range(5):
					r = rnd.randint(0, 6)
					if pieceBag[r] not in recentPieces:
						break
				if len(recentPieces) > 5:
					recentPieces.pop()
				bagIndex = r
			#	writeBoardLabel('C', ','.join(recentPieces), wBoard)
			nextPID = pieceBag[bagIndex % 7]
			# Clear the next piece window and draw the next piece
			changeTexture(1, 7, 2, 17, ' ', crs.ACS_CKBOARD, wNextP)
			drawPiece( \
				pieceInfo[nextPID]["yn"], pieceInfo[nextPID]["xn"], \
				pieceInfo[nextPID]["orient"], nextPID, wNextP, [crs.ACS_CKBOARD] \
			)
			wNextP.refresh()
			pieceInPlay = True
			# Reset the T-Spin boolean if necessary
			if tSpun:
				tSpun = False
				clearBoardLabel(wBoard)
				writeBoardLabel('C', "LEVEL " + str(difficulty), wBoard)
			# Set the autodrop timer
			pieceDropTime = time.time()
			continue
		# SUBSECTION: PIECE AUTODROP, GAME OVER, AND LINE CLEAR
		if time.time() - pieceDropTime > dropTimes[difficulty] or pieceDropped:
			# Under normal circumstances
			if piece.canMove('D', wBoard):
				piece.move('D', wBoard)
				pieceDropTime = time.time()
				pieceJustSpawned = False
			# When the piece it at the bottom
			else:
				if pieceDropped:
					dropDelay = False
				pieceInPlay = False
				pieceDropped = False
				atBottom = False
				canHold = True
				# Game over check
				if pieceJustSpawned:
					for n in range(4):
						crs.flash()
						crs.napms(125)
					holdPID = ''
					changeTexture(4, 7, 5, 17, ' ', crs.ACS_CKBOARD, wNextP)
					wNextP.refresh()
					clearBoardLabel(wBoard)
					writeBoardLabel('C', "GAME OVER!", wBoard)
					wBoard.addstr(19, 1, "PRESS SPACE TO START")
					wBoard.addstr(20, 1, "    A NEW GAME      ")
					crs.napms(2000)
					playing = False
					checkScore = True
					continue
				pieceJustSpawned = False
				wBoard.refresh()
				# Add softDrops to score and update piece statistics
				scoreData["SCORE"] += softDrops
				softDrops = 0
				writeScore(scoreData["SCORE"], "SCORE", wScore, wStats)
				wScore.refresh()
				scoreData["STAT" + piece.pID] += 1
				writeScore(scoreData["STAT" + piece.pID], "STAT" + piece.pID, wScore, wStats)
				wStats.refresh()
				# Erase old piece object
				del piece
				# Check if lines can be cleared
				lines = getFullLines(wBoard)
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
						crs.napms(50)
					# Clear the lines
					for y in lines:
						for x in range(1, 11):
							setCellValue(y, x, "EMPTY", wBoard)
					# From the topmost line, drop down the remaining blocks
					for y in reversed(lines):
						j = y
						while not isLineEmpty(j - 1, wBoard):
							for x in range(1, 11):
								setCellValue(j, x, cellValues[getCellValue(j - 1, x, wBoard)], wBoard)
								setCellValue(j - 1, x, "EMPTY", wBoard)
							j -= 1
						wBoard.refresh()
						crs.napms(50)
					# Update scoreData and score labels
					scoreData["LINES"] += len(lines)
					if tSpun:
						scoreData["SCORE"] += 2 * lineClearScores[len(lines)] * (difficulty + 1)
						for n in range(2):
							crs.flash()
							crs.napms(125)
						writeBoardLabel('C', "T-SPIN DETECTED!", wBoard)
						crs.napms(250)
					else:
						scoreData["SCORE"] += lineClearScores[len(lines)] * (difficulty + 1)
					writeScore(scoreData["LINES"], "LINES", wScore, wStats)
					writeScore(scoreData["SCORE"], "SCORE", wScore, wStats)
					wScore.refresh()
					scoreData["STAT" + str(len(lines))] += 1
					writeScore(scoreData["STAT" + str(len(lines))], "STAT" + str(len(lines)), wScore, wStats)
					wStats.refresh()
					# Update difficulty check
					if lineClearDiffShifts[difficulty] <= scoreData["LINES"] and \
						difficulty < 9:
						difficulty += 1
						clearBoardLabel(wBoard)
						writeBoardLabel('C', "LEVEL " + str(difficulty), wBoard)
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
		if keypress in arrowCodes and pieceInPlay:
			if keypress != 'U':
				pieceToDrop = False
				if piece.canMove(keypress, wBoard):
					piece.move(keypress, wBoard)
					if keypress == 'D':
						pieceDropTime = time.time()
						softDrops += 1
					if not piece.canMove('D', wBoard) and not atBottom:
						pieceDropTime = time.time() + 0.25
						atBottom = True
					pieceJustSpawned = False
			# pieceToDrop Boolean is used to check for double press of up arrow key
			else:
				if not pieceToDrop:
					pieceToDrop = True
					continue
				while piece.canMove('D', wBoard):
					piece.move('D', wBoard)
					softDrops += 1
					pieceJustSpawned = False
				pieceToDrop = False
				pieceDropped = True
		elif keypress in rotateCodes and pieceInPlay:
			rotDir = "CW" if keypress == "SPACE" else "CCW"
			if piece.canRotate(rotDir, wBoard):
				piece.rotate(rotDir, wBoard)
				if piece.pID == 'T' and ( not piece.canMove('D', wBoard) ) \
					and ( not isCellEmpty(piece.y, piece.x, wBoard) \
					or not isCellEmpty(piece.y, piece.x + 2, wBoard) ):
					tSpun = True
				pieceJustSpawned = False
		elif keypress == 'H' and allowHoldFeature and pieceInPlay and canHold:
			# Remove active piece from the board
			piece.undraw(wBoard)
			piece.undrawGhost(wBoard)
			# Stow or swap the active piece into the hold slot
			if holdPID == '':
				holdPID = piece.pID
				pieceInPlay = False
				del piece
			else:
				oldPID = piece.pID
				del piece
				piece = Piece( \
					pieceInfo[holdPID]['y'], \
					pieceInfo[holdPID]['x'], \
					holdPID, \
					pieceInfo[holdPID]["orient"],
					wBoard \
				)
				holdPID = oldPID
				pieceJustSpawned = True
				pieceDropTime = time.time()
			# Draw the new hold piece
			changeTexture(4, 7, 5, 17, ' ', crs.ACS_CKBOARD, wNextP)
			drawPiece( \
				pieceInfo[holdPID]["yn"] + 3, pieceInfo[holdPID]["xn"], \
				pieceInfo[holdPID]["orient"], holdPID, wNextP, [crs.ACS_CKBOARD] \
			)
			wNextP.refresh()
			# Disallow holding until the swapped piece is finished
			canHold = False
		elif keypress == "ESC":
			paused = True
			clearBoardLabel(wBoard)
			writeBoardLabel('C', "PAUSED", wBoard)
	return None

# SECTION: MAIN
#Set ESC key delay time
os.environ.setdefault('ESCDELAY', '25')
#Initialize screen
screen = crs.initscr()
crs.start_color()
crs.use_default_colors()
#Run screen checks
if crs.LINES < 24 or crs.COLS < 72:
	crs.endwin()
	print("Your terminal must be at least 72x24 to run this game.")
	print("Please adjust your terminal settings accordingly.")
	exit()
#Define colors
if crs.can_change_color():
	crs.init_color(1, 1000, 0, 0)
	crs.init_color(2, 0, 1000, 0)
	crs.init_color(3, 1000, 1000, 0)
	crs.init_color(4, 0, 0, 1000)
	crs.init_color(5, 1000, 500, 1000)
	crs.init_color(6, 500, 500, 1000)
	crs.init_color(7, 1000, 750, 325)
	
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
wBoard = crs.newwin(24, 22, 0, 27)
wBoard.keypad(True)
wBoard.nodelay(True)
wNextP = crs.newwin(7, 19, 0, 51)
wStats = crs.newwin(17, 19, 7, 51)
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
wCntrl.addstr(2, 1, " ,  ,  : MOVE PIECE")
wCntrl.addch(2, 1, crs.ACS_LARROW)
wCntrl.addch(2, 4, crs.ACS_RARROW)
wCntrl.addch(2, 7, crs.ACS_DARROW)
wCntrl.addstr(3, 1, "    x2 : DROP PIECE")
wCntrl.addch(3, 3, crs.ACS_UARROW)
wCntrl.addstr(4, 1, " SPACE : ROTATE CW")
wCntrl.addstr(5, 1, " CTRL+ : ROTATE CCW")
wCntrl.addstr(6, 1, " SPACE :")
wCntrl.addstr(7, 1, "     H : HOLD PIECE")
wCntrl.addstr(8, 1, " ESC,P : PAUSE OR")
wCntrl.addstr(9, 1, "       : RESUME")
wCntrl.addstr(10, 6, "IF PAUSED:")
wCntrl.addstr(11, 1, "     Q : QUIT GAME")
wCntrl.addstr(12, 1, "     G : TOGGLE GHOST")
drawGrid(wBoard)
drawBoardBorder(wBoard)
writeBoardLabel('L', "PRESS SPACE TO START", wBoard)
wNextP.addstr(1, 1, "NEXT")
wNextP.addstr(2, 1, "PIECE")
wNextP.hline(3, 1, crs.ACS_HLINE, 17)
wNextP.addstr(4, 1, "HOLD")
wNextP.addstr(5, 1, "PIECE")
wNextP.vline(1, 7, crs.ACS_VLINE, 5)
wNextP.addch(3, 7, crs.ACS_PLUS)
#wNextP.addstr(2, 2, 11 * '-')
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
writeScore(0, "SCORE", wScore, wStats)
writeScore(0, "LINES", wScore, wStats)
writeScore(0, "STATC", wScore, wStats)
writeScore(0, "STATS", wScore, wStats)
writeScore(0, "STATZ", wScore, wStats)
writeScore(0, "STATL", wScore, wStats)
writeScore(0, "STATR", wScore, wStats)
writeScore(0, "STATI", wScore, wStats)
writeScore(0, "STATT", wScore, wStats)
writeScore(0, "STAT1", wScore, wStats)
writeScore(0, "STAT2", wScore, wStats)
writeScore(0, "STAT3", wScore, wStats)
writeScore(0, "STAT4", wScore, wStats)
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
#Display error message if screen shrunk too far
if resizedTooSmall:
	print("The terminal was resized beyond the minimum requirements of 72x24.")
	print("This program is designed to shut down if the terminal is too small,")
	print("as it is a pain to implement resizing for such a specific screen area.")
	print("Please prevent small resizes from happening in the future.")
elif missingSettings:
	print("The settings.json file is missing from your local directory/folder.")
	print("You can find a reference copy of it on the github repository, at:")
	print("\thttps://github.com/cSquaerd/CursaTetra.git")
	print("Please download it and place in the directory/folder where you are currently.")
