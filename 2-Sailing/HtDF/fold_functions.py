# (listof X) means:

# ListOfX is one of:
#     - None
#     - X -> ListOfX

# interp. List of X

# def fn_for_lox(lox):
#     if lox.head is None:
#         return ...
#     else:
#         return ...fn_for_X(lox.head)
#                   fn_for_lox(lox)   # after lox.head = lox.head.next

#NOTE#: some evluation might defrentaiate how we play with the combination:
# 1 - The order of passing the combination as arguments to the self reference recursion
# 2 - Also there are evluation must be done before updating the list not after


# Design abstract fold function for (listof X) directly from Template?
# 1- How many set of dots ... are waited for resulting in the Template? TWO
    # 1st- Base Case straightforward result?
    # 2nd- some function its result builds up with the combinations [lox.head (restof lox)]



# build up a list
class X:
    pass

node3 = X()
node3.val = 3
node3.next = None

node2 = X()
node2.val = 2
node2.next = node3

node1 = X()
node1.val = 1
node1.next = node2


class List:
    pass

list = List()
list.head = node1

# ===============================
# Build Abstract Fold function from template directly

def identity(x):
    return x

# fold abstract function for Type X: generic type
def foldX(fn ,b, x):
    if x is None:
        return b
    return fn(x.val)

# ( [] X -> X )    X   (listof X) -> [X]
# Purpose: the abstraction fold function for (listof X)
def fold(fn, b, lox):
    if lox.head is None:
        return [b]
    else:
        value = foldX(identity, b, lox.head)
        lox.head = lox.head.next
        return [fn(fold(fn, b, lox), start = value)]

# sum the list!
# print(fold(sum, 0, list)[0])
# ===============================
# multiply all the list!
# import math  # math.prod
# print(fold(math.prod, 1, list)[0])
# ===============================
# SEE? we have to be creative and create function that helps as reach
# even if it does not exist yet or prepared!
def concates(iterable, start):
    result = start
    for i in iterable:
        result = result + i
    return result

# print(fold(concates, '', list)[0])
# ===============================
# NOT PERFECT
def appendo(list, start):
    list.append(start)
    return list
# print(fold(appendo, None, list)[0])

# ===============================

# ==
# There is a MONSTER Level!!
import sys
sys.path.append('..')
from HtDD.mutual_reference.file_system_tree import *

#
# Design abstract fold function for (listof X) directly from Template?
# 1- How many set of dots ... are waited for resulting in the Template? THREE
    # 1st- fn makes its result of combinations: element.name, element.data, fn_for_ListOfElements(element.subs), call it com1
    # 2st- Base Case straightforward result!
    # 3rd- some function its result builds up with the combinations: fn_for_Element(loe.head), fn_for_ListOfElements(loe.head.next), call it com2



def combination1(n, d, los):
    los.append(n)
    return los
# combination1('ahmed', 1, additional_names).listprint()

def combination2(los1, los2):
    return ListOfStrings.mergeLists(los1, los2)
# combination2(combination1('ahmed', 1, additional_names), list_all_names).listprint()

# ingenuity of inference Types at signature!!
# ( String Integer Y -> X ) ( X Y -> Y ) Y Element -> X
# purpose: Abstract Fold function that operate on mutual-recursive Data Structures
def fold(com1, com2, b, element):
    def fn_for__Element(element):     # -> X
         return com1(element.name,
                     element.data,
                     fn_for__ListOfElements(element.subs))
    def fn_for__ListOfElements(loe):  # -> Y
        if loe.head is None:
            return b
        else:
            val = fn_for__Element(loe.head)
            loe.head = loe.head.next
            return com2(val,
                        fn_for__ListOfElements(loe))
    return fn_for__Element(element)

fold(combination1, combination2, ListOfStrings(), f1).listprint()  #correct!
fold(combination1, combination2, ListOfStrings(), D4).listprint()  # inf. loop!
