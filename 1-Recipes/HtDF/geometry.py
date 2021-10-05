# DESIGN a function called area that consumes the length of one side
# of a square and produces the area of the square.

# length is Number    # Type Comment

# Number (0, infin) represents the length of one side of a square  # Interpretation

# Data Examples
l1 = 0
l2 = 2.5
l3 = 4

# # Data Driven Template
# def fn_for_length(l):
#     if (type(l) in [int, float] && l > 0):
#         return (...l)
# Template Rules used:
    # - atomic non-distinct: Integer
# /* it is optionally to add guards type(l) in [int, float] && l > 0 , see debugging and testing section*/


#1- Number -> Number    # signature
#2- purpose: consumes the length of one side of a square and produces the area of the square.

# #3- stub
# def calcSquare(l):
#     return 0

#5- function body: Raw Material are copied from Data Driven Template gives real sense
def calcSquare(l):
    if (type(l) not in  [int, float] ):
        raise TypeError('the length of square can only be int or float!')
    if (l < 0):
         raise Exception("Sorry, no lenghts below zero !")
    return (l * l)


#4- Examples wrapped in unit tests:
# Manual Testing Setup
def test_case_one():
    assert  calcSquare(l1) == 0, 'should be 0'
def test_case_two():
    assert calcSquare(l2) == 6.25, 'should be 6.25'

if  __name__ == "__main__":
    test_case_one()
    test_case_two()
    print('All Tests Passed!')


#6- Test and Dubgging untill Correct
# length = [ 2 , 1.1, -2.5, 2j, 'two', False ]
# for i in range(len(length)):
#     print ("The volume of cuboid:",calcSquare(length[i]))
