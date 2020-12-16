from SudokuSolver.SudokuBoard import SudokuBoard
import sys, pygame as pg
import time

pg.init()
font = pg.font.SysFont(None, 60)
mySudoku = SudokuBoard()
mySudoku.s_board = mySudoku.sudoku_maker()

class SudokuGUI:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw_canvas(self):
        self.canvas.fill(pg.Color("white"))
        pg.draw.rect(self.canvas, pg.Color("black"), pg.Rect(10, 10, 630, 630), 10)
        i = 1
        while i * 70 < 630:
            line_width = 3 if i % 3 > 0 else 8
            pg.draw.line(self.canvas, pg.Color("black"), pg.Vector2((i * 70) + 10, 10), pg.Vector2((i * 70) + 10, 640), line_width)
            pg.draw.line(self.canvas, pg.Color("black"), pg.Vector2(10, (i * 70) + 10), pg.Vector2(640, (i * 70) + 10), line_width)
            i += 1

    def draw_nums(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] != 0:
                    n_text = font.render(str(board[r][c]), True, pg.Color("black"))
                    self.canvas.blit(n_text, pg.Vector2((c * 70) + 33.5, (r * 70) + 27.5)) # modify this for sketching feature
    def solve_draw(self, board, r, c, tof=True):
        pg.draw.rect(self.canvas, pg.Color("white"), pg.Rect(c * 70 + 13.5, r * 70 + 13, 67.5, 67.5), 0)
        n_text = font.render(str(board[r][c]), True, pg.Color("black"))
        self.canvas.blit(n_text, pg.Vector2((c * 70) + 33.5, (r * 70) + 27.5))
        if tof:
            pg.draw.rect(self.canvas, pg.Color("orange"), pg.Rect(c * 70 + 13.5, r * 70 + 12, 67.5, 67.5), 3)
        else:
            pg.draw.rect(self.canvas, pg.Color("blue"), pg.Rect(c * 70 + 13.5, r * 70 + 12, 67.5, 67.5), 3)
    def backtracking_solver(self, board, r, c):
        if r > mySudoku.side - 1:
            return True
        if board[r][c] != 0:
            if c == mySudoku.side - 1:
                itr = self.backtracking_solver(board, r + 1, 0)
            else:
                itr = self.backtracking_solver(board, r, c + 1)
            return itr
        else:
            for i in range(1, mySudoku.side + 1):
                if mySudoku.is_present(board, r, c, i):
                    board[r][c] = i
                    self.solve_draw(board, r, c, True)
                    pg.display.flip()
                    pg.time.delay(50)
                    if c == mySudoku.side - 1:
                        itr = self.backtracking_solver(board, r + 1, 0)
                    else:
                        itr = self.backtracking_solver(board, r, c + 1)
                    if itr is True:
                        return True
            board[r][c] = 0
            self.solve_draw(board, r, c, False)
            pg.display.flip()
            pg.time.delay(50)
            return False

    def start_sol(self, board):
        return self.backtracking_solver(board, 0, 0)

# main
def sudoku_loop():
    canvas_size = 650, 750
    canvas = pg.display.set_mode(canvas_size)
    pg.display.set_caption("Sudoku Solver")
    to_run = True
    myGUI = SudokuGUI(canvas)
    print("run")
    while to_run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                to_run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    myGUI.start_sol(mySudoku.s_board)
        myGUI.draw_canvas()
        myGUI.draw_nums(mySudoku.s_board)
        pg.display.flip()


sudoku_loop()
