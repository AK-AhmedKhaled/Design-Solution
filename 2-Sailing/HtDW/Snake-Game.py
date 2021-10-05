# PROBLEM : How to Design World: after Analysis, Design a Snake Game !!
# focus on arbitrary sized data
# Run Early , Run Often :)
import random
import curses

screen = curses.initscr()
curses.curs_set(0)
SCREEN_HIEGHT, SCREEN_WIDTH = screen.getmaxyx()

# 1- define SnakeUnit Structure
class SnakeUnit(object):
    """docstring for Snake."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None             # reference to a SnakeUnit
# 2- SnakeUnit is SnakeUnit(x, y)
# 3- INTERPRETATION: current position of a one  unit of a Snake on Screen, by default SnakeUnit() or SnakeUnit(SCREEN_WIDTH, SCREEN_HIEGHT)


initx = SCREEN_WIDTH // 4
inity = SCREEN_HIEGHT // 2

# 3- Data Examples: each unit should have a unique x, y position
initsnakeunit = SnakeUnit(initx, inity)
# // Horizontal Extensions
snakeunit2 = SnakeUnit(initx - 1, inity)
snakeunit3 = SnakeUnit(initx - 2, inity)

# # 4- Data Driven Template
# def fn_for_SnakeUnit(snakeunit):
#     return (...snakeunit.x snakeunit.y)
# Template Rules used:
    # - compound Data: 2 fields


# 1- define Snake(ListOfSnakeUnit(s))
class Snake:
    def __init__(self):
        self.head = None   # pointer for a SnakeUnit, None means empty list
    def listprint(self):  # for Testing
      unit = self.head
      while unit is not None:
         print(unit.x, unit.y)
         unit = unit.next

# 2- Snake is one-of:
    # - empty(None) : There is No Case for such Snake!!
    # - SnakeUnit -> Snake(ListOfSnakeUnit)

# 3- INTERPRETATION: Snake is a series of SnakeUnit(s) form the snake on the screen,
#    each SnakeUnit is unique in its coordinates but it must be sequenced!

# 4- Data Examples

# snake1
snake1 = Snake()
snake1.head = initsnakeunit
snake1.head.next = snakeunit2
snakeunit2.next = snakeunit3


# Instead of this Implementation:
# snake1 = [initsnakeunit, snakeunit2, snakeunit2]

# # 4- Data Driven Template
# /*
# Care about function needs to travese the linked list, head pointer must be unchangable! use virtual head (temp)
# even with that (temp) has the ability to change connections over the list TAKE CARE of what you want.
# */
# def fn_for_Snake(snake): # Snake or Snake.head ?? مهم
#     # remember Snake is ListOfSnakeUnit
#     if (snake.head == None ):  #empty?
#         (...)
#     else:
#         (... fn_for_SnakeUnit(snake.head)
#              fn_for_Snake(less_snake)    less-\ version of Snake(ListOfSnakeUnit(s)) or Infinite loop!!?
#         )
# ;; Template Rules Used:
# ;    one of: 2 cases
# ;       - atomic distict: empty
# ;       - compound: 2 fields:
                # - Type Reference: SnakeUnit
                # - Self-reference: (Snake) is ListOfSnakeUnit :wrap this seletor to the call of the Template Function itself

######################
# /* WISH LIST: */
######################
# SnakeUnit -> bool
# Purpose: takes a SnakeUnit then return True if there is a next SnakeUnit
# fun body:
def nextexist(snakeunit):
    if snakeunit.next is None:
        return False
    else:
        return True
# ======================================
# SnakeUnit , int, int -> bool
# purpse: check if SnakeUnit.x and SnakeUnit.y is  different from x ,y in pairs so all is well and return True
# Fun Body:
def differentpositions(snakeunit, x, y):
    if (snakeunit.x == x and snakeunit.y == y):
        return False
    else:
        return True
# =======================================
# SnakeUnit, SnakeUnit -> bool   # signature
# Purpose: return True if The Corrdinates of the Two Units x, and y are the same else False
def iscollapse(snakeunit, x, y):
    if (snakeunit.x == x and snakeunit.y == y):
        return True
    else:
        return False

# =============================================================
##############################
# /* Main Functionality: */
##############################
# a reference to SnakeUnit, Special reference to SnakeUnit (play the role of the head)-> SnakeUnit  # 1- signature
# /* NOTE
# after long Thinking.. No need to Pass actual list (that just have head address) and pass the address to a virtual reference
# why? to safely preserve the original head address it is unmutable unless the list will lost.
# Ques? Is there a CASE in which we MUST provide teh Original List ? remember Linked list is merely an address (original address)
# to the FIRST block(unit) of the list
# */
# 2- Purpose: consumes a Snake(ListOfSnakeUnit(s)) and go forward untill end unit (tail) ,then return it after get rid of it!
# # 3- stub
# def getTail_eraseTail(prev, curr):
#     return snakeunit3
# 5- body:
def getTail_eraseTail(prev, curr):
    if (curr is None):
        return None
    else:
        if (not nextexist(curr)):
            tail = curr
            prev.next = None
            return tail
        else:
            prev = curr
            curr = curr.next                   # Do Not play with head now!
            return getTail_eraseTail(prev, curr)
# # 4- UnitTests and Examples:
# def test_case_one_getTail():
#     assert getTail_eraseTail(None, snake1.head) == snakeunit3
# if __name__=="__main__":
#     test_case_one_getTail()
#     print('All Tests Passed!, we got the tail Recursivilly')

# # 6- Testing and debugging:
# print('before deletion List')
# snake1.listprint()
# tail = getTail_eraseTail(None, snake1.head)
# print('-----------------')
# print('after deletion List')
# snake1.listprint()
# print('-----------------')
# print('tail info : ',tail.x, tail.y)
# =======================================================================
# 1-signature Snake, SnakeUnit -> Snake  # signature
# /*
# That is the CASE you MUST pass the ORIGINAL list (address), so we want to change it to becomes new original
# */
# 2- Purpose: link SnakeUnit as a head of the passed snake(ListOfSnakeUnits)
# # 3- stub
# def linknewhead(snake, snakeunit):
#     return snake

# # 4- UnitTests and Examples:
# def test_case_one_newhead():
#     newhead = SnakeUnit(20, 10)
#     linknewhead(snake1, newhead)
# if __name__ == "__main__":
#     test_case_one_newhead()
#     print('All Tests passed!')

# 5- body: Template is copied from ????? Data Definition
def linknewhead(snake, unit):
    if (unit is None):
        raise Exception('new Head Unit is None!')
    else:
        if (snake.head == None ):  #empty?
            snake.head = unit
        else:
            unit.next  = snake.head
            snake.head = unit
# 6- Testing and Debugging:

# ===========================================================
# temp, int, int -> bool    # 1- signature
# 2- Purpose: Takes a Snake(ListOfSnakeUnit(s)) and, a Tow ints represents food (x, y) position in respect and it returns true:
#          wether those x and y values are Not unique (does exists on any one pairs all over the list), so food is apear in frott of snake

# /*
# # most important thing Do Not Play on snake argument head pointer (so why we need it then? a copy of the head address is sufficient)
# # ,you have a temp a 'virtual head that can move'!
# */

# # 3- stub
# def food_collapse_snake(temp, x, y):
#     return False

# 5- function body, template is used from Snake Data Definition
def food_collapse_snake(temp, x, y):
    if (temp == None ):
        return False
    else:
        if (not differentpositions(temp, x, y)):
            return True
        else:
            temp = temp.next
            return food_collapse_snake(temp, x, y)

# # 4- UnitTests and Examples:
# def test_case_one_food_collapse_snake():
#     assert food_collapse_snake(snake1.head, snake1.head.x, snake1.head.y) == True
# def test_case_two_food_collapse_snake():
#     assert food_collapse_snake(snake1.head, 40, 25) == False
# if __name__=="__main__":
#     test_case_one_food_collapse_snake()
#     test_case_two_food_collapse_snake()
#     print('All Tests passed!')
# =====================================================================
# reference to SnakeUnit, int, int -> bool     # 1- signature
# 2- Purpose: Consumes a reference to non-head SnakeUnit: The first after The head unit, so:
        # - Snake original address left so, preserves its value unless the list will lost!,  snake1.head = snake1.head.next
#    and the current head coordinates x, y and checks over the Snake(ListOfSnakeUnit(s)) unless current head,
#    if the current SnakeUnit Head becomes not unique: at the same x, y Positions on the Screen then return true

# # 3- stub
# def head_collapsed(nextafterhead, x, y):
#     return False                         # if head is collapsed the False will not over the Game

# 5- Function Body: Template used from snake Data Definition
def head_collapsed(temp, x, y):
    if (temp == None):
        return False
    else:
        if iscollapse(temp, x, y):
            return True
        else:
            temp = temp.next
            return head_collapsed(temp, x, y)    # less-snake(ListOfSnakeUnit(s)) !!?

# # 4- Examles and Unit Tests:
# def test_case_one_head_collapsed():
#     assert head_collapsed(snake1.head.next, snake1.head.next.x, snake1.head.next.y) == True
# def test_case_two_head_collapsed():
#     assert head_collapsed(snake1.head.next, snake1.head.x, snake1.head.y) == False
# if __name__ == "__main__":
#     test_case_one_head_collapsed()
#     test_case_two_head_collapsed()
#     print('All Tests Passed!')

# 6- Test and  Debugging untill Correct:
# ==============================================================================
# 1- Possible structure
class Food(object):
    """docstring for Food."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
