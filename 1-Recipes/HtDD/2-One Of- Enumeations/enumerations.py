# Using the LetterGrade data definition below design a function that
# consumes a letter grade and produces the next highest letter grade.
# Call your function bump-up.

# 1- No possible Structure

# LetterGrade is one-of:
#     - 'A'
#     - 'B'
#     - 'C'                        # 2- Type Comment


# 3- Interpretation: the letter grade in a course as 'A' > 'B' > 'C'

# 4- Data Example
grade1 = 'C'
grade2 = 'B'
grade3 = 'A'

# # 5- Data Template for function operating on this Type we defined
# def fn_for_LetterGrade(lg):
#     if (type(lg) not str):
#         raise TypeError("My function consumes one of Those 'Strings' 'A', 'B', or C' to indicate grade")
#     elif (lg == 'A'):
#         return (...lg)
#     elif (lg == 'B'):
#         return (...lg)
#     elif (lg == 'C'):
#         return (...lg)
#     else:
#         return (...lg)
# Template Rules used:
    # - one-of: 3 cases
    # - atomic non-distinct: str 'A'
    # - atomic non-distinct: str 'B'
    # - atomic non-distinct: str 'C'
