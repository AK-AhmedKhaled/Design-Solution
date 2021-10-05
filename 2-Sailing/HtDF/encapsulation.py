# Lexical Scope
# This Definition is local, another is Global, and another is very deep local..!
# locals is the Base behind Encapsulation (at the time before the OOP)

# Encapsulation made SoftWare Industry Miracles!
# React .. sickitlearn .. Transflow .. SQLlite ..  .. (Encapsulated Packages)
    # they all contain a lot more functions than we need to make a "function" what we need



# Data Definitions
import sys
sys.path.append('..')
from HtDD.mutual_reference.file_system_tree import *


# Pre-Encapsulated Template?
# def fn_for_Element(element):
#     # Definitions: element, fn_for__Element, fn_for__ListOfElements
#     def fn_for__Element(element):
#          return ...element.name
#                    element.data
#                    fn_for_ListOfElements(element.subs)
#     def fn_for__ListOfElements(loe):
#         if loe is None:
#             return ...
#         else:
#             return ...fn_for_Element(loe.head)
#                       fn_for_ListOfElements(loe.head.next)
#     # Exepression
#     return fn_for__Element(element)



# Functions
#NOTE# seems complex Structure?, Design its functions go so smooth~~ thanks to Design Recepie
#      Key? Design 2 functions at once each of them operate on one of the 2 Mutual Recursion Type,
#           both collaporate to combine the solution. they require eah other to work "They are mutually Recursive"

#1- Design a function that consumes an 'Element' and produces the sum of all the file data in the tree

# Element -> Integer
# ListOfElements -> ?Integer?

# produce the sum of all the file data in the tree

# stubs
# def sum_data__element(ele):
#     return 0

# def sum_data__loe(loe):
#     return 0






# sum_data makes its own local world,
# instead of silly names, sum_data hides implementation details and provide reason interface to users
def sum_data(element):
    # Definitions
    def sum_data__element(element):
        if element.data != 0:
            return element.data
        return 0 + sum_data__loe(element.subs)

    def sum_data__loe(head):
        temp = head
        if temp is None:
            return 0
        else:
            return sum_data__element(temp) + sum_data__loe(temp.next)


    # what is Exepression?
    return sum_data__element(element)  # The Trampoline


def test_case_one1():
    assert sum_data(f1) == 1
    assert sum_data(D4) == 0+1+2
    assert sum_data(D6) == 0+0+0+1+2+3



def find(element, name):
    # Definitions
    def find_Data__Element(element, name):
        if element.name == name:
            return element.data
        return find_Data__ListOfElements(element.subs, name)

    def find_Data__ListOfElements(loe, name):
        temp = loe
        if temp is None:
            return False
        else:
            if find_Data__Element(temp, name) != False:
                    return find_Data__Element(temp, name)
            else:
                return find_Data__ListOfElements(temp.next, name)
    # Exepression
    return find_Data__Element(element, name)

def test_case_one3():
    assert find(f1, 'f1') == 1
    assert find(D4, 'f2') == 2
    assert find(D4, 'D4') == 0
    assert find(D6, 'D4') == 0
    assert find(D5, 'f3') == 3
    assert find(D4, 'f3') == False
    assert find(D5, 'f1') == False
if __name__=='__main__':
    test_case_one1()
    test_case_one3()
    print('All Tests passed!')
