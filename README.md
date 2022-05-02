# sudokool
## Introduction
Sudoku puzzles were invented in the 1700’s by the Swiss mathematician, Leonhard Euler, and
have become widely popular in recent times. The format of these puzzles is very simple: given an
n by n grid, with some squares filled in with a number between 1 and n, the player tries to find
an arrangement for the grid such that no number repeats twice in the column or row. If such
arrangement exists, it is said to be a solution of the puzzle. Furthermore, if there is only one solution, then the solution is unique.
Often times, there are additional constraints that are introduced to increase difficulty, such as
cutting up the grid into subgrids of n boxes, which must also contain no repeats.

We are tasked to develop an algorithm which constructs Sudoku puzzles with unique solutions
of 4 difficulty levels and to minimize the complexity of the algorithm. In order to do this, we
propose the following research plan:
## Research Plan
Our research plan is divided into five phases:
1. Creating Completed Grids: We will develop an algorithm that yields a basic 9 x 9 Sudoku
grid. Numbers will be randomized using the Unix urandom binary to ensure a reasonable
degree of randomness.
2. Generating Seed Puzzles: Using the “dig-in” algorithm, Sudoku puzzles with varying de-
grees of difficulty will be created. One of the limitations of Zhang’s algorithm is that the
highest difficulty left 22 numbers on the grid. However, the theoretical minimum number of
numbers in a 9 x 9 grid that has a unique solution is 17 (Zhang, p. 4). Our goal for this project
is for our algorithm to utilize only 17 numbers at the maximum difficulty. In this step, we will
generate 4 puzzles of varying difficulty, which will be determined in phase 3.
3. Designating Heuristics to Assess Difficulty: To assess difficulty of our puzzles, it is nec-
essary to develop some sort of heuristic that ranks them. (Possibly on a scale from 0-100).
Factors that could rank a puzzle based on difficulty will be assessed.
4. Randomizing Seed Puzzles: We will develop a randomizing algorithm that takes a seed
puzzle and scrambles it while maintaining an unique solution, efffectively creating a new
puzzle.
5. Creating an Interactive Version: Finally, a long term goal for our project is to create a playable
version online alongside a research paper that highlights our findings.
