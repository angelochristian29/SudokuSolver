def sudoku(base_num):
    base = base_num
    side = base * base

    def sol_pattern(r, c): return (base * (r % base) + r // base + c) % side

    from random import sample
    def rand(s): return sample(s, len(s))

    r_base = range(base)
    rows = [g * base + r for g in rand(r_base) for r in rand(r_base)]
    columns = [g * base + c for g in rand(r_base) for c in rand(r_base)]
    nums = rand(range(1, base * base + 1))
    board = [[nums[sol_pattern(r, c)] for c in columns] for r in rows]
    # Process of creating blank spaces in board
    squares = side * side
    blanks = squares * 3 // 4
    for p in sample(range(squares), blanks):
        board[p // side][p % side] = 0
    nums_size = len(str(side))
    for line in board:
        print("[" + " ".join(f"{n or '.':{nums_size}}" for n in line) + "]")


class SudokuBoard(object):
    pass


sudoku(3)
