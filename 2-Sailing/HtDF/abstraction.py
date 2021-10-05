import math


# 1- ABSTRACTION BY PARAMETRIZATION
# PI = 3.14
#
# x1  = 1.6
# circle1_area = PI*x1*x1
#
# x2  = 3.88
# circle2_area = PI*x2*x2
#
#
# # Think to reduce the code you typing ?? Function
# def circle_area(x):
#     PI = 3.14
#     return  PI*x*x
# Abstraction: we observe many 'repitition expression'  and the only 'point of variant'
# =====================================================================================
# What we do 'Abstractly' is:
    # - having one copy ot the repetitive code expression
    # - with a more general name
    # - add a parameter(s) for varing position(s)
# then:
    # - replace each repetitive expression with call to absttract function
    # - pass varying value
# =====================================================================================

# def find_y (list):
#     if list.head == 'y':
#         return ok we found
#     list.head = list.head.next
#     return find_y(list.head)
#
# def find_x (list):
#         if list.head == 'x':
#             return ok we found
#         list.head = list.head.next
#         return find_y(list.head)
#
# # Abstraction
# def find(list, name):
#     if list.head == name:
#         return ok we found
#     list.head = list.head.next
#     return find_y(list.head)

# =========================================================================================
# Doing Abstraction imply doing HtDF Recipie in reverse: why? to keep out mentra "start form simple to a little complex"
# Is that means function signature is the hardest step? yes it somtimes be,
# You trace line by line, to detect input and output seprately and you find out if there is a "Generic Type"
# "Generic Type": function cnsumes is not specific can be whatever but it is a 'place'holder, once you determine it replace it.


# Integers -> [0 +Integers]
# def square(x):
#     return x*x
#
# # [0 +Integers] -> [0 +Integers]
# def square_root(x):
#     return math.sqrt(x)
#
#
# # # # Abstraction
# # Abstract Signature: ( X -> Y ) X -> Y      Generic Types: X Y
# # Abstrat Purpose: givin fn,  n .. produces fn(n)
# def map(fn, x):
#     return fn(x)
#
# def length(s):
#     return len(s)
#
# assert map(square, x=2) == 4
# assert map(square_root, x=4) == 2
# # ==
# assert map(length, x='abc') == 3  # ohh! it is more Generic, we start with wrapping [square, square_root] in abstract way, we find out many fn can be passed!
# # X is a Generic Type pass to
#
#
# print('All Tests passed!')
# ================================================================================
# re-Designing other Important abstract Functionallity:
# (X -> Boolean) (ListOf X) -> (ListOf X)
# re produce a given ListOfX ignoring Xs that miss the condition produced by the function argument

def positive(x):
    return x>0

def negative(x):
    return x<0

# #PROBLEM# i CAN NOT reset filtered_list
def filter2(fn, listofX, i=0, filtered_list = None):
    if filtered_list == None and i==0:
        filtered_list = []
    if i == len(listofX)-1:
        return filtered_list
    else:
        if fn(listofX[i]):
            filtered_list.append(listofX[i])
        i += 1
        return filter2(fn, listofX, i)

numbers = [3 ,-2, -8, 4, -1, 2, 0]
print(filter2(positive, numbers)) #[3, 4, 2]
# print(filter2(negative, numbers)) #[3, 4, 2, -2, -8, -1]

# ================================================================================
# build_list like range()
# How to stretch maximum number of recursion?
                # import sys
                # sys.setrecursionlimit(5000)

# def identity(x):
#     return x

# # Natural (Natural -> X) -> (ListOf X)
# def build_list(n, i=0, fn=identity, list=[]):
#     if i == n:
#         return list
#     list.append(fn(i))
#     i += 1
#     print(i)
#     return build_list(n, i)

# print(build_list(5))

# ================================================================================
# Python mutable Function Default argument: [Advanced Topic]
# def add_emp(emp, emp_list=[]):
#     emp_list.append(emp)
#     print(emp_list)
#
# print(add_emp.__defaults__)
# add_emp('Ahmed')
# add_emp('Soliman')
# print(add_emp.__defaults__)
#
# print('=========================')
#
# def add_emp_fixed(emp, emp_list=None):
#     if emp_list == None:
#         emp_list = []
#     emp_list.append(emp)
#     print(emp_list)
#
# print(add_emp_fixed.__defaults__)
# add_emp_fixed('Ahmed')
# add_emp_fixed('Soliman')
# print(add_emp_fixed.__defaults__)







# ==
