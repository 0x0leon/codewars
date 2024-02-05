
# https://www.codewars.com/kata/5588bd9f28dbb06f43000085/train/python
'''
For example, backtracking, constraint propagation, and heuristic search 
algorithms are more effective at solving Sudoku puzzles than 
brute-force methods.

'''
import codewars_test as test

N = 9


def validate_cell(sudoku, row, col, value):

    # check row -
    for x in range(9):
        if sudoku[row][x] == value:
            return False
    # check colum |
    for x in range(9):
        if sudoku[x][col] == value:
            return False

    # check sourrounding grid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + startRow][j + startCol] == value:
                return False

    return True


def sudoku_solver(puzzle, row=0, col=0):
    if row == N - 1 and col == N:
        return True

    if col == N:
        row += 1
        col = 0

    if puzzle[row][col] > 0:
        return sudoku_solver(puzzle, row, col + 1)

    for num in range(1, N + 1, 1):

        if validate_cell(puzzle, row, col, num):
            puzzle[row][col] = num

            if sudoku_solver(puzzle, row, col + 1):
                return puzzle

        puzzle[row][col] = 0
    return False


@test.describe("Fixed tests")
def fixed():

    @test.it("Should solve an easy puzzle")
    def fff():
        puzzle = [
            [0, 0, 6, 1, 0, 0, 0, 0, 8],
            [0, 8, 0, 0, 9, 0, 0, 3, 0],
            [2, 0, 0, 0, 0, 5, 4, 0, 0],
            [4, 0, 0, 0, 0, 1, 8, 0, 0],
            [0, 3, 0, 0, 7, 0, 0, 4, 0],
            [0, 0, 7, 9, 0, 0, 0, 0, 3],
            [0, 0, 8, 4, 0, 0, 0, 0, 6],
            [0, 2, 0, 0, 5, 0, 0, 8, 0],
            [1, 0, 0, 0, 0, 2, 5, 0, 0]
        ]

        solution = [
            [3, 4, 6, 1, 2, 7, 9, 5, 8],
            [7, 8, 5, 6, 9, 4, 1, 3, 2],
            [2, 1, 9, 3, 8, 5, 4, 6, 7],
            [4, 6, 2, 5, 3, 1, 8, 7, 9],
            [9, 3, 1, 2, 7, 8, 6, 4, 5],
            [8, 5, 7, 9, 4, 6, 2, 1, 3],
            [5, 9, 8, 4, 1, 3, 7, 2, 6],
            [6, 2, 4, 7, 5, 9, 3, 8, 1],
            [1, 7, 3, 8, 6, 2, 5, 9, 4]
        ]

        test.assert_equals(sudoku_solver(puzzle), solution)
