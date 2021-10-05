### Problem HtDD- Large Enumeration:
# assume  function for a text editor program respnsonds to a key presses,
# each letter printable like, QWERTY..., it returns, but the response is different
# when it comes to spaces key [space, tab] return space, arrow keys move the cursor
# and functional keys [no response], finally ENTER_KEY break the line


# WRITE THIS PARAGRAPH:
# ---------
# Ahmed
# Loves Monkeies
# study Computer Science
# programs very nicely


# 1- no Possible Structrue for KeyPressed
# KeyPressed is one of:                         # 2- Type Comment
#     - atomic distinct: int ENTER_KEY (ASCII: 13)
#     - atomic distinct: int BACK_SPACE (ASCII: 8)
#     - atomic distinct: int SPACE (ASCII: 32)
#     - atomic non-distinct: adjoining Intervals, Interval ints [65, 90]  # Printable CAPITALS && Interval ints [97, 122]  # Printable smalls
#     - atomic non-distinct: Other Keys: adjoining Intervals < No resonse for any other keys for simplicity! >

# 3- Interpretation: each key pressed we extract its ASCII code and execute its functionality
# /*
# There is a masking layer ord() on every input key press from user : ord(input())
# */

# 4- Data Examples: is kind of redundancy
# key1st_hit = ord('A')
# key2st_hit = ord('h')
# key3st_hit = ord('n')
# key4st_hit = 8                  # BACK_SPACE
# key4st_hit = ord('m')
# key4st_hit = ord('e')
# key4st_hit = ord('d')
# key4st_hit = 13                # ENTER_KEY

# Some Constants:
ENTER_KEY  = 13
BACK_SPACE = 8
SPACE = 32



# 5- Data Driven Template
# def fn_for_KeyPressed (ord(k)):
#     if (k == ENTER_KEY):
#         (...)
#     elif (k == SPACE):
#         (...)
#     elif (k == BACK_SPACE):
#         (...)
#     elif (k >= 65 && k <= 90 && k >= 97 && k <= 122):
#         (...k)
#     else:
#         (...k)
