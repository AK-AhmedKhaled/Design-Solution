# TAIL RECURSION
# TO AVOID BUILDING UP CONTEXT OF PENDING COMPUTATIONS: TAIL POSITION.
# ==
import sys
sys.path.append('../HtDD')
from linked_list import *
# RECURSE && MUTUAL RECURSE

# DESIGN: a function consumes a list and produces the sum of all its elements
#         then make a tail-recursive version of it

# listof Number -> Number
# consumes a list and produces the sum of all its elements
def sum_list(lon):
    if lon is None:
        return 0
    else:
        return first_X(lon) + sum_list(rest_lox(lon))  # 15
# 0 and the '+' sign is only addition to the Template on our mind!

# Tests
# print(sum_list(lox2))
# ==
# when listof Number gets longer,
# pending computation (set of {a + b + c + .. + 0}) gets longer


# programming Languages implementation,
# cosumes specific expensive and limited part of computer memory 'Stack'
# to store and save the context of pending computation

# But what can we do in order to help programming Languages
# NOT to use Stack proportionally with long lists!?



# CONCEPT: Tail Position
# whenever an EXPRESSION in a position
# where its result is the result for the enclosing function, is in TAIL POSITION

# at Example niether first_X(lon) nor sum_list(rest_lox(lon)) is in tail position.
# why? simply after evaluation each does not produce the answer to the enclosing function.
# INSTEAD, the Primitive Operation '+' is in tail position!

# what causes our problem (growing build up of pending pluses)?
# there is a recursive call sum_list(rest_lox(lon)) is NOT in TAIL POSITION,
# the plus is WAITING for it.

# pluses are not going happen in the return
# pluses are     going happen in the way in


# Template
# def sum_list_optimized(lon0):
#     def sum_list_optimized(lon, acc):
#         if lon is None:
#             return ...acc
#         else:
#             return ...acc
#                       first_X(lon)
#                       sum_list_optimized(rest_lox(lon), acc)
#     return sum_list_optimized(lon0, ...)


#
def sum_list_optimized(lon0):
    # acc: Ntural; keeps the sum untill the end
    # spread a little and detect the invarient "True pattern"

    # invarient? starts from 0 ,it is sum of elements seen so far
    # we increment acc with the current val first_X(lon),
    # and when rest_lox(lon) is None ,return what you end up with

    # sum_list_optimized(1 -> 2 -> 3 -> 4 -> 5)  # outer call
    #
    # sum_list_optimized(1 -> 2 -> 3 -> 4 -> 5,  0)
    # sum_list_optimized(     2 -> 3 -> 4 -> 5,  1)
    # sum_list_optimized(          3 -> 4 -> 5,  3)
    # sum_list_optimized(               4 -> 5,  6)
    # sum_list_optimized(                    5, 10)
    # sum_list_optimized(                     , 15) # quik returns without waiting sums bit by bit!

    def sum_list_optimized(lon, acc):
        if lon is None:
            return acc
        else:
            return sum_list_optimized(rest_lox(lon), acc+first_X(lon))
    return sum_list_optimized(lon0, 0)
# Tests
print(sum_list_optimized(lox2)) # 15



# ==
