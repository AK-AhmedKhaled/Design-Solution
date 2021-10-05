# Data Definitions
class Element(object):
    def __init__(self, name, data, subs):
        self.name = name
        self.data = data
        self.subs = subs
        self.next = None  # work with this pointer should be done by internal implementation of the list
# Element is  Element(String Integer ListOfElements)


# interp. An Element in the file System, with name, and either data or sub-elements
                                                            # - if data is 0, then subs is considered to be List of sub-elements.
                                                            # - if data in non-0, then subs is ignored.

class ListOfElements(object):
    def __init__(self, element=None):
        self.head = element

    def append(self, element):
        NewNode = Element(element.name, element.data, element.subs)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next = NewNode

    def listprint(self):
        printNode = self.head
        while printNode is not None:
            print (printNode.name)
            printNode = printNode.next




# ListOfElements is one-of:
    # - None
    # - (Element ListOfElements)


#NOTE#: here you can see the self-reference cycle , where is mutual-reference?
        # Element is point to  ListOfElements as part of it AND ListOfElements is point to Element as part of it!! ..Mutual-reference Cycle

# interp. a list of file system Elements

# Data Examples: How to combose such Structure ??



subsf1 = ListOfElements()
# subsf1.listprint()
# print('====')
f1 =  Element('f1', 1 , subsf1)

subsf2 = ListOfElements()
# subsf2.listprint()
# print('====')
f2 =  Element('f2', 2 , subsf2)

subsD4 = ListOfElements()
subsD4.append(f1)
subsD4.append(f2)
# subsD4.listprint()
# print('====')
D4 =  Element('D4', 0 , subsD4)

subsf3 = ListOfElements()
# subsf3.listprint()
# print('====')
f3 =  Element('f3', 3 , subsf3)

subsD5 = ListOfElements()
subsD5.append(f3)
# subsD5.listprint()
# print('====')
D5 =  Element('D5', 0 , subsD5)

subsD6 = ListOfElements()
subsD6.append(D4)
subsD6.append(D5)
# subsD6.listprint()
# print('====')
D6 =  Element('D6', 0 , subsD6)

# VISUALIZATION OF THE TREE
#                  D6:0
#         D4:0                    D5:0
#    f1:1     f2:2                f3:3
#


# How to Tempating this Mutual Recursion?
# # Data Templates
# def fn_for__Element(element):
#      return ...element.name
#                element.data
#                fn_for__ListOfElements(element.subs)
#
#
# def fn_for__ListOfElements(loe):
#     if loe is None:
#         return ...
#     else:
#         return ...fn_for__Element(loe.head)
#                   fn_for__ListOfElements(loe.head.next)

# # Did you hear about pre encapsulated Template ??
# # to make good interface hide all collaborative functions implementation details
# def fn_for_Element(element):
#     # Definitions: element, fn_for__Element, fn_for__ListOfElements
#     def fn_for__Element(element):
#          return ...element.name
#                    element.data
#                    fn_for__ListOfElements(element.subs)
#     def fn_for__ListOfElements(loe):
#         if loe is None:
#             return ...
#         else:
#             return ...fn_for__Element(loe.head)
#                       fn_for__ListOfElements(loe.head.next)
#     # Exepression
#     return fn_for__Element(element)

# ==

class String(object):
    def __init__(self, value=''):
        self.value = value
        self.next  = None

class ListOfStrings(object):
    def __init__(self, node=None):
        self.head = node

    def append(self, name):
      NewNode = String(name)
      if self.head is None:
         self.head = NewNode
         return
      laste = self.head
      while(laste.next):
         laste = laste.next
      laste.next=NewNode

    def listprint(self):
        printNode = self.head
        while printNode is not None:
            print (printNode.value)
            printNode = printNode.next

    def mergeLists(los1, los2):
        tail = los1.head
        if los1.head is None:
            tail.next = los2.head
            return
        if los2.head is None:
            tail.next = los1.head
            return
        while tail.next != None:
            tail = tail.next
        tail.next = los2.head
        return los1


list_all_names = ListOfStrings()
list_all_names.append(D6.name)
list_all_names.append(D4.name)
list_all_names.append(f1.name)
list_all_names.append(f2.name)
list_all_names.append(D5.name)
list_all_names.append(f3.name)
# list_all_names.listprint()

additional_names = ListOfStrings()
additional_names.append('ff4')
additional_names.append('ffg')
additional_names.append('f47')
# additional_names.listprint()

# ListOfStrings.mergeLists(list_all_names, additional_names).listprint()
