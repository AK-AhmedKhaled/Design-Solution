# Woories about performance is a crucial to study and analyze
# it turns out
# 1- its too easy to worry about the program efficiency
# 2- its too easy to worry too soon about the program efficiency
# 3- its too easy to worry just plain incorrectly about the program efficiency

# GENERAL RULE: it is better idea to design a simple program that is easy todo
#               understand and to change, and then worry about efficiency later
#               once the program is running

# SUGGESTION: run the program againist a sample of dataset and measure
#             its performance to see "where" the real performance problems are.
#
# SURPRISINGLY:
# 1- often what you think that is a performance problem is is not
# 2- some otherthings you you did not think it is a performance problems,
#    it turns out it is unfortenately!

## FINAL ADVICE:
# There is one category you need to fix as part of the design
# problems with exponential Growth of Running Time as input grows

# How Lexical Scoping let us do such optimization one some Category
# causes exponential Growth of Running Time as input grows ?
    # ...by avoiding Re-Computation

# To Calc the Running Time of a program/function in python is like:
                    # import time
                    # start_time = time.time()
                    # main()  or 'any statement'
                    # print("--- %s seconds ---" % (time.time() - start_time))

import sys
import time
start = time.time()
sys.path.append('..')
from HtDD.mutual_reference.file_system_tree import *  # import Data Definitions


# consider skinny list like this:
# y  =  Element('y', 1 ,None)
# x5 =  Element('x', 0 , y)
# x4 =  Element('x', 0 ,x5)
# x3 =  Element('x', 0 ,x4)
# x2 =  Element('x', 0 ,x3)
# x1 =  Element('x', 0 ,x2)
# Runtime of the program is in millis 2.7074813842773438


# y   =  Element('y', 1 ,None)
# x10 =  Element('x', 0, y)
# x9  =  Element('x', 0,x10)
# x8  =  Element('x', 0 ,x9)
# x7  =  Element('x', 0 ,x8)
# x6  =  Element('x', 0 ,x7)
# x5  =  Element('x', 0 ,x6)
# x4  =  Element('x', 0 ,x5)
# x3  =  Element('x', 0 ,x4)
# x2  =  Element('x', 0 ,x3)
# x1  =  Element('x', 0 ,x2)
# Runtime of the program is in millis 2.0284652709960938


y   =  Element('y', 1 ,None)
x20 =  Element('x', 0, y)
x19 =  Element('x', 0, x20)
x18 =  Element('x', 0, x19)
x17 =  Element('x', 0, x18)
x16 =  Element('x', 0, x17)
x15 =  Element('x', 0, x16)
x14 =  Element('x', 0, x15)
x13 =  Element('x', 0, x14)
x12 =  Element('x', 0, x13)
x11 =  Element('x', 0, x12)
x10 =  Element('x', 0, x11)
x9  =  Element('x', 0,x10)
x8  =  Element('x', 0 ,x9)
x7  =  Element('x', 0 ,x8)
x6  =  Element('x', 0 ,x7)
x5  =  Element('x', 0 ,x6)
x4  =  Element('x', 0 ,x5)
x3  =  Element('x', 0 ,x4)
x2  =  Element('x', 0 ,x3)
x1  =  Element('x', 0 ,x2)
# Runtime of the program is in millis 268.6138153076172
# after avoid recomputation
# Runtime of the program is in millis 2.349853515625



from encapsulation import find
result = find(x1, 'y')
assert result == 1
print(result)

end = time.time()
print(f"Runtime of the program is in millis {(end - start)*1000}") # Did you see the exponential Growth ? in fact NO hahaha!

# ==
#  How to systimaticlly AVOID RE-COMPUTATION on recursive functions ?
# 1- wrap nearest enclosing expression in a local
# 2-
def find(element, name):
    # Definitions
    def find_Data__Element(element, name):
        if element.name == name:
            return element.data
        return find_Data__ListOfElements(element.subs, name)

    def find_Data__ListOfElements(loe, name):
        if loe is None:
            return False
        else:
            found = find_Data__Element(loe, name)  # local 'found' save us a recomputation!
            if found != False:
                    return found
            else:
                return find_Data__ListOfElements(loe.next, name)
    # Exepression
    return find_Data__Element(element, name)


# result = find(x1, 'y')
# assert result == 1
# print(result)
#
# end = time.time()
# print(f"Runtime of the program is in millis {(end - start)*1000}")  # Did you see the exponential Growth ? in fact NO hahaha!
# Runtime of the program is in millis 2.0635128021240234