# 2- Type Comment
# Food is Food(int, int)

# 3-INTERPRETATION: Two Integers (x, y) in respect to represent the Food Position on Screen

init_x_pos = SCREEN_WIDTH // 2
init_y_pos = SCREEN_HIEGHT // 2
# print('init_x_pos',init_x_pos, 'init_y_pos',init_y_pos)
# 4- Data Examples:
currentFood = Food(init_x_pos, init_y_pos)

# # 5- Data Driven Template
# def fn_for_Food(food):
#     return (... food.x
#                 food.y
#            )
# Template Rules used:
    # - compound: 2 fields
# =============================================================
# Food -> Food   # 1- signature
# 2- Purpose: consume Food and return it at a random Position on a Screen
# # 3- stub
# def generate_food(food):
#     return Food(1, 1)    # most top left

# # 4- Examples and Unit Tests:
# def test_case_one():
#     assert generate_food() not in []
# if __name__ == "__main__":
#     test_case_one()
#     print('All tests passed!')

# # function body: Template is copied from Food Data Template
def generate_food():
    x = random.randint(1, SCREEN_WIDTH-1)    # 0, and SCREEN_WIDTH are borders!
    y = random.randint(1, SCREEN_HIEGHT-1)
    food = Food(x, y)
    return food
# 6- Debugging and Testing:
# ====================================================================
# THE PROGRAM MAIN LOGIC:

