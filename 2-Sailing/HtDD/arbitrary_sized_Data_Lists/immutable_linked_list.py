# TWO one-of Types as parameters

class String(object):
   def __init__(self, value=None):
      self.value = value
      self.next = None

class LinkedList(object):
    """docstring for LinkedList.
        Immutable Linked Lists is so important to make a 'sequence' of operations on lists
        and the Original remains the same !
    """
    def __init__(self):
       self.head = None

    def print_list(self):
        temp = make_copy()
        if  temp.head is None:
            return ''
        print(temp.head.value)
        temp.head =  temp.head.next
        temp.print_list()

    def make_copy(self):  # developed by me
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

print(list1)
print(list2)
print(list3)
copy3 = list3.make_copy()
print(copy3)


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
