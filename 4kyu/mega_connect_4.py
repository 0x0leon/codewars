import codewars_test as test

# https://www.codewars.com/kata/6250122a983b3500358fb671/train/python4


class Cell:
    def __init__(self, x, y, val) -> None:
        self.x = x
        self.y = y
        self.val = val

    def to_string(self):
        return f'x:{self.x} y:{self.y} val:{self.val}'


class MegaConnect4:

    board_size = 0
    win_condition = 0

    board = []

    def __init__(self, board_size, win_condition):
        self.board_size = board_size
        self.win_condition = win_condition
        print(board_size)
        self.board = [[Cell(x, y, 0) for x in range(self.board_size)]
                      for y in range(self.board_size)]

    def check_winning(self, x):
        print(self.board)

    def print_board(self):
        for i in self.board:
            for n in i:
                print("|", n.x, "(", n.val, ")", n.y, "|", end=" ")
            print()

    def validate_cell(self, x, y):
        if self.board_size >= x >= 0 and self.board_size >= y >= 0:
            return True
        return False

    def simulate_throw(self, col, player):
        self.board[0][col].val = player

    def add_move(self, player, col):
        # return true if this is a winning move
        self.simulate_throw(4, 1)
        self.print_board()

        print()


'''
board size M x M



'''


@test.describe("mega connect 4")
def tests():
    @test.it("x gets 3 in a column")
    def test_example_puzzle():
        game = MegaConnect4(5, 3)
        test.assert_equals(game.add_move("x", 0), False)
        test.assert_equals(game.add_move("y", 1), False)
        test.assert_equals(game.add_move("x", 2), False)
        test.assert_equals(game.add_move("x", 0), False)
        test.assert_equals(game.add_move("x", 0), True)

    @test.it("y gets 3 in a row")
    def test_example_puzzle():
        game = MegaConnect4(7, 3)
        test.assert_equals(game.add_move("x", 0), False)
        test.assert_equals(game.add_move("y", 1), False)
        test.assert_equals(game.add_move("x", 5), False)
        test.assert_equals(game.add_move("x", 0), False)
        test.assert_equals(game.add_move("x", 1), False)
        test.assert_equals(game.add_move("y", 2), False)
        test.assert_equals(game.add_move("y", 3), True)

    @test.it("no one got 4 consecutive")
    def test_example_puzzle():
        game = MegaConnect4(10, 4)
        test.assert_equals(game.add_move("x", 0), False)
        test.assert_equals(game.add_move("y", 1), False)
        test.assert_equals(game.add_move("x", 5), False)
        test.assert_equals(game.add_move("x", 0), False)
        test.assert_equals(game.add_move("x", 1), False)
        test.assert_equals(game.add_move("y", 2), False)
        test.assert_equals(game.add_move("y", 3), False)

    @test.it("x got 3 in a diagonal")
    def test_example_puzzle():
        game = MegaConnect4(5, 3)
        test.assert_equals(game.add_move("x", 0), False)
        test.assert_equals(game.add_move("y", 1), False)
        test.assert_equals(game.add_move("x", 1), False)
        test.assert_equals(game.add_move("x", 2), False)
        test.assert_equals(game.add_move("y", 2), False)
        test.assert_equals(game.add_move("x", 2), True)

    @test.it("x got 4 in a row (completed in middle)")
    def test_example_puzzle():
        game = MegaConnect4(5, 4)
        test.assert_equals(game.add_move("x", 0), False)
        test.assert_equals(game.add_move("y", 0), False)
        test.assert_equals(game.add_move("x", 2), False)
        test.assert_equals(game.add_move("x", 3), False)
        test.assert_equals(game.add_move("y", 2), False)
        test.assert_equals(game.add_move("x", 1), True)
