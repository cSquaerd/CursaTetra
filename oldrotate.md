```Python
def rotate(piece, newOrient):
	if piece.pID == 'S':
		if newOrient == 'V':
			piece.undraw()
			piece.orient = newOrient
			piece.draw()
		#	setCellValue(piece.y + 2, piece.x, "EMPTY")
		#	setCellValue(piece.y + 1, piece.x + 2, "EMPTY")
		#	setCellValue(piece.y, piece.x, "ACTIVE")
		#	setCellValue(piece.y + 1, piece.x, "ACTIVE")
		elif newOrient == 'H':
			piece.undraw()
			piece.orient = newOrient
			piece.draw()
		#	setCellValue(piece.y, piece.x, "EMPTY")
		#	setCellValue(piece.y + 1, piece.x, "EMPTY")
		#	setCellValue(piece.y + 1, piece.x + 2, "ACTIVE")
		#	setCellValue(piece.y + 2, piece.x, "ACTIVE")
	elif piece.pID == 'Z':
		if newOrient == 'V':
			setCellValue(piece.y + 2, piece.x + 1, "EMPTY")
			setCellValue(piece.y + 2, piece.x + 2, "EMPTY")
			setCellValue(piece.y, piece.x + 1, "ACTIVE")
			setCellValue(piece.y + 2, piece.x, "ACTIVE")
		elif newOrient == 'H':
			setCellValue(piece.y, piece.x + 1, "EMPTY")
			setCellValue(piece.y + 2, piece.x , "EMPTY")
			setCellValue(piece.y + 2, piece.x + 1, "ACTIVE")
			setCellValue(piece.y + 2, piece.x + 2, "ACTIVE")
	elif piece.pID == 'L':
		if piece.orient == 'H':
			setCellValue(piece.y, piece.x + 1, "EMPTY")
			setCellValue(piece.y + 2, piece.x + 1, "EMPTY")
			setCellValue(piece.y + 2, piece.x + 2, "EMPTY")
			if newOrient == 'V':
				setCellValue(piece.y + 1, piece.x, "ACTIVE")
				setCellValue(piece.y + 1, piece.x + 2, "ACTIVE")
				setCellValue(piece.y + 2, piece.x, "ACTIVE")
			elif newOrient == 'VP':
				setCellValue(piece.y + 1, piece.x, "ACTIVE")
				setCellValue(piece.y, piece.x + 2, "ACTIVE")
				setCellValue(piece.y + 1, piece.x + 2, "ACTIVE")
		elif piece.orient == 'V':
			setCellValue(piece.y + 1, piece.x, "EMPTY")
			setCellValue(piece.y + 2, piece.x, "EMPTY")
			setCellValue(piece.y + 1, piece.x + 2, "EMPTY")
			if newOrient == 'H':
				setCellValue(piece.y, piece.x + 1, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 1, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 2, "ACTIVE")
			elif newOrient == 'HP':
				setCellValue(piece.y, piece.x, "ACTIVE")
				setCellValue(piece.y, piece.x + 1, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 1, "ACTIVE")
		elif piece.orient == 'HP':
			setCellValue(piece.y, piece.x, "EMPTY")
			setCellValue(piece.y, piece.x + 1, "EMPTY")
			setCellValue(piece.y + 2, piece.x + 1, "EMPTY")
			if newOrient == 'V':
				setCellValue(piece.y + 1, piece.x, "ACTIVE")
				setCellValue(piece.y + 1, piece.x + 2, "ACTIVE")
				setCellValue(piece.y + 2, piece.x, "ACTIVE")
			elif newOrient == 'VP':
				setCellValue(piece.y + 1, piece.x, "ACTIVE")
				setCellValue(piece.y, piece.x + 2, "ACTIVE")
				setCellValue(piece.y + 1, piece.x + 2, "ACTIVE")
		elif piece.orient == 'VP':
			setCellValue(piece.y, piece.x + 2, "EMPTY")
			setCellValue(piece.y + 1, piece.x, "EMPTY")
			setCellValue(piece.y + 1, piece.x + 2, "EMPTY")
			if newOrient == 'H':
				setCellValue(piece.y, piece.x + 1, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 1, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 2, "ACTIVE")
			elif newOrient == 'HP':
				setCellValue(piece.y, piece.x, "ACTIVE")
				setCellValue(piece.y, piece.x + 1, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 1, "ACTIVE")
	elif piece.pID == 'R':
		if piece.orient == 'H':
			setCellValue(piece.y, piece.x + 1, "EMPTY")
			setCellValue(piece.y + 2, piece.x, "EMPTY")
			setCellValue(piece.y + 2, piece.x + 1, "EMPTY")
			if newOrient == 'V':
				setCellValue(piece.y, piece.x, "ACTIVE")
				setCellValue(piece.y + 1, piece.x, "ACTIVE")
				setCellValue(piece.y + 1, piece.x + 2, "ACTIVE")
			elif newOrient == 'VP':
				setCellValue(piece.y + 1, piece.x, "ACTIVE")
				setCellValue(piece.y + 1, piece.x + 2, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 2, "ACTIVE")
		elif piece.orient == 'V':
			setCellValue(piece.y, piece.x, "EMPTY")
			setCellValue(piece.y + 1, piece.x, "EMPTY")
			setCellValue(piece.y + 1, piece.x + 2, "EMPTY")
			if newOrient == 'H':
				setCellValue(piece.y, piece.x + 1, "ACTIVE")
				setCellValue(piece.y + 2, piece.x, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 1, "ACTIVE")
			elif newOrient == 'HP':
				setCellValue(piece.y, piece.x + 1, "ACTIVE")
				setCellValue(piece.y, piece.x + 2, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 1, "ACTIVE")
		elif piece.orient == 'HP':
			setCellValue(piece.y, piece.x + 1, "EMPTY")
			setCellValue(piece.y, piece.x + 2, "EMPTY")
			setCellValue(piece.y + 2, piece.x + 1, "EMPTY")
			if newOrient == 'V':
				setCellValue(piece.y, piece.x, "ACTIVE")
				setCellValue(piece.y + 1, piece.x, "ACTIVE")
				setCellValue(piece.y + 1, piece.x + 2, "ACTIVE")
			elif newOrient == 'VP':
				setCellValue(piece.y + 1, piece.x, "ACTIVE")
				setCellValue(piece.y + 1, piece.x + 2, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 2, "ACTIVE")
		elif piece.orient == 'VP':
			setCellValue(piece.y + 1, piece.x, "EMPTY")
			setCellValue(piece.y + 1, piece.x + 2, "EMPTY")
			setCellValue(piece.y + 2, piece.x + 2, "EMPTY")
			if newOrient == 'H':
				setCellValue(piece.y, piece.x + 1, "ACTIVE")
				setCellValue(piece.y + 2, piece.x, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 1, "ACTIVE")
			elif newOrient == 'HP':
				setCellValue(piece.y, piece.x + 1, "ACTIVE")
				setCellValue(piece.y, piece.x + 2, "ACTIVE")
				setCellValue(piece.y + 2, piece.x + 1, "ACTIVE")

	piece.orient = newOrient
```
