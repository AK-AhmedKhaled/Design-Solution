# WHAT YOU CAN DO NOW?

# Brute Force Search: human Strategy? NO
# Generating Search Space contains All possible Soutions and pich the best one by
# backtracking it through solution Tree!.
# ...  just putting the solution, you are now transformed from previous "state"
#      to the current "State" one after the solution is searched and detected

# ============================
# Data Definitions:
from examples import *
from is_valid import *  # The most complicated!!

# Val is Natural[1, 9]

# Board is a (list of (Val|False))  81 element long
# interp.
#  visually 9*9 array, each square defined by (r, c)
#  for our implementation it is a flatten array, rows layed out one after another


# Pos is Natural[0, 80]
# interp.
#  the position of the square on the Board given its position index in the flatten list:
#  the row is: p//9  'qoutient'
#  the col is: p%9   'remainder'


# Unit is a (list of Pos) of length: 9
# interp.
#  the position of every square in a unit
#  we have 27 of them: 9 rows + 9 cols + 9 squares


# convert 0_based row, col to a pos of our flatten board
def row_col_to_pos(r, c):
    return r*9+c
# ==

# Functions

# Board Pos -> Val|False
# return the value of a given position at the given Board
def read_square(board, pos):
    return board[pos]


# Board Pos Val -> Board
# return a new Updated Board in just one change: given val is assigned to the given pos
def fill_square(board, pos, val):
    newState = board[:]
    newState[pos] = val
    return newState

# ==

# Board -> Board the solution version || False is Board is unsolvable

# produce a solution -new generated board- for the given board

# ASSUMPTION: the Board is given is reasonable (valid)

# def solve_sudoku(board):
#     return False


# # Template Blending: Arbitrary-Arity-Tree and Generative Recursion and Back-Tracking Search

# def solve_sudoku(board):
#     def solve__board(board):
#         if solved(board):
#             return board
#         else:
#             return solve__lob(next_boards)
#
#     def solve__lob(lob):
#         if lob is None:
#             return False
#         else:
#             try_ =  solve__board(lob[0])
#             if try_ != False:
#                 return try
#             else:
#                 return solve__lob(lob)  # after lob.pop(0)
#
#
#    return solve__board(board)


# ========================
# ========================
# ========================
# ========================
# WISH LIST::

# !!!
# Board -> Boolean

# produce True if the givin Board is the Final Solution (Board has no Blanks)

# There is an Important Assumption givin Board is always a valid Borad

# def solved(board):
#     return False

def solved(board):
    result = True
    for i in board:
        if type(i) is not int:
            result = False
            break
    return result

# Tests
def solved_test():
    assert solved(BOARD3)     == False
    assert solved(BOARD4_SOL) == True



# ======================
# ======WISH LIST=======
# ======================
# !!!-!!!

# !!!-!!!
# Board -> Pos

# produce the first Position for a Blank square in a given Board

# def first_balnk(board):  # stub
#     return 0

def first_balnk(board, i=0):
    if len(board) == 0:
        raise Exception('Hey, How Do you get here on earth!!, Board should not branch here at all')
    elif len(board) == i:
        raise Exception('seems to be filled and at the context of program probable board such it is a solved one')
    else:
        if board[i] == False:
            return i
        else:
            return first_balnk(board, i+1)

# Tests?
def first_balnk_tests():
    assert first_balnk(BOARD1) == 0
    assert first_balnk(BOARD7) == 8
    # print(BOARD7) # is BOARD7 still not changed by first_balnk?? !!!!


# !!!-!!!
# Pos  Board -> list od Board

# produce a list of Board, lists all possibillities to move step from current state
  # ..Array of 9 Arrays: each 81 represents squares but in flattened fashion

# def fill_all_possibillities(position, board):  # stub
#     return Board1_all_possibillities

def fill_all_possibillities(position, board):
    all_possibillities = []
    def populate_board_pos(board, position, val):
        new_board = fill_square(board, position, val)
        return new_board

    for i in range(9):
        one_possible = populate_board_pos(board, position, i+1)
        all_possibillities.append(one_possible)
    return all_possibillities

# Tests?
def fill_all_possibillities_tests():
    assert fill_all_possibillities(first_balnk(BOARD1), BOARD1) == Board1_all_possibillities


# !!!-!!!
# (list of Board) -> (list of Board)

# produce a filtered version of a given possibillities to only keep solving on valid Boards

# def keep_only_valid(lob):  # stub
#     return [BOARD1, BOARD3, BOARD4]

def keep_only_valid(lob):
    return list(filter(is_valid_board, lob))
# Tests?
def keep_only_valid_tests():
    assert keep_only_valid(LOB2) == []
    assert keep_only_valid(LOB1) == LOB1_filtered

# ===========================================================================================
# !!!-!!!
# Board -> (list of Board)

# produces a list of all valid next Boards from given Board,

# How? finds the first Blank square and fill it with [1, 9], keeps only valid boards

# def next_boards(board):
#     return BOARD4_next_valid

def next_boards(board):
    return keep_only_valid(fill_all_possibillities(first_balnk(board), board))              # awesome function composition!

def next_boards_tests():
    assert next_boards(BOARD7) ==  []
    assert next_boards(BOARD4) ==  BOARD4_next_valid
    assert next_boards(BOARD1) ==  Board1_all_possibillities  # when all possibillities is valid :D
# ================================
# ================================
# ================================
# ================================

# function body
def solve_sudoku(board):

    def solve__board(board):
        if solved(board):
            return board
        else:
            return solve__lob(next_boards(board))

    def solve__lob(lob, i=0):
        if len(lob) == 0 or i == len(lob):
            return False
        else:
            try_ =  solve__board(lob[i])
            if try_ != False:
                return try_
            else:
                return solve__lob(lob, i+1)

    return solve__board(board)


def sudoku_test_cases():
    assert solve_sudoku(BOARD7) == False
    assert solve_sudoku(BOARD4) == BOARD4_SOL


# ==
if __name__ == '__main__':
    solved_test()
    first_balnk_tests()
    fill_all_possibillities_tests()
    is_valid_board_tests()
    keep_only_valid_tests()
    next_boards_tests()
    sudoku_test_cases()
    print('All Tets passed!!')
# ==
print(solve_sudoku(BOARD6))