window = curses.newwin(SCREEN_HIEGHT, SCREEN_WIDTH, 0, 0)
window.keypad(True)
window.timeout(100)
window.addch(currentFood.y, currentFood.x, curses.ACS_PI)
currentkey = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    currentkey = currentkey if next_key == -1 else next_key
    if snake1.head.x in [0, SCREEN_WIDTH] or snake1.head.y in [0, SCREEN_HIEGHT] or  head_collapsed(snake1.head.next, snake1.head.x, snake1.head.y):
        curses.endwin()
        quit()
    new_head = SnakeUnit(snake1.head.x, snake1.head.y)
    if currentkey == curses.KEY_DOWN:
        new_head.y += 1
    if currentkey == curses.KEY_UP:
        new_head.y -= 1
    if currentkey == curses.KEY_RIGHT:
        new_head.x += 1
    if currentkey == curses.KEY_LEFT:
        new_head.x -= 1
    linknewhead(snake1, new_head)                                      # Inserting at Begging O(1)! Awesome, if list inserting at 0 is Worst Case!
    if [snake1.head.x, snake1.head.y] == [currentFood.x, currentFood.y]:
        currentFood = None
        while currentFood is None:
            newfood = generate_food()
            currentFood = newfood if (not food_collapse_snake(snake1.head, newfood.x, newfood.y)) else None
        window.addch(currentFood.y, currentFood.x, curses.ACS_PI)
    else:
        tail = getTail_eraseTail(None, snake1.head)
        window.addch(tail.y, tail.x, ' ')
    window.addch(snake1.head.y, snake1.head.x, curses.ACS_CKBOARD) # ACS_BULLET
