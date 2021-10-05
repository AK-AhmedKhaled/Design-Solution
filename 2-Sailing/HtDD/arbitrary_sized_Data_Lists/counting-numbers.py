# arbitrary-sized Data
# like any series: counting numbers (factorial belongs), fabonachi series, ....


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
