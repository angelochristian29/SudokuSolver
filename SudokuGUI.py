from SudokuSolver.SudokuBoard import SudokuBoard
import sys, pygame as pg

pg.init()
screen_size = 650, 650
screen = pg.display.set_mode(screen_size)
mySudoku = SudokuBoard(3)
mySudoku.s_board = mySudoku.sudoku_maker()
font = pg.font.SysFont(None, 60)

def draw_canvas():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(10,10, 630, 630), 10)
    for i in range(630):
        line_width = 3 if i % 3 > 0 else 8
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * 70) + 10, 10), pg.Vector2((i * 70) + 10, 640), line_width)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(10, (i * 70) + 10), pg.Vector2(640, (i * 70) + 10), line_width)

def draw_numbers():
    for r in range(9):
        for c in range(9):
            output = mySudoku.s_board[r][c]
            n_text = font.render(str(output), True, pg.Color("black"))
            screen.blit(n_text, pg.Vector2((c * 70) + 33.5, (r * 70) + 27.5)) # modify this for sketching feature

def sudoku_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    draw_canvas()
    draw_numbers()
    pg.display.flip()
while 1:
    sudoku_loop()
