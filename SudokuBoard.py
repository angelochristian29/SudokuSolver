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
            board[p // self.side][p % self.side] = ' '
        return board

    def is_present(self, board, r, c, num):
        for i in range(self.side):
            if board[r][i] == num:
                return False
        for i in range(self.side):
            if board[i][c] == num:
                return False
        box_row = r - (r % self.base)
        box_column = c - (c % self.base)
        for i in range(box_row, box_row + self.base):
            for j in range(box_column, box_column + self.base):
                if board[i][j] == num:
                    return False
        return True

    def backtracking_solver(self, board, r, c):
        if r > self.side - 1:
            return True
        if board[r][c] != ' ':
            if c == self.side - 1:
                itr = self.backtracking_solver(board, r + 1, 0)
            else:
                itr = self.backtracking_solver(board, r, c + 1)
            return itr
        else:
            for i in range(1, self.side + 1):
                if self.is_present(board, r, c, i):
                    board[r][c] = i
                    if c == self.side - 1:
                        itr = self.backtracking_solver(board, r + 1, 0)
                    else:
                        itr = self.backtracking_solver(board, r, c + 1)
                    if itr is True:
                        return True
            board[r][c] = ' '
            return False
    def start_sol(self, board):
        return self.backtracking_solver(board, 0, 0)

    def board_printer(self, board):
        for line in board:
            print(line)


