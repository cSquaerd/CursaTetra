# CursaTetra
## A terminal-bounded block-based puzzle game written in Python/Curses
### Piece orientations
* H : horizontal (default)
* V : vertical
* HP : horizontal, pi radians around (180 deg)
* VP : vertical, pi radians around (180 deg)
### Piece: Class for active block data
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
### Piece designations & diagrams
#### Based on specification in Game Boy version
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
		0.
		1.  [][]
		2.[][]
		```
		* Vertical
		```
		  012345
		0.[]
		1.[][]
		2.  []
		```
	* Observations:
		* Rotates about (2:3, 1) Clockwise (???)
* Z : Z-piece
	* Diagrams:
		* Horizontal
		```
		  012345
		0.
		1.[][]
		2.  [][]
		```
		* Vertical
		```
		  012345
		0.  []
		1.[][]
		2.[]
		```
	* Observations:
		* Rotates about (2:3, 1) Clockwise (???)
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
		* Rotates about (2:3, 2) Clockwise (???)
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
