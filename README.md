# CursaTetra
## A terminal-bounded block-based puzzle game written in Python/Curses

# Notes from development
## Piece orientations

* H : horizontal (default)
* V : vertical
* HP : horizontal, pi radians around (180 deg)
* VP : vertical, pi radians around (180 deg)

## Piece designations & diagrams
### Based on specification in Game Boy version

* Note: The orientation of the pieces may seem backwards at first glance; Consider it in terms of the orientation of an underline below the text character that identifies a piece

* C : Square
	* Diagram:
```
  012345
0.[][]
1.[][]
2.
```

	* Orientations:
		* None

* S : S-piece
	* Diagram:
```
  012345
0.  [][]
1.[][]
2.
```

	* Orientations:
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
	* Diagram:
```
  012345
0.[][]
1.  [][]
2.
```

	* Orientations:
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
	* Diagram:
```
  012345
0.  []
1.  []
2.  [][]
```

	* Orientations:
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
	* Diagram:
```
  012345
0.  []
1.  []
2.[][]
```

	* Orientations:
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
	* Diagram:
```
  01234567
0.  []
1.  []
2.  []
3.  []
```

	* Orientations:
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
	* Diagram:
```
  012345
0.
1.[][][]
2.  []
```

	* Orientations:
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
