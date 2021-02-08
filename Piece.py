from ct_cell import *
from ct_draw import *
# Boolean that enables the ghost piece
# (Werid stuff happens if it changes during an unpaused game)
doGhost = [True]
pieceSchemaChecks = {
	'C': {
		"movement": {
			'': {
				'L': { "empty": [(-1, 0), (-1, 1)], "bounds": [(-1, 1)] },
				'R': { "empty": [(2, 0), (2, 1)], "bounds": [(2, 1)] },
				'D': { "empty": [(0, 2), (1, 2)], "bounds": [(0, 2)] }
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
			'H': { "empty": [(1, 0), (0, 2)], "bounds": [] },
			'V': { "empty": [(1, 2), (2, 2)], "bounds": [(2, 2)] }
		}, "movement": {
			'H': {
				'L': { "empty": [(-1, 1), (0, 2)], "bounds": [(-1, 2)] },
				'R': { "empty": [(3, 2), (2, 1)], "bounds": [(3, 2)] },
				'D': { "empty": [(0, 2), (1, 3), (2, 3)], "bounds": [(0, 3)] }
			}, 'V': {
				'L': { "empty": [(-1, 1), (-1, 2), (0, 0)], "bounds": [(-1, 2)] },
				'R': { "empty": [(2, 0), (2, 1), (1, 2)], "bounds": [(2, 2)] },
				'D': { "empty": [(0, 3), (1, 2)], "bounds": [(0, 3)] }
			}
		}
	}, 'L': {
		"rotation": {
			'H': {
				"CW": { "empty": [(0, 1), (0, 2), (2, 1)], "bounds": [(0, 2)] },
				"CCW": { "empty": [(0, 1), (2, 0), (2, 1)], "bounds": [(0, 2)] }
			}, 'V': {
				"CW": { "empty": [(0, 0), (1, 0), (1, 2)], "bounds": [] },
				"CCW": { "empty": [(1, 0), (1, 2), (2, 2)], "bounds": [] }
			}, 'HP': {
				"CW": { "empty": [(0, 1), (2, 0), (2, 1)], "bounds": [(2, 2)] },
				"CCW": { "empty": [(0, 1), (0, 2), (2, 1)], "bounds": [(2, 2)] }
			}, 'VP': {
				"CW": { "empty": [(1, 0), (1, 2), (2, 2)], "bounds": [] },
				"CCW": { "empty": [(0, 0), (1, 0), (1, 2)], "bounds": [] }
			}
		}, "movement": {
			'H': {
				'L': { "empty": [(0, 0), (0, 1), (0, 2)], "bounds": [(0, 2)] },
				'R': { "empty": [(2, 0), (2, 1), (3, 2)], "bounds": [(3, 2)] },
				'D': { "empty": [(1, 3), (2, 3)], "bounds": [(1, 3)] }
			}, 'V': {
				'L': { "empty": [(-1, 1), (-1, 2)], "bounds": [(-1, 2)] },
				'R': { "empty": [(1, 2), (3, 1)], "bounds": [(3, 2)] },
				'D': { "empty": [(0, 3), (1, 2), (2, 2)], "bounds": [(0, 3)] }
			}, 'HP': {
				'L': { "empty": [(-1, 0), (0, 1), (0, 2)], "bounds": [(-1, 2)] },
				'R': { "empty": [(2, 0), (2, 1), (2, 2)], "bounds": [(2, 2)] },
				'D': { "empty": [(0, 1), (1, 3)], "bounds": [(1, 3)] }
			}, 'VP': {
				'L': { "empty": [(-1, 1), (1, 0)], "bounds": [(-1, 1)] },
				'R': { "empty": [(3, 0), (3, 1)], "bounds": [(3, 1)] },
				'D': { "empty": [(0, 2), (1, 2), (2, 2)], "bounds": [(0, 2)] }
			}
		}
	}, 'R': {
		"rotation": {
			'H': {
				"CW": { "empty": [(0, 1), (0, 0), (2, 1)], "bounds": [(2, 2)] },
				"CCW": { "empty": [(0, 1), (2, 2), (2, 1)], "bounds": [(2, 2)] }
			}, 'V': {
				"CW": { "empty": [(1, 0), (2, 0), (1, 2)], "bounds": [] },
				"CCW": { "empty": [(1, 0), (1, 2), (0, 2)], "bounds": [] }
			}, 'HP': {
				"CW": { "empty": [(0, 1), (2, 2), (2, 1)], "bounds": [(0, 2)] },
				"CCW": { "empty": [(0, 0), (0, 1), (2, 1)], "bounds": [(0, 2)] }
			}, 'VP': {
				"CW": { "empty": [(1, 0), (0, 2), (1, 2)], "bounds": [] },
				"CCW": { "empty": [(1, 0), (2, 0), (1, 2)], "bounds": [] }
			}
		}, "movement": {
			'H': {
				'L': { "empty": [(-1, 2), (0, 1), (0, 0)], "bounds": [(-1, 2)] },
				'R': { "empty": [(2, 0), (2, 1), (2, 2)], "bounds": [(2, 2)] },
				'D': { "empty": [(0, 3), (1, 3)], "bounds": [(0, 3)] }
			}, 'V': {
				'L': { "empty": [(-1, 0), (-1, 1)], "bounds": [(-1, 1)] },
				'R': { "empty": [(1, 0), (3, 1)], "bounds": [(3, 1)] },
				'D': { "empty": [(0, 2), (1, 2), (2, 2)], "bounds": [(0, 2)] }
			}, 'HP': {
				'L': { "empty": [(0, 0), (0, 1), (0, 2)], "bounds": [(0, 2)] },
				'R': { "empty": [(3, 0), (2, 1), (2, 2)], "bounds": [(3, 0)] },
				'D': { "empty": [(1, 3), (2, 1)], "bounds": [(1, 3)] }
			}, 'VP': {
				'L': { "empty": [(-1, 1), (1, 2)], "bounds": [(-1, 2)] },
				'R': { "empty": [(3, 1), (3, 2)], "bounds": [(3, 2)] },
				'D': { "empty": [(0, 2), (1, 2), (2, 3)], "bounds": [(2, 3)] }
			}
		}
	}, 'I': {
		"rotation": {
			'H': { "empty": [(0, 2), (2, 2), (3, 2)], "bounds": [(0, 3), (3, 3)] },
			'V': { "empty": [(1, 0), (1, 1), (1, 3)], "bounds": [(1, 3)] }
		}, "movement": {
			'H': {
				'L': { "empty": [(0, 0), (0, 1), (0, 2), (0, 3)], "bounds": [(0, 3)] },
				'R': { "empty": [(2, 0), (2, 1), (2, 2), (2, 3)], "bounds": [(2, 3)] },
				'D': { "empty": [(1, 4)], "bounds": [(1, 4)] }
			}, 'V': {
				'L': { "empty": [(-1, 2)], "bounds": [(-1, 2)] },
				'R': { "empty": [(4, 2)], "bounds": [(4, 2)] },
				'D': { "empty": [(0, 3), (1, 3), (2, 3), (3, 3)], "bounds": [(0, 3)] }
			}
		}
	}, 'T': {
		"rotation": {
			'H': { "empty": [(1, 0)], "bounds": [] },
			'V': { "empty": [(2, 1)], "bounds": [(2, 2)] },
			'HP': { "empty": [(1, 2)], "bounds": [] },
			'VP': { "empty": [(0, 1)], "bounds": [(0, 2)] }
		}, "movement": {
			'H': {
				'L': { "empty": [(-1, 1), (0, 2)], "bounds": [(-1, 2)] },
				'R': { "empty": [(3, 1), (2, 2)], "bounds": [(3, 2)] },
				'D': { "empty": [(0, 2), (1, 3), (2, 2)], "bounds": [(0, 3)] }
			}, 'V': {
				'L': { "empty": [(0, 0), (-1, 1), (0, 2)], "bounds": [(-1, 2)] },
				'R': { "empty": [(2, 0), (2, 1), (2, 2)], "bounds": [(2, 2)] },
				'D': { "empty": [(0, 2), (1, 3)], "bounds": [(0, 3)] }
			}, 'HP': {
				'L': { "empty": [(0, 0), (-1, 1)], "bounds": [(-1, 1)] },
				'R': { "empty": [(2, 0), (3, 1)], "bounds": [(3, 1)] },
				'D': { "empty": [(0, 2), (1, 2), (2, 2)], "bounds": [(0, 2)] }
			}, 'VP': {
				'L': { "empty": [(0, 0), (0, 1), (0, 2)], "bounds": [(0, 2)] },
				'R': { "empty": [(2, 0), (3, 1), (2, 2)], "bounds": [(3, 2)] },
				'D': { "empty": [(1, 3), (2, 2)], "bounds": [(1, 3)] }
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
		if self.pID in ('L', 'R'):
			for cell in pieceSchemaChecks[self.pID]["rotation"][self.orient][direction]["empty"]:
				if not isCellEmpty(self.y + cell[1], self.x + cell[0], board):
					return False
			for cell in pieceSchemaChecks[self.pID]["rotation"][self.orient][direction]["bounds"]:
				if not isCellInBounds(self.y + cell[1], self.x + cell[0]):
					return False
			return True
		elif self.pID in ('S', 'Z', 'I', 'T'):
			for cell in pieceSchemaChecks[self.pID]["rotation"][self.orient]["empty"]:
				if not isCellEmpty(self.y + cell[1], self.x + cell[0], board):
					return False
			for cell in pieceSchemaChecks[self.pID]["rotation"][self.orient]["bounds"]:
				if not isCellInBounds(self.y + cell[1], self.x + cell[0]):
					return False
			return True
		else:
			return False
	def canMove(self, direction, board):
		for cell in pieceSchemaChecks[self.pID]["movement"][self.orient][direction]["empty"]:
			if not isCellEmpty(self.y + cell[1], self.x + cell[0], board):
				return False
		for cell in pieceSchemaChecks[self.pID]["movement"][self.orient][direction]["bounds"]:
			if not isCellInBounds(self.y + cell[1], self.x + cell[0]):
				return False
		return True
