import curses as crs
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
def writeScore(score, scoreType, scoreWnd, statsWnd):
	scoreIndex = scoreLabels.index(scoreType)
	if scoreIndex < 3:
		scoreWnd.addstr(scoreIndex, 16 - numDigits(score), str(score))
	else:
		statsWnd.addstr(scoreIndex, 18 - numDigits(score), str(score))
"""
Clears a score label
"""
def clearScore(scoreType, scoreWnd, statsWnd):
	scoreIndex = scoreLabels.index(scoreType)
	if scoreIndex < 3:
		scoreWnd.addstr(scoreIndex, 9, "      0")
	else:
		statsWnd.addstr(scoreIndex, 11, "      0")

"""
Writes a label to the lower section of the board;

The label can be left, center, or right aligned;
If the align argument is a string representation of
an integer, then the label will be written starting at
the numbered cell and will wrap around, allowing
for scrolling labels with repeated calls
"""
def writeBoardLabel(align, label, board):
	if align == 'L':
		x = 1
	elif align == 'C':
		x = (20 - len(label)) // 2 + 1
	elif align == 'R':
		x = 21 - len(label)
	else:
		x = int(align) - 1
		for c in label:
			board.addch(22, x % 20 + 1, c)
			x += 1
		return None

	board.addstr(22, x, label)
	board.refresh()
"""
Clears the lower section of the board
"""
def clearBoardLabel(board):
	board.addstr(22, 1, 20 * ' ')

