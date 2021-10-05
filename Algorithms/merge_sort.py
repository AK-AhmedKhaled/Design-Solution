import sys
sys.path.append('../3-Diving/HtDD')
from generic_list_last_try import *


# Merge Sort  # Generative Recursion  # O(nlog2n) # Systymatic Design

# (listof Number) -> (listof Numbers)
# produces a sorted version of a given list in ascending order using Merge Sort

lon1 = LOX(X(1))
apppend(lon1, 2)
apppend(lon1, 3)
# print_Xs(lon1)
# ==================
lon2 = LOX(X(4))
apppend(lon2, 5)
# print_Xs(lon2)
# ==================
lon  = LOX(X(1))
apppend(lon, 2)
apppend(lon, 3)
apppend(lon, 4)
apppend(lon, 5)
# print_Xs(lon)

# Template for Generative Recursion
# def generec(lon):
#     if trivial(lon):
#         return trivial_answer(lon)
#     else:
#         return ...lon
#                   generec(next_problem(lon))



# ======================
# ======================
# =======WISHLIST=======
# ======================
# ======================
# !!!
# (listof Numbers) (listof Numbers) -> (listof Numbers)
# produces a product of a sorted list of all elements of given two lists

# Two one-of cross produt table
#              lon1        None   (Number (listof Number))
#  lon2

#  None                     lon2        lon2

# (Number (listof Number))  lon1      <smaller of the two candidates> (listof Number)


def merge(lon1, lon2):
    # sorted<(listof Number)> result so far accumulator
    def merge(lon1, lon2, sorted):
        print_Xs(sorted)
        if lon1.head is None:
            return lon2
        elif lon2.head is None:
            return lon1
        else:
            if first_X(lon1).value <= first_X(lon2).value:
                apppend(sorted, first_X(lon1).value)
                return append_lox(sorted, merge(rest_Xs(lon1), lon2, sorted))
            else:
                apppend(sorted, first_X(lon2).value)
                return append_lox(sorted, merge(lon1, rest_Xs(lon2), sorted))
    return merge(lon1, lon2, LOX())
# print_Xs(merge(lon1, lon2))


def merge_test():
    assert equals_X_by_X(merge(lon1, lon2),  lon)
    assert equals_X_by_X(merge(lon1, LOX()), lon1)
    assert equals_X_by_X(merge(LOX(), lon2), lon2)
# =================
def merge_sort(lon):
    def trivial(lon):
        return lon.head is None or lon.head.next is None
    def trivial_answer(lon):
        return lon

    if trivial(lon):
        return trivial_answer(lon)
    else:
        return merge(
                  merge_sort(take(lon, how_many)),
                  merge_sort(drop(lon, how_many)))
# ===
if __name__=='__main__':
    # merge_test()
    print('All Tests passed!')
