from examples import *
# Constants:
ALL_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# positions of all units
ROWS =     [[0,  1,  2,  3,  4,  5,  6,  7,   8],
            [9, 10, 11, 12, 13, 14, 15, 16,  17],
            [18, 19, 20, 21, 22, 23, 24, 25, 26],
            [27, 28, 29, 30, 31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40, 41, 42, 43, 44],
            [45, 46, 47, 48, 49, 50, 51, 52, 53],
            [54, 55, 56, 57, 58, 59, 60, 61, 62],
            [63, 64, 65, 66, 67, 68, 69, 70, 71],
            [72, 73, 74, 75, 76, 77, 78, 79, 80]]

COLS =     [[0,  9, 18, 27, 36, 45, 54, 63, 72],
            [1, 10, 19, 28, 37, 46, 55, 64, 73],
            [2, 11, 20, 29, 38, 47, 56, 65, 74],
            [3, 12, 21, 30, 39, 48, 57, 66, 75],
            [4, 13, 22, 31, 40, 49, 58, 67, 76],
            [5, 14, 23, 32, 41, 50, 59, 68, 77],
            [6, 15, 24, 33, 42, 51, 60, 69, 78],
            [7, 16, 25, 34, 43, 52, 61, 70, 79],
            [8, 17, 26, 35, 44, 53, 62, 71, 80]]

SQUARES=   [[ 0,  1,  2,  9, 10, 11, 18, 19, 20],
            [ 3,  4,  5, 12, 13, 14, 21, 22, 23],
            [ 6,  7,  8, 15, 16, 17, 24, 25, 26],
            [27, 28, 29, 36, 37, 38, 45, 46, 47],
            [30, 31, 32, 39, 40, 41, 48, 49, 50],
            [33, 34, 35, 42, 43, 44, 51, 52, 53],
            [54, 55, 56, 63, 64, 65, 72, 73, 74],
            [57, 58, 59, 66, 67, 68, 75, 76, 77],
            [60, 61, 62, 69, 70, 71, 78, 79, 80]]

UNITS = ROWS + COLS + SQUARES
# print(UNITS)
# ==


# !!!-!!!-!!!
# Board -> Boolean

# produce True if NO UNIT on the Board has same Val twice, otherwise False

# def is_valid(board):  # stub
#     return False


def is_valid_board(board):

    def validate_units(UNITS, i=0):
        if i == 27:
            return True
        else:
            result = no_duplicates(keep_only_values(grap_values(UNITS[i], board)))
            return result and validate_units(UNITS, i+1)  # short-circuit saves performance here

    def grap_values(unit, board):
        vf_list = []
        for i in unit:
            vf_list.append(board[i])
        return vf_list

    def keep_only_values(lovf):
        filtered = list(filter(lambda x: x != False, lovf))
        return filtered

    def no_duplicates(lov):
        return len(set(lov)) == len(lov)

    return validate_units(UNITS)

# Tests?
def is_valid_board_tests():
    assert is_valid_board(BOARD1)  == True
    assert is_valid_board(BOARD4)  == True
    assert is_valid_board(BOARD8)  == False
    assert is_valid_board(BOARD9)  == False
    assert is_valid_board(BOARD10) == False
