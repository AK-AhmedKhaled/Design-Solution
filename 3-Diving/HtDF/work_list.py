import sys
sys.path.append('../HtDD')
from family_tree import *
from linked_list import *

# Descendant family Tree

# Design a function consumes a Wizard and produces the name of every wizard
# in the tree that was placed in the same house as their immediate parent.

# Wizard -> (Listof String)
# purpose: consumes a wizard and produces the name of every wizard
#          in the tree that was placed in the same house as their immediate parent

# def same_house_as_parent(root):  # stub
#     return None

# Template copied from family tree with Accumulator version
def same_house_as_parent(wizard):
    # acc<parent_house>: String
    # invarian? keeps current wizard s parent str value ('': for given root)

    # Progression Examples
    # fn_for_wiz(wk, '')  # outer call
    #
    # fn_for_wiz(wk, '')
    # fn_for_wiz(wh 'G')
    # fn_for_wiz(wc 'S')
    # fn_for_wiz(wd 'S')
    # fn_for_wiz(wh 'G')
    # fn_for_wiz(wi 'G')
    # fn_for_wiz(wj 'G')
    # fn_for_wiz(we 'R')
    # fn_for_wiz(wf 'R')
    # fn_for_wiz(wb 'R')
    # fn_for_wiz(wg 'R')
    # fn_for_wiz(wa 'S')
    def fn_for_wiz(wizard, parent_house, names_list):
        if wizard.house == parent_house:
            names_list.append(wizard.name)
        fn_for_low(wizard.children, wizard.house, names_list)
        return names_list

    def fn_for_low(low, parent_house, names_list):
        if low is None:
            return []
        else:
            return fn_for_wiz(first_Wiz(low) , parent_house, names_list) + fn_for_low(rest_Wiz(low), parent_house, names_list)
    return fn_for_wiz(wizard, '', [])
# same_house_as_parent(wk)


def same_house_as_parent_test():
    assert same_house_as_parent(wa) == []
    assert same_house_as_parent(wh) == []
    assert same_house_as_parent(wg) == ['A']
    assert same_house_as_parent(wk) == ['E', 'F', 'A']
# =============================================================
# Wizard -> Natural
# produce the count of wizards on a tree givin wiazard as root
# def count_wizards():  # stub
#     return 0

# # Template: mutual reference
def count_wizards(wizard):
    # acc: result; Natural
    # invar. number of wizards seen so far
    # progg. Exs.
    # fn_for_wiz(wk, 0) # outer call
    #
    # fn_for_wiz(wk, 0)
    # fn_for_wiz(wh, 1)
    # fn_for_wiz(wc, 2)
    # fn_for_wiz(wd, 3)
    # fn_for_wiz(wi, 4)
    # ...
    def fn_for_wiz(wizard):
        return 1 + fn_for_low(wizard.children)
    def fn_for_low(low):
        if low is None:
            return 0
        else:
            return fn_for_wiz(first_Wiz(low)) + fn_for_low(rest_Wiz(low))
    return fn_for_wiz(wizard)
# ===============================================
def count_wizards_tests():
    assert count_wizards(wc) == 1
    assert count_wizards(wh) == 3
    assert count_wizards(wk) == 11
# ===
# CAN ANY ONE SOLVE COUNT BY LOSS CONTEXT Accumulator ?? I TRIED AND I FAILED!
# ===
# WorkList Accumulator

# Our Main CASE is:
    # - to make all recursive calls in tail position in both mutual recursive functions
    # - traverse the Tree pass on a node once!! [either depth or breadth order traversing]

# Wizard -> Natural
# produce the count of wizards on a tree givin wiazard as root
# def count_depth(wizard):  # stub
#     return 0

# # Template: mutual reference
def count_depth(wizard):
    # acc1: result; Natural
    # invar. number of wizards seen so far
    # acc2: togo (Listof Wizard)
    # invar. list of Wizards still to visit, (it is updated by evey wizard)
    # progg. Exs.
    # fn_for_wiz(wk, 0) # outer call
    #
    # fn_for_wiz(wk, 0)
    # fn_for_wiz(wh, 1)
    # fn_for_wiz(wc, 2)
    # fn_for_wiz(wd, 3)
    # fn_for_wiz(wi, 4)
    # ...
    def fn_for_wiz(wizard, togo, result):
        return fn_for_low(append_two_lowizes(wizard.children ,togo), result+1)
    def fn_for_low(togo):
        if low is None:
            return 0
        else:
            return fn_for_wiz(first_Wiz(togo), rest_Wiz(low),  result)
    return fn_for_wiz(wizard, None, 0)

