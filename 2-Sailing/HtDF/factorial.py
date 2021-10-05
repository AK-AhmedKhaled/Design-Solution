# Factorial recursively
#NOTE# You decide how to treat Natural Numbers

# Natural is one-of:
    # = 0     BASE CASE
    # = Natural += 1

# Natural Numbers is a series of arbitrary size: 0, 1, 2, 3, 4, 5, .., ..

#
n0 = 0   # BASE CASE
n1 = 1
n2 = 5

# # Data Driven Template
# def fn_for_Natural(n):
#     if (n == 0):
#         (...)
#     else:
#         (... n
#              fn_for_Natural(n-1)   # Transition: movement through BASE CASE
#         )



# Natural -> natural         # Signature

# Purpose: consumes a Natural which we defined (Treated as a series),
# and produces natural (merely a result but should be positive greater than 0)

# # stub
# def factorial(n):
#     return 1


def factorial(n):
    if (n == 0):
        return 1
    else:
        return n*factorial(n-1)

# Unit Tests and Examples
def test_case_factorial():
    assert factorial(n0) == 1
    assert factorial(n1) == 1
    assert factorial(n2) == 120
if __name__ == "__main__":
    test_case_factorial()
    print('All Tests passed!')
