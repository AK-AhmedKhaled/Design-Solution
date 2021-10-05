# TWO one-of Types as parameters

class String(object):
   def __init__(self, value=None):
      self.value = value
      self.next = None

class ListOfStrings(object):
    """docstring for LinkedList.
        Immutable Linked Lists is so important to make a 'sequence' of operations on lists
        and the Original remains the same !
    """
    def __init__(self):
       self.head = None

    def print_list(self):
        temp = self.make_copy()
        if  temp.head is None:
            return ''
        print(temp.head.value)
        temp.head =  temp.head.next
        temp.print_list()

    def make_copy(self):    # developed by me
        copy = ListOfStrings()
        node = self.head
        if node != None:
            node_cpd = String(node.value)
            copy.head = node_cpd
            node = node.next
        while not node is None:
            node_copied = String(node.value)
            node_cpd.next = node_copied
            node = node.next
            node_cpd = node_cpd.next
        return copy

# ListOfStrings is one-of:
    # - None
    # - String -> ListOfStrings


# Data Examples...
emptylist1 = ListOfStrings()
emptylist2 = ListOfStrings()

list1 = ListOfStrings()
list1.head = String('a')

list2 = ListOfStrings()
list2.head = String('a')
l2_s2 = String('b')
list2.head.next = l2_s2

list3 = ListOfStrings()
list3.head = String('a')
l3_s2 = String('b')
list3.head.next = l3_s2
l3_s3 = String('c')
l3_s2.next = l3_s3

list1.print_list()
list2.print_list()
list3.print_list()
copy3 = list3.make_copy()
copy3.print_list()


# Cross Product Image
                    #2nd   # empty  non-empty
    # 1st   # empty           True     True
            # non-empty       False   it depends ... (1st.a == 2nd.a) and (1st.b == 2nd.b) and (1st.c == 2nd.c) and (1st is empty)
                                                   # (1st.a == 2nd.a) and (1st.b == 2nd.b) and (1st.c == 2nd.c) and (1st is empty)

# # Boring costly Template shows that you could not laverage the CROSS PRODUCT Table
# def fn_for_two_one_of_types(los1, los2):
#     copy1 = los1.make_copy()
#     copy2 = los2.make_copy()
#     if copy1.head is None and copy2.head is None:
#         return True
#     elif copy1 is None and (not copy2 is None):
#         return True
#     elif (not copy1.head is None) and copy2.head is None:
#         return False
#     else:
#         ... copy1.head
#             copy1.head = copy1.head.next ... fn_for_two_one_of_types(..., copy1.head)
#             copy2.head
#             copy2.head = copy2.head.next ... fn_for_two_one_of_types(..., copy2.head)


#  # This is more consice shows good modeling before type any code!
# def fn_for_two_one_of_types(los1, los2):
#     copy1 = los1.make_copy()
#     copy2 = los2.make_copy()
#     if copy1.head is None:
#         return True
#     elif copy2.head is None:
#         return False
#     else:
#         ... copy1.head
#         copy1.head = copy1.head.next ... fn_for_two_one_of_types(..., copy1.head)
#         copy2.head
#         copy2.head = copy2.head.next ... fn_for_two_one_of_types(..., copy2.head)



#NOTE# This simple print if still active will destroy our tests as it mutates our lists !!: its over thanks to make_copy()
# list1.print_list()
# ============================================================================================
# Design a function that consumes 2 ListOfStrings
# and produce True if the first list is a prefix of the second

# Analysis: the ith element of the first less match the jth element of the second list as long as i=j
#           AND the the first list is at most as long as the second


# ListOfStrings, ListOfStrings -> Boolean

# Purpose: its likely to put the first ListOfStrings over the second to see if the first is identical to the first sub-part
#          ,and produce True or False if measurement fails




# def isPrefix(los1, los2):
#     return True


# def isPrefix(los1, los2):
#     if los1.head is None:
#         return True
#     elif los2.head is None:
#         return False
#     else:
#         ok = (los1.head.value == los2.head.value)
#         los1.head = los1.head.next
#         los2.head = los2.head.next
#         return ok and isPrefix(los1, los2)
# here los1, and los2 changed!, we will not be able to run all test cases at once!!!

def isPrefix(los1, los2):
    copy1 = los1.make_copy()
    copy2 = los2.make_copy()
    if copy1.head is None:
        return True
    elif copy2.head is None:
        return False
    else:
        ok = (copy1.head.value == copy2.head.value)
        copy1.head = copy1.head.next
        copy2.head = copy2.head.next
        return ok and isPrefix(copy1, copy2)
# here los1, and los2 remains thanks to make_copy() !!

#NOTE#
# at both of those Examples:
 # list1: 1 2 3  list2: 1 2 3
 # list1: None  list2: None
# if we change the order of checks (check los2.head is None first we got a totally reversed result!!) which Base Case:فخ to drill first

def test_case_one():
    assert isPrefix(emptylist1, emptylist2) == True
    assert isPrefix(emptylist1, list1) == True
    assert isPrefix(list1, emptylist2) == False
    assert isPrefix(list1, list2) == True
    assert isPrefix(list1, list2) == True
    assert isPrefix(list2, list1) == False
    assert isPrefix(list2, list3) == True
    assert isPrefix(list3, list2) == False
if __name__ == '__main__':
    test_case_one()
    print('All Tests passed!')







# =
