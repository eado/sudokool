# sudoku puzzles can be separated into groups of 3 x 3 squares
from random import sample, randint


GROUPS = 3
NTH = GROUPS * 3

puzzle = []

# initialize puzzle matrix with all zeros
def genzeros():
    return [[0 for _ in range(0, NTH)] for _ in range(0, NTH)]

# transfer puzzle data from one matrix reference to another
def transferpuzzle(initial, new):
    for row in range(0, NTH):
        for column in range(0, NTH):
            new[row][column] = initial[row][column] 

def printPuzzle():
    zeros = 0
    for (r, row) in enumerate(puzzle):
        print("-" * (NTH * 2 + 7)) if r % 3 == 0 else None
        for (c, entry) in enumerate(row):
            print("| ", end="") if c % 3 == 0 else None
            num = "_" if entry == 0 else str(entry)
            zeros += 1 if entry == 0 else 0
            print(num + " ", end="")
        print("|")
    print("-" * (NTH * 2 + 7))

lines = []
while True:
    try:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    except EOFError:
        break

for row in lines:
    if row == "-" * (NTH * 2 + 7):
        continue
    stringnums = list(filter(lambda x: x != " " and x != "", "".join(row.split("|")).split(" ")))
    nums = list(map(lambda x: 0 if x == "_" else int(x), stringnums))
    puzzle.append(nums)

# tokenizing
tokens = sample(range(1, NTH + 1), NTH)
print(tokens)

for row in range(0, NTH):
    for column in range(0, NTH):
        val = puzzle[row][column] 
        if val == 0:
            continue
        puzzle[row][column] = tokens[val - 1]

# randomize stacks
def swaprows(r1, r2):
    puzzle[r1], puzzle[r2] = puzzle[r2], puzzle[r1]

def swapcols(c1, c2):
    for row in range(0, NTH):
        puzzle[row][c1], puzzle[row][c2] = puzzle[row][c2], puzzle[row][c1]

if randint(0, 1) == 0:
    swaprows(0, 3)
    swaprows(1, 4)
    swaprows(2, 5)

if randint(0, 1) == 0:
    swaprows(3, 6)
    swaprows(4, 7)
    swaprows(5, 8)

if randint(0, 1) == 0:
    swaprows(6, 0)
    swaprows(7, 1)
    swaprows(8, 2)

# randomize bands
if randint(0, 1) == 0:
    swapcols(0, 3)
    swapcols(1, 4)
    swapcols(2, 5)

if randint(0, 1) == 0:
    swapcols(3, 6)
    swapcols(4, 7)
    swapcols(5, 8)

if randint(0, 1) == 0:
    swapcols(6, 0)
    swapcols(7, 1)
    swapcols(8, 2)

# randomize rows
for row in range(0, GROUPS):
    if randint(0, 1) == 0:
        swaprows(3 * row + 0, 3 * row + 1)
    if randint(0, 1) == 0:
        swaprows(3 * row + 1, 3 * row + 2)
    if randint(0, 1) == 0:
        swaprows(3 * row + 2, 3 * row + 0)

# randomize cols
for col in range(0, GROUPS):
    if randint(0, 1) == 0:
        swapcols(3 * col + 0, 3 * col + 1)
    if randint(0, 1) == 0:
        swapcols(3 * col + 1, 3 * col + 2)
    if randint(0, 1) == 0:
        swapcols(3 * col + 2, 3 * col + 0)

# randomize transpose
if randint(0, 1) == 0:
    trans = genzeros()
    for row in range(0, NTH):
        for column in range(0, NTH):
            trans[row][column] = puzzle[column][row]

    transferpuzzle(trans, puzzle)

# randomize reflection rows
if randint(0, 1) == 0:
    swaprows(0, 8)
    swaprows(1, 7)
    swaprows(2, 6)
    swaprows(3, 5)

# randomize reflection cols
if randint(0, 1) == 0:
    swapcols(0, 8)
    swapcols(1, 7)
    swapcols(2, 6)
    swapcols(3, 5)

# randomize rotation
if randint(0, 1) == 0: 
    puzzle = [[puzzle[j][i] for j in range(len(puzzle))] for i in range(len(puzzle[0])-1,-1,-1)]

printPuzzle()