from random import randint, sample

# sudoku puzzles can be separated into groups of 3 x 3 squares
GROUPS = 3
NTH = GROUPS * 3

# initialize puzzle matrix with all zeros
def genZeros():
    return [[0 for _ in range(0, NTH)] for _ in range(0, NTH)]

puzzle = genZeros()
savedPuzzle = genZeros()
initialPuzzle = genZeros()

# transfer puzzle data from one matrix reference to another
def transferPuzzle(initial, new):
    for row in range(0, NTH):
        for column in range(0, NTH):
            new[row][column] = initial[row][column] 

# reset puzzle reference to all zeros       
def setPuzzle():
    for row in range(0, NTH):
        for column in range(0, NTH):
            puzzle[row][column] = 0

# save digged puzzle
def savePuzzle(): transferPuzzle(puzzle, savedPuzzle)

# restore digged puzzle
def restorePuzzle(): transferPuzzle(savedPuzzle, puzzle)

# save initially solved puzzle
def saveInitialPuzzle(): transferPuzzle(puzzle, initialPuzzle)

# check if computer-solved solution is the same as the initial solution
def sameSolution():
    for row in range(0, NTH):
        for column in range(0, NTH):
            if puzzle[row][column] != initialPuzzle[row][column]:
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
    print("Blanks: {}, Entries: {}\n\n".format(zeros, 81 - zeros))

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
        for row in range(0, NTH): # for each neighborhood
            for column in range(0, NTH):
                if puzzle[row][column] != 0: # if cell is already filled, don't retry
                    continue
                nums = getAppNumbers(row, column) # get applicable numbers
                # no available numbers
                if (len(nums) == 0):
                    restorePuzzle() if restore else setPuzzle() # revert back to initial puzzle
                    fails += 1 # count number of cycles
                    failed = True # break out of loop
                    break
                else:
                    index = randint(0, len(nums) - 1) # choose a random number to fill
                    puzzle[row][column] = nums[index]
            if failed:
                break
        if failed:
            failed = False
        else:
            break
    return fails

def dig():
    dug = 0
    it = 0
    while dug < 45: # assert that the number of cells dug is at least 45 (this number changes based on difficulty)
        it += 1
        if it > 100: # try to randomly dig 100 times. if we still haven't reached the optimum number, restart
            transferPuzzle(initialPuzzle, puzzle)
            it = 0
            dug = 0
        for row in sample(range(0, GROUPS), GROUPS - 1):
            for col in sample(range(0, GROUPS), GROUPS - 1): # choose a random neighborhood
                nums = sample(range(1, NTH), NTH - 1) 
                for num in nums:
                    r = row * GROUPS + (num % GROUPS) # randomize neighborhood order
                    c = col * GROUPS + (num // GROUPS)
                    # print("({}, {})".format(r, c))
                    entry = puzzle[r][c]
                    if entry == 0: # no need to repeat dig
                        continue 
                    puzzle[r][c] = 0 # attempt dig
                    appnums = getAppNumbers(r, c)
                    if len(appnums) == 1: # if there are multiple solutions, don't dig
                        dug += 1
                        break
                    else:
                        puzzle[r][c] = entry # place entry back
                    

print("Generating:")
print("Cycles: {}".format(createSolvable()))
saveInitialPuzzle()
printPuzzle()           

print("Digging:")
dig()  
savePuzzle()
printPuzzle()

cycles = []
for _ in range(0, 50):
    print("Solving: ")
    cycle = createSolvable(True)
    cycles.append(cycle)
    print("Cycles: {}".format(cycle))

    print("Equal: {}".format(sameSolution()))
    restorePuzzle()

printPuzzle()
print(cycles)

# def createSolvable2():
#     cycles = 0
#     while len(history) > 0:
#         cycles += 1
#         upuzzle, (ur, uc), uavail = history.pop()
#         transferPuzzle(upuzzle, puzzle)
#         while len(uavail) > 0:
#             # print(ur, uc, uavail)
#             if (puzzle[ur][uc] != 0):
#                 if uc == NTH - 1 and ur == NTH - 1:
#                     return cycles
#                 elif uc == NTH - 1:
#                     ur += 1
#                     uc = 0
#                 else:
#                     uc += 1
                
#                 uavail = getAppNumbers(ur, uc)
#                 shuffle(uavail)
#                 continue

#             choice = uavail.pop()
#             puzzle[ur][uc] = choice

#             cpuzzle = genZeros()
#             cavail = uavail.copy()
#             transferPuzzle(puzzle, cpuzzle)
#             history.append((cpuzzle, (ur, uc), cavail))

#             if uc == NTH - 1 and ur == NTH - 1:
#                 return cycles
#             elif uc == NTH - 1:
#                 ur += 1
#                 uc = 0
#             else:
#                 uc += 1
            
#             uavail = getAppNumbers(ur, uc)
#             shuffle(uavail)

#     return -1

# history: List[Tuple[
#     List[List[int]],
#     Tuple[int, int],
#     List[int]
# ]] = [(genZeros(), (0, 0), sample([x for x in range(1, NTH + 1)], 9))]