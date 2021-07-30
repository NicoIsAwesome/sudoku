# sudoku
sudoku(數獨)

## Sudoku數獨 wiki page
https://en.wikipedia.org/wiki/Sudoku

## Requirements (python2 only)
pip install pycosat

## Usage

### [1] edit the numberList in the sudoku.py
```
	numberList = [ \
		0, 2, 0, 0, 0, 0, 0, 0, 0, \
		0, 0, 0, 6, 0, 0, 0, 0, 3, \
        0, 7, 4, 0, 8, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 3, 0, 0, 2, \
        0, 8, 0, 0, 4, 0, 0, 1, 0, \
        6, 0, 0, 5, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 1, 0, 7, 8, 0, \
        5, 0, 0, 0, 0, 9, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 4, 0]
```

### [2] python sudoku.py
result:
```
126 437 958 
895 621 473 
374 985 126 
 
457 193 862 
983 246 517 
612 578 394 
 
269 314 785 
548 769 231 
731 852 649 
```