# (wizard.children ,togo) small change: swap (togo, wizard.children)
# causes differen Traverse <breadth order traverse>! DOES IT MAKE SENSE?

def count_depth_test():
    assert count_wizards(wc) == 1
    assert count_wizards(wh) == 3
    assert count_wizards(wk) == 11


if __name__ == '__main__':
    same_house_as_parent_test()
    count_wizards_tests()
    count_depth_test()
    print('All Tests passed!')
# ==
# REMEMBER: 3 Kinds of Accumulators:
# 1 - context preserving Accumulators: preserve context lost in Natural Recursion
# 2 - Result So Far: help achieve tail Recursion by preventing pending Operations
# 3- Work List Accumulator: help achieve tail Recursion by eliminating the need to
#    retain future recursive calls in pending Operation.
# ===============================
# Do you REMEMBER same_house_as_parent(wizard)? Design same function but to be
# Tail recursive!:


# Wizard -> (Listof String): 'Ahmed s List'
# produce the name of each wizard lives in same house with its direct parent
# def same_house_as_parent2(): # stub
    x = LOX()
    x.value = ''
    return x

# TEMPLATE: from Wizard acc version(arb-arity tree wrapped in local fired by a trempoline)
# with SPECIFICATION Additions:
# worklist accumulator
# result so far accumulator
# , for "tail recursion" Our Ultimate goal

# Solving the problem that way, require to build up upon todo listof Wizard
# to be listof ToDo: which is entry a little cplicated:
# preserve the parent name <String> of each wizard while created and appended

# def same_house_as_parent2(wizard):
#     # acc<worklist>: our own implementation of (Listof Wizard), LOWiz() holds todo entries ToDo
#     # invarian? at point of each call to fn_for_wiz, it is a list of un visited wizards
#     #
#     # acc<Result so far>: our own implementation of (listof X): LOX()
#     # invarian?  holds those names cared about we have seen yet.
#
#     def class ToDo(object):
#         def __init__(self, wizard, parent):
#             self.wizard = wizard  # Wizard
#             self.parent = parent  # String
#     # ToDo is ToDo(Wizard, String)
#     # interp. is a compound Wizard_Entry assigns for each wizard entry its paren name
#
#     def same_house_as_parent2(wizard_entry, todo, names):
#         return fn_for_low(... todo wizard_entry.wizard wizard_entry.wizard.name wizard_entry.wizard.house wizard_entry.parent names) # Tail Recursion
#     def fn_for_low(todo, names):
#         if todo is None:
#             return ... names
#         else: return same_house_as_parent2(... todo names)  # Tail Recursion
#     return same_house_as_parent2(wizard, ..., ...)




def same_house_as_parent2(wizard):
    # acc<worklist>: our own implementation of (Listof Wizard), LOWiz() holds todo entries ToDo
    # invarian? at point of each call to fn_for_wiz, it is a list of un visited wizards
    # acc<Result so far>: our own implementation of (listof X): LOX()
    # invarian?  holds those names cared about we have seen yet.

    def class WLE(object): #WLE stands for: Work List Entry
        def __init__(self, wizard, parent=''):
            self.wizard = wizard  # Wizard
            self.parent = parent  # String
            self.next   = None
    # WLE is WLE(Wizard, String)
    # interp. is a compound work list Entry assigns for each wizard its parent name
    #


    # Wizard -> WLE
    # produce the work list entry for each corresponding wizard
    def mapwiz(wizard, parent_house):
        todo_entry = WLE()
        todo_entry.wizard = wizard
        todo_entry.parent = parent_house
        return todo_entry



    # (listof Wizard) -> (listof WLE)
    # produce the work list entry for each corresponding wizard
    def make_todo_list(low, parent_house):
        if low is None:
            return None
        else:
            entry = mapwiz(first_Wiz(low), parent_house)
            return None

    # Wizard -> WLE
    # pre-loads the current todo with current wizard children
    def append_two_todos(wizard):
        return None
    # ==========================================================================
    def same_house_as_parent2(wizard, todo, parent_house, names):
        if  parent_house == wizard.house:
            names.append(wizard.house)
        return fn_for_lotodo(append_two_todos(make_todo_list(wizard.children), wizard.name), todo), names)) # Tail Recursion
    def fn_for_lotodo(todo, names):
        if todo is None:
            return names
        else:
            return same_house_as_parent2(first_todo(todo), rest_lotodo(todo), first_todo(todo).parent , names)  # Tail Recursion
    return same_house_as_parent2(wizard, None, '', LOX())

# Tests?: No Cretiria of our own list about Equality! untill now
# ==
