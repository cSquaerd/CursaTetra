from ct_cell import *
from ct_draw import *
# Boolean that enables the ghost piece
# (Werid stuff happens if it changes during an unpaused game)
doGhost = [True]
pieceSchemaChecks = {
	'C': {
		"movement": {
			'': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}
		}
	}, 'S': {
		"rotation": {
			'H': { "empty": [(0, 0), (0, 1)], "bounds": [] },
			'V': { "empty": [(2, 1), (0, 2)], "bounds": [(2, 2)] }
		}, "movement": {
			'H': {
				'L': { "empty": [(-1, 2), (0, 1)], "bounds": [(-1, 2)] },
				'R': { "empty": [(3, 1), (2, 2)], "bounds": [(3, 2)] },
				'D': { "empty": [(0, 3), (1, 3), (2, 2)], "bounds": [(0, 3)] }
			}, 'V': {
				'L': { "empty": [(-1, 0), (-1, 1), (0, 2)], "bounds": [(-1, 2)] },
				'R': { "empty": [(2, 1), (2, 2), (1, 0)], "bounds": [(2, 2)] },
				'D': { "empty": [(1, 3), (0, 2)], "bounds": [(1, 3)] }
			}
		}
	}, 'Z': {
		"rotation": {
			'H': { "empty": [], "bounds": [] },
			'V': { "empty": [], "bounds": [] }
		}, "movement": {
			'H': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'V': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}
		}
	}, 'L': {
		"rotation": {
			'H': {
				"CW": { "empty": [], "bounds": [] },
				"CCW": { "empty": [], "bounds": [] }
			},
			'V': {
				"CW": { "empty": [], "bounds": [] },
				"CCW": { "empty": [], "bounds": [] }
			},
			'HP': {
				"CW": { "empty": [], "bounds": [] },
				"CCW": { "empty": [], "bounds": [] }
			},
			'VP': {
				"CW": { "empty": [], "bounds": [] },
				"CCW": { "empty": [], "bounds": [] }
			}
		}, "movement": {
			'H': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'V': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'HP': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'VP': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}
		}
	}, 'R': {
		"rotation": {
			'H': {
				"CW": { "empty": [], "bounds": [] },
				"CCW": { "empty": [], "bounds": [] }
			},
			'V': {
				"CW": { "empty": [], "bounds": [] },
				"CCW": { "empty": [], "bounds": [] }
			},
			'HP': {
				"CW": { "empty": [], "bounds": [] },
				"CCW": { "empty": [], "bounds": [] }
			},
			'VP': {
				"CW": { "empty": [], "bounds": [] },
				"CCW": { "empty": [], "bounds": [] }
			}
		}, "movement": {
			'H': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'V': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'HP': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'VP': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}
		}
	}, 'I': {
		"rotation": {
			'H': { "empty": [], "bounds": [] },
			'V': { "empty": [], "bounds": [] }
		}, "movement": {
			'H': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'V': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}
		}
	}, 'T': {
		"rotation": {
			'H': { "empty": [], "bounds": [] },
			'V': { "empty": [], "bounds": [] },
			'HP': { "empty": [], "bounds": [] },
			'VP': { "empty": [], "bounds": [] }
		}, "movement": {
			'H': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'V': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'HP': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}, 'VP': {
				'L': { "empty": [], "bounds": [] },
				'R': { "empty": [], "bounds": [] },
				'D': { "empty": [], "bounds": [] }
			}
		}
	}
}
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
	global doGhost
	def __init__(self, y, x, p, o, board):
		self.y = y
		self.x = x
		self.pID = p
		self.orient = o
		self.hasLanded = False
		self.ghostDepth = 0
		self.drawGhost(board)
		self.draw(board)
	def draw(self, board):
		drawPiece(self.y, 2 * self.x - 1, self.orient, self.pID, board, [crs.ACS_CKBOARD])
	def undraw(self, board):
		drawPiece(self.y, 2 * self.x - 1, self.orient, self.pID, board, ". ")
	def getGhostDepth(self, board):
		originalY = self.y
		while self.canMove('D', board):
			self.y += 1
		self.ghostDepth = self.y
		self.y = originalY
	def drawGhost(self, board):
		if not doGhost[0]:
			return None
		self.getGhostDepth(board)
		drawPiece( \
			self.ghostDepth, 2 * self.x - 1, \
			self.orient, self.pID, board, \
			ghostChars \
		)
	def undrawGhost(self, board):
		if not doGhost[0]:
			return None
		drawPiece(self.ghostDepth, 2 * self.x - 1, self.orient, self.pID, board, ". ")
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
	def rotate(self, rotDir, board):
		self.undraw(board)
		self.undrawGhost(board)
		self.orient = self.getNewOrient(rotDir)
		self.drawGhost(board)
		self.draw(board)
	def move(self, direction, board):
		yShift = 1 if direction == 'D' else 0
		xShift = 1 if direction == 'R' else -1 if direction == 'L' else 0
		self.undraw(board)
		self.undrawGhost(board)
		self.y += yShift
		self.x += xShift
		self.drawGhost(board)
		self.draw(board)
	def canRotate(self, direction, board):
		if self.pID == 'S':
			for cell in pieceSchemaChecks['S']["rotation"][self.orient]["empty"]:
				if not isCellEmpty(self.y + cell[1], self.x + cell[0], board):
					return False
			for cell in pieceSchemaChecks['S']["rotation"][self.orient]["bounds"]:
				if not isCellInBounds(self.y + cell[1], self.x + cell[0]):
					return False
			return True
		#	if self.orient == 'H' and isCellEmpty(self.y, self.x, board) and \
		#		isCellEmpty(self.y + 1, self.x, board):
		#		return True
		#	elif self.orient == 'V' and isCellEmpty(self.y + 1, self.x + 2, board) and \
		#		isCellEmpty(self.y + 2, self.x, board) and \
		#		isCellInBounds(self.y + 2, self.x + 2):
		#		return True
		elif self.pID == 'Z':
			if self.orient == 'H' and isCellEmpty(self.y, self.x + 1, board) and \
				isCellEmpty(self.y + 2, self.x, board):
				return True
			elif self.orient == 'V' and isCellEmpty(self.y + 2, self.x + 1, board) and \
				isCellEmpty(self.y + 2, self.x + 2, board) and \
				isCellInBounds(self.y + 2, self.x + 2):
				return True
		elif self.pID == 'L':
			if self.orient == 'H':
				if direction == 'CW' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 1, self.x, board) and isCellEmpty(self.y + 2, self.x, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
				elif direction == 'CCW' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 1, self.x, board) and isCellEmpty(self.y, self.x + 2, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
			elif self.orient == 'V':
				if direction == 'CW' and isCellEmpty(self.y, self.x, board) and \
					isCellEmpty(self.y, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board):
					return True
				elif direction == 'CCW' and isCellEmpty(self.y, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
			elif self.orient == 'HP':
				if direction == 'CW' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x, board) and isCellEmpty(self.y, self.x + 2, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
				elif direction == 'CCW' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x, board) and isCellEmpty(self.y + 2, self.x, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
			elif self.orient == 'VP':
				if direction == 'CW' and isCellEmpty(self.y, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
				elif direction == 'CCW' and isCellEmpty(self.y, self.x, board) and \
					isCellEmpty(self.y, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board):
					return True
		elif self.pID == 'R':
			if self.orient == 'H':
				if direction == 'CW' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x, board) and isCellEmpty(self.y, self.x, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
				elif direction == 'CCW' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y + 1, self.x, board) and isCellEmpty(self.y + 2, self.x + 2, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
			elif self.orient == 'V':
				if direction == 'CW' and isCellEmpty(self.y, self.x + 1, board) and \
					isCellEmpty(self.y, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board):
					return True
				elif direction == 'CCW' and isCellEmpty(self.y, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
			elif self.orient == 'HP':
				if direction == 'CW' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 1, self.x, board) and isCellEmpty(self.y + 2, self.x + 2, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
				elif direction == 'CCW' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y, self.x, board) and isCellEmpty(self.y + 1, self.x, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
			elif self.orient == 'VP':
				if direction == 'CW' and isCellEmpty(self.y, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board):
					return True
				elif direction == 'CCW' and isCellEmpty(self.y, self.x + 1, board) and \
					isCellEmpty(self.y, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board):
					return True
		elif self.pID == 'I':
			if self.orient == 'H' and isCellInBounds(self.y + 3, self.x + 3) and \
				isCellInBounds(self.y + 3, self.x) and \
				isCellEmpty(self.y + 2, self.x, board) and \
				isCellEmpty(self.y + 2, self.x + 2, board) and \
				isCellEmpty(self.y + 2, self.x + 3, board):
				return True
			elif self.orient == 'V' and isCellInBounds(self.y + 3, self.x + 1) and \
				isCellEmpty(self.y, self.x + 1, board) and \
				isCellEmpty(self.y + 1, self.x + 1, board) and \
				isCellEmpty(self.y + 3, self.x + 1, board):
				return True
		elif self.pID == 'T':
			if self.orient == 'H' and isCellEmpty(self.y, self.x + 1, board):
				return True
			elif self.orient == 'V' and isCellEmpty(self.y + 1, self.x + 2, board) and \
				isCellInBounds(self.y + 2, self.x + 2):
				return True
			elif self.orient == 'HP' and isCellEmpty(self.y + 2, self.x + 1, board):
				return True
			elif self.orient == 'VP' and isCellEmpty(self.y + 1, self.x, board) and \
				isCellInBounds(self.y + 2, self.x):
				return True
		return False
	def canMove(self, direction, board):
		if self.pID == 'C':
			if direction == 'L' and isCellInBounds(self.y + 1, self.x - 1) and \
				isCellEmpty(self.y, self.x - 1, board) and \
				isCellEmpty(self.y + 1, self.x - 1, board):
				return True
			elif direction == 'R' and isCellInBounds(self.y + 1, self.x + 2) and \
				isCellEmpty(self.y, self.x + 2, board) and \
				isCellEmpty(self.y + 1, self.x + 2, board):
				return True
			elif direction == 'D' and isCellInBounds(self.y + 2, self.x) and \
				isCellEmpty(self.y + 2, self.x, board) and \
				isCellEmpty(self.y + 2, self.x + 1, board):
				return True
		elif self.pID == 'S':
			for cell in pieceSchemaChecks['S']["movement"][self.orient][direction]["empty"]:
				if not isCellEmpty(self.y + cell[1], self.x + cell[0], board):
					return False
			for cell in pieceSchemaChecks['S']["movement"][self.orient][direction]["bounds"]:
				if not isCellInBounds(self.y + cell[1], self.x + cell[0]):
					return False
			return True
		#	if self.orient == 'H':
		#		if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
		#			isCellEmpty(self.y + 2, self.x - 1, board) and \
		#			isCellEmpty(self.y + 1, self.x, board):
		#			return True
		#		elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
		#			isCellEmpty(self.y + 1, self.x + 3, board) and \
		#			isCellEmpty(self.y + 2, self.x + 2, board):
		#			return True
		#		elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
		#			isCellEmpty(self.y + 3, self.x, board) and \
		#			isCellEmpty(self.y + 3, self.x + 1, board) and \
		#			isCellEmpty(self.y + 2, self.x + 2, board):
		#			return True
		#	elif self.orient == 'V':
		#		if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
		#			isCellEmpty(self.y, self.x - 1, board) and \
		#			isCellEmpty(self.y + 1, self.x - 1, board) and \
		#			isCellEmpty(self.y + 2, self.x, board):
		#			return True
		#		elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
		#			isCellEmpty(self.y + 1, self.x + 2, board) and \
		#			isCellEmpty(self.y + 2, self.x + 2, board) and \
		#			isCellEmpty(self.y, self.x + 1, board):
		#			return True
		#		elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
		#			isCellEmpty(self.y + 3, self.x + 1, board) and \
		#			isCellEmpty(self.y + 2, self.x, board):
		#			return True
		elif self.pID == 'Z':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 2, self.x + 3, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x + 1, board) and \
					isCellEmpty(self.y + 3, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1, board) and \
					isCellEmpty(self.y + 2, self.x - 1, board) and \
					isCellEmpty(self.y, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board):
					return True
		elif self.pID == 'L':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y, self.x, board) and \
					isCellEmpty(self.y + 1, self.x, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 2, self.x + 3, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board) and \
					isCellEmpty(self.y, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 1, board) and \
					isCellEmpty(self.y + 3, self.x + 2, board):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1, board) and \
					isCellEmpty(self.y + 2, self.x - 1, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
			if self.orient == 'HP':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y, self.x - 1, board) and \
					isCellEmpty(self.y + 1, self.x, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 1, board) and \
					isCellEmpty(self.y + 1, self.x, board):
					return True
			elif self.orient == 'VP':
				if direction == 'L' and isCellInBounds(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1, board) and \
					isCellEmpty(self.y, self.x + 1, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y, self.x + 3, board) and \
					isCellEmpty(self.y + 1, self.x + 3, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
		elif self.pID == 'R':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x - 1, board) and \
					isCellEmpty(self.y + 1, self.x, board) and \
					isCellEmpty(self.y, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x, board) and \
					isCellEmpty(self.y + 3, self.x + 1, board):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y, self.x - 1, board) and \
					isCellEmpty(self.y + 1, self.x - 1, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3, board) and \
					isCellEmpty(self.y, self.x + 1, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
			if self.orient == 'HP':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y, self.x, board) and \
					isCellEmpty(self.y + 1, self.x, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y, self.x + 3) and \
					isCellEmpty(self.y, self.x + 3, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 1, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board):
					return True
			elif self.orient == 'VP':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3, board) and \
					isCellEmpty(self.y + 2, self.x + 3, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 2) and \
					isCellEmpty(self.y + 3, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
		elif self.pID == 'I':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y, self.x, board) and \
					isCellEmpty(self.y + 1, self.x, board) and \
					isCellEmpty(self.y + 2, self.x, board) and \
					isCellEmpty(self.y + 3, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 3, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board) and \
					isCellEmpty(self.y + 3, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 4, self.x + 1) and \
					isCellEmpty(self.y + 4, self.x + 1, board):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 2, self.x - 1, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 4) and \
					isCellEmpty(self.y + 2, self.x + 4, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x, board) and \
					isCellEmpty(self.y + 3, self.x + 1, board) and \
					isCellEmpty(self.y + 3, self.x + 2, board) and \
					isCellEmpty(self.y + 3, self.x + 3, board):
					return True
		elif self.pID == 'T':
			if self.orient == 'H':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
			elif self.orient == 'V':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1, board) and \
					isCellEmpty(self.y + 2, self.x, board) and \
					isCellEmpty(self.y, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 2) and \
					isCellEmpty(self.y, self.x + 2, board) and \
					isCellEmpty(self.y + 1, self.x + 2, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x) and \
					isCellEmpty(self.y + 3, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
			elif self.orient == 'HP':
				if direction == 'L' and isCellInBounds(self.y + 1, self.x - 1) and \
					isCellEmpty(self.y + 1, self.x - 1, board) and \
					isCellEmpty(self.y, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 1, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3, board) and \
					isCellEmpty(self.y, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y + 2, self.x, board) and \
					isCellEmpty(self.y + 2, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
			elif self.orient == 'VP':
				if direction == 'L' and isCellInBounds(self.y + 2, self.x) and \
					isCellEmpty(self.y, self.x, board) and \
					isCellEmpty(self.y + 1, self.x, board) and \
					isCellEmpty(self.y + 2, self.x, board):
					return True
				elif direction == 'R' and isCellInBounds(self.y + 2, self.x + 3) and \
					isCellEmpty(self.y + 1, self.x + 3, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board) and \
					isCellEmpty(self.y, self.x + 2, board):
					return True
				elif direction == 'D' and isCellInBounds(self.y + 3, self.x + 1) and \
					isCellEmpty(self.y + 3, self.x + 1, board) and \
					isCellEmpty(self.y + 2, self.x + 2, board):
					return True
		return False

