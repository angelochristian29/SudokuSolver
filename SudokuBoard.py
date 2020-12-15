class SudokuBoard:

    def __init__(self, base):
        self.base = base
        self.side = base*base
        self.s_board = [[]]

    def sudoku_maker(self):
        def sol_pattern(r, c): return (self.base * (r % self.base) + r // self.base + c) % self.side

        from random import sample
        def rand(s): return sample(s, len(s))

        r_base = range(self.base)
        rows = [g * self.base + r for g in rand(r_base) for r in rand(r_base)]
        columns = [g * self.base + c for g in rand(r_base) for c in rand(r_base)]
        nums = rand(range(1, self.side + 1))
        board = [[nums[sol_pattern(r, c)] for c in columns] for r in rows]
        # Process of creating blank spaces in board
        squares = self.side * self.side
        blanks = squares * 3 // 4
        for p in sample(range(squares), blanks):
            board[p // self.side][p % self.side] = 0
        return board

    def isPresent(self, board, r, c, num):
        for i in range(self.side):
            if board[r][i] == num:
                return False
        for i in range(self.side):
            if board[i][c] == num:
                return False
        row = r - (r % self.base)
        column = c - (c % self.base)
        for i in range(row, row + self.base):
            for j in range(column, column + self.base):
                if board[i][j] == num:
                    return False
        return True
    def puzzle_solver(self, board, r, c):
        if r > self.side - 1:
            return True
        if board[r][c] != 0:
            if c == self.side - 1:
                itr = self.puzzle_solver(board, r + 1, 0)
            else:
                itr = self.puzzle_solver(board, r, c + 1)
            return itr
        else:
            for i in range(1, self.side + 1):
                if self.isPresent(board, r, c, i):
                    board[r][c] = i
                    if c == self.side - 1:
                        itr = self.puzzle_solver(board, r + 1, 0)
                    else:
                        itr = self.puzzle_solver(board, r, c + 1)
                    if itr is True:
                        return True
            board[r][c] = 0
            return False
    def start_sol(self, board):
        return self.puzzle_solver(board, 0, 0)

    def board_printer(self, board):
        for line in board:
            print(line)

mySudoku = SudokuBoard(3)
mySudoku.s_board = mySudoku.sudoku_maker()
mySudoku.board_printer(mySudoku.s_board)
print("")
mySudoku.start_sol(mySudoku.s_board)
mySudoku.board_printer(mySudoku.s_board)
