# import Data Definitions
import sys
sys.path.append('..')
from HtDD.mutual_reference.file_system_tree import *


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



# VISUALIZATION OF THE TREE
#                  D6:0
#         D4:0                    D5:0
#    f1:1     f2:2                f3:3


# functions bodies,
def sum_data__element(element):
       if element.data != 0:
           return element.data
       return 0 + sum_data__loe(element.subs)

#ADVICE#: Trust self-Natural Recursion and mutual-Natural Recursion :)#
def sum_data__loe(head):
    temp = head
    if temp is None:
        return 0
    else:
        return sum_data__element(temp) + sum_data__loe(temp.next)


# unit tests:
def test_case_one1():
    assert sum_data__element(f1) == 1
    assert sum_data__element(D4) == 0+1+2
    assert sum_data__element(D6) == 0+0+0+1+2+3

def test_case_two1():
    assert sum_data__loe(None) == 0
    assert sum_data__loe(f1.subs) == 0
    assert sum_data__loe(D4.subs) == 1 + 2
if __name__=='__main__':
    test_case_one1()
    test_case_two1()
    print('All Tests passed!')

#2- Design a function that consumes an 'Element' and produces a list of names of all elements in the tree


#3- Design a function that consumes a String Element and produces True if there is an element in the tree
  # with the given name

# Element, name        -> Boolean
# ListOfElements, name -> Boolean

# consumes a String and an Element and produces if Element and any of its subs has that name

# def name_exist__element(element, name):
#     return True
#
# def name_exist__ListOfElements(head, name):
#     return True


# VISUALIZATION OF THE TREE
#                  D6:0
#         D4:0                    D5:0
#    f1:1     f2:2                f3:3

#NOTE:# when pass a parameter like name, make sure of its behavior,
      # Is it will be constant over time? or it must updated to generate solution

def name_exist__element(element, name):
        if element.name is name:
            return True
        return name_exist__ListOfElements(element.subs, name)


def name_exist__ListOfElements(head, name):
    if head is None:
        return False
    else:
        return name_exist__element(head, name) or name_exist__ListOfElements(head.next, name)



def test_case_one2():
    assert name_exist__element(D6, 'D6')    == True
    assert name_exist__element(D6, 'D5')    == True
    assert name_exist__element(D6, 'f2')    == True
    assert name_exist__element(D6, 'test1') == False

def test_case_two2():
    assert name_exist__ListOfElements(None, 'any')   == False
    assert name_exist__ListOfElements(D4, 'D4')      == True
    assert name_exist__ListOfElements(D4, 'D5')      == True
    assert name_exist__ListOfElements(D4, 'dir1')    == False
if __name__=='__main__':
    test_case_one2()
    test_case_two2()
    print('All Tests passed!')
#
# BackTracking Search
# Design a function that consumes String and Element and looks for a data element with the given name.
# if it finds that element it produces its data, otherwise it produces False.


# Element String        ->    Integer or False
# ListOfElements String -> ?? Integer or False ??

# search the tree habits under the given Element for a given name,
# produce the data if Element was found; False otherwise


# def find_Data__Element(element, name):
#     return 0
#
# def find_Data__ListOfElements(head, name):
#     return False




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

# VISUALIZATION OF THE TREE
#                  D6:0
#         D4:0                    D5:0
#    f1:1     f2:2                f3:3

def test_case_one3():
    assert find_Data__Element(f1, 'f1') == 1
    assert find_Data__Element(D4, 'f2') == 2
    assert find_Data__Element(D4, 'D4') == 0
    assert find_Data__Element(D6, 'D4') == 0
    assert find_Data__Element(D5, 'f3') == 3
    assert find_Data__Element(D4, 'f3') == False
    assert find_Data__Element(D5, 'f1') == False

def test_case_two3():
    assert find_Data__ListOfElements(None, 'f1') == False
    assert find_Data__ListOfElements(f1, 'f2')   == 2
if __name__=='__main__':
    test_case_one3()
    test_case_two3()
    print('All Tests passed!')

















#
