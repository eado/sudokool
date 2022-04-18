from random import randint, sample

# sudoku puzzles can be separated into groups of 3 x 3 squares
GROUPS = 3
NTH = GROUPS * 3

# initialize puzzle matrix with all zeros
puzzle = [[0 for _ in range(0, NTH)] for _ in range(0, NTH)]
savedPuzzle = [[0 for _ in range(0, NTH)] for _ in range(0, NTH)]
def setPuzzle():
    for row in range(0, NTH):
        for column in range(0, NTH):
            puzzle[row][column] = 0

def savePuzzle():
    for row in range(0, NTH):
        for column in range(0, NTH):
            savedPuzzle[row][column] = puzzle[row][column] 

def restorePuzzle():
    for row in range(0, NTH):
        for column in range(0, NTH):
            puzzle[row][column] = savedPuzzle[row][column] 

def sameSolution():
    for row in range(0, NTH):
        for column in range(0, NTH):
            if puzzle[row][column] != savedPuzzle[row][column]:
                return False
    return True

# pretty print puzzle
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
    print("Blanks: {}\n\n".format(zeros))

def getNeighborhood(r, c):
    rx = int(r / GROUPS)
    cx = int(c / GROUPS)
    neigh = []
    for rn in range(rx * GROUPS, (rx * GROUPS) + GROUPS):
        for cn in range(cx * GROUPS, (cx * GROUPS) + GROUPS):
            neigh.append(puzzle[rn][cn])
    return neigh

# for a certain position in the matrix, get the possible valid numbers to fill
def getAppNumbers(r, c):
    arr = [x for x in range(1, NTH + 1)]
    # get row
    row = puzzle[r]
    arr = list(filter(lambda x: x not in row, arr))
    # get columns
    col = list(map(lambda row: row[c], puzzle))
    arr = list(filter(lambda x: x not in col, arr))
    # get neighborhood
    neigh = getNeighborhood(r, c)

    arr = list(filter(lambda x: x not in neigh, arr))

    return arr

# for each entry in the matrix, get the applicable numbers
# if no applicable numbers exist, restart the process
def createSolvable(restore = False):
    fails = 0
    failed = False
    while True:
        for row in range(0, NTH):
            for column in range(0, NTH):
                if puzzle[row][column] != 0:
                    continue
                nums = getAppNumbers(row, column)
                # no available numbers
                if (len(nums) == 0):
                    restorePuzzle() if restore else setPuzzle()
                    fails += 1
                    failed = True
                    break
                else:
                    index = randint(0, len(nums) - 1)
                    puzzle[row][column] = nums[index]
            if failed:
                break
        if failed:
            failed = False
        else:
            break
    return fails

def dig():
    # dig one from each neighborhood
    sets = []
    for _ in range(0, 9):
        for row in sample(range(0, GROUPS), GROUPS - 1):
            for col in sample(range(0, GROUPS), GROUPS - 1):
                num1 = randint(0, 8)
                num2 = randint(0, 8)
                n1 = puzzle[row * GROUPS + (num1 % GROUPS)][col * GROUPS + (num1 // GROUPS)]
                n2 = puzzle[row * GROUPS + (num2 % GROUPS)][col * GROUPS + (num2 // GROUPS)]

                # print(sets)
                if {n1, n2} not in sets:
                    puzzle[row * GROUPS + (num1 % GROUPS)][col * GROUPS + (num1 // GROUPS)] = 0
                    puzzle[row * GROUPS + (num2 % GROUPS)][col * GROUPS + (num2 // GROUPS)] = 0
                    sets.append({n1, n2})
                else:
                    puzzle[row * GROUPS + (num1 % GROUPS)][col * GROUPS + (num1 // GROUPS)] = 0
                    

print("Generating:")
print("Cycles: {}".format(createSolvable()))
printPuzzle()           

print("Digging:")
dig()  
savePuzzle()
printPuzzle()

print("Solving: ")
print("Cycles: {}".format(createSolvable(True)))
printPuzzle()

print("Equal: {}".format(sameSolution()))