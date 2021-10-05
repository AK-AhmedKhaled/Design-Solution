import sys
sys.path.append('../HtDD')
from linked_list import *


# Accumulators
# 1- Classical Context preserving
# Structrual Recursion is blind and has fish memory loss all information except what on its hand.
  # such is suffiecient; for example Traversing a list of chars

# Wwhat about if we want to given a list it skips one every recursive call
# without printing; given a -> b -> c -> d -> e it prints a -> c -> e


# # Template for Accumulators
# def fn_for_lox(lox0):
#     def fn_for_lox(lox, acc):
#         if lox is None:
#             return ...acc
#         else:
#             return ...acc
#                       fn_for_X(first_X(lox))
#                       skip_one(rest_lox(lox), acc)
#     return fn_for_lox(lox0, acc)


# Trhee things to do with Accumulators:
# Accumulator has invarian: something thats always True about ccumulator
# for example, number:1 is what we initialize acc
# 1- initialize acc value < done once, by the trimpoline>
# 2- exploit the value <ask contextual question to it>
# 3- update the value  <very precise: some times you need solve Eq.>

# =====
# listof X -> listof X
# print currext X just every after n call to the recurse
def skip_n(lox0, n):
    # acc: Natural;
    # invarian!?:   max(acc) - min(acc) = n: the number of element to skip before including the next one <it is deducted>
    # ==
    # skip_n( [a -> b -> c -> d -> e -> None], 2) # outer call
    # ==
    # skip_n(  [a] -> b  -> c -> d -> e  -> None, 0)  # include
    # skip_n(        [b] -> c  -> d -> e -> None, 1)  # do NOT include
    # skip_n(             [c] -> d  -> e -> None, 2)  # do NOT include
    # skip_n(                   [d] -> e -> None, 0)  # include
    # skip_n(                        [e] -> None, 1)  # do NOT include
    # skip_n(                               None, 2)  # return None
    def skip_n(lox, acc):
        if lox is None:
            return None
        else:
            if acc == 0:
                print(first_X(lox))
            skip_n(rest_lox(lox), (acc+1)%(n+1))
    return skip_n(lox0, 0)
# ======
skip_n(lox1, 1)
skip_n(lox1, 2)
# Tests
def test_skip_n():
    assert skip_n(lox1, 0) == lox1
    assert skip_n(lox1, 1) == lox1 # a -> c -> e
    assert skip_n(lox1, 2) == lox1 # a -> d
# ==
