class X(object):
    def __init__(self):
        self.value = None
        self.next  = None
# ===============
# None
# ^^
x15 = X()
x15.value = 'e'
x15.next  = None
# ^^
x14 = X()
x14.value = 'd'
x14.next  = x15
# ^^
x13 = X()
x13.value = 'c'
x13.next  = x14
# ^^
x12 = X()
x12.value = 'b'
x12.next  = x13
# ^^
x11 = X()
x11.value = 'a'
x11.next  = x12
# =======================================

# None
# ^^
x25 = X()
x25.value = 5
x25.next  = None

# ^^
x24 = X()
x24.value = 4
x24.next  = x25

# ^^
x23 = X()
x23.value = 3
x23.next  = x24

# ^^
x22 = X()
x22.value = 2
x22.next  = x23

# ^^
x21 = X()
x21.value = 1
x21.next  = x22
# ====================================
class LOX(object):
    def __init__(self):
        self.head = None

lox1 = LOX()
lox1.head = x11


lox2 = LOX()
lox2.head = x21

lox3 = None
# ==
# ====================================
# Testing append
x3 = X()
x3.value = 'test3'
x3.next  = None

x2 = X()
x2.value = 'test2'
x2.next  = None

x1 = X()
x1.value = 'test1'
x1.next  = x2

lox4 = LOX()
lox4.head = x1
# ====================================
# Primitive Operations

# listof X -> Y
# listof X -> X
# produce X element pointed by the head of a given listof X
# produce X element (pointed by the head of a given listof X) s value 'Y'
# def first_X(lox):  #stub
#     return None

def first_X_val(lox):
    return lox.head.value

def first_X(lox):
    return lox.head
# Tests
def test_first():
    assert first_X_val(lox1) == 'a'
    assert first_X_val(lox2) ==  1
    assert first_X(lox1) ==  x12
    assert first_X(lox2) ==  x21
# =======================================================
# ============
# X -> X
# produce a copy of a given x, not only its value but its full linked sequence

# REVERSE ENGINEERING
# X1(1, X2)   ->  X2(2, X3) ->  X3(4, X4) ->  X4(5, None)
# x_(1, #--)      X_(3, #--)   X_(4, #--)     X_(5, None)
def copy_x(x):
    if x is None:
        return None
    else:
        x_head = X()
        x_head.value = x.value
        x_head.next  = link_next(x.next)
        return x_head
# =============
# X -> X
# produce new x holds a value of its correspndse and holds all sequnce information
def link_next(x):
    if x is None:
        return None
    else:
        return copy_x(x)
# ======
# listof X -> listof X
# produce same list but first element is truncated.
# CARE!!.. we will not change what the head of a given list, its the whole structure is about!
def rest_lox(lox):
    if lox is None or lox.head.next is None:
        return None
    else:
        new_lox = LOX()
        x_head       =  copy_x(lox.head.next)
        new_lox.head = x_head
        return new_lox
# Tests
def test_rest_lox():
    assert rest_lox(lox3) == None
    # assert rest_lox(lox2) == ???
# ==
# ========================
# ========================
# ===Main Functionality===
# ========================
# ========================
# listof X -> None
# interp. at a time print out X content untill you reach end of a given list
def print_list(lox):
    if lox is None:
        print(' ')
        return None
    else:
        print(first_X_val(lox))
        print_list(rest_lox(lox))

# print_list(lox1)
# print_list(lox2)
# ===================================
# (listof X), X -> (listof X)
# produces same list with last element joined at the end of it
# def append(list, element):  # stub
#     return None
#

# def append(l0, element):
#     def append(l, ele, templ, once):
#         if once:
#             templ.head = l.head
#
#         if l is None:
#             newl = LOX()
#             newl.head = element
#             return newl
#
#         if l.head is None:
#             l.head = element
#             return l
#
#         if templ.head.next is None:
#             templ.head.next = element
#             return l
#         else:
#             templ.head = templ.head.next
#             return append2(l, element, templ, False)
#
#     return append(l0, element, LOX(), True)
# ==========================================================
# version that takes String data: create X intennally!
def append_by_val(l0, data):
    def append(l, d, templ, once):
        if once:  # BY ME: Ahmed Khaled
            templ.head = l.head
        if l is None:
            element = X()
            element.value = d

            newl = LOX()
            newl.head = element

            return newl
        if l.head is None:
            element = X()
            element.value = d
            l.head = element
            return l
        if templ.head.next is None:
            element = X()
            element.value = d

            templ.head.next = element
            return l
        else:
            templ.head = templ.head.next
            return append(l, d, templ, False)
    return append(l0, data, LOX(), True)

# ===============================
lox_names1 = LOX()
A1 = X()
A1.value = 'A'
lox_names1.head = A1
# ===============================
A2 = X()
A2.value = 'A'
A2.next  = None
# ------------------
lox_names2 = LOX()
F2 = X()
F2.value = 'F'
F2.next  = None

E2 = X()
E2.value = 'E'
E2.next  = F2

lox_names2.head = E2

# ==== See
# print_list(lox_names1)
# print_list(lox_names2)
# print_list(append_by_val(lox_names2, 'A'))
# ==== OK


# WE NEED TO DEFINE WHAT EQUALITY MEANS FOR ASSERTION TEST!!
def append_by_val_tests():
    assert append_by_val(None, 'A')       == lox_names1      # 'A' -> None
    assert append_by_val(lox_names2, 'A') == lox_names3#!!!   # 'E' -> 'F' -> 'A' -> None


# new_list = append_by_val(lox4, x3)
# new_list = append(lox4, 'test3')
# print_list(new_list)
# ===================================
# if __name__=='__main__':
#     test_first()
#     append_by_val_tests()
#
