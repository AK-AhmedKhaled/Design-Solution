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


# str -> str   # 1- signature
# 2- Purpose: consumes a letter grade and produces the next highest letter grade.

# 3-stub
# def bump_up(lg):
#     return 'A'

# 4- Examples and Unit Tests:
# < Tets are done on the test_design_proccess.py >


# 5- function body: Template is copiead and all right reserved!
def bump_up(lg):
    if (not isinstance(lg, str)):
        raise TypeError("use Strings, one of 'A', 'B', or C' to indicate grade") # Guard: optionally
    if  (lg == 'A'):
        return 'A'
    elif (lg == 'B'):
        return 'A'
    elif (lg == 'C'):
        return 'B'
    else:
        raise Exception("my function consumes one of 'A', 'B', or C' to indicate grade, can not deal with " +  str(lg))
# 6- Debugging and Tesing: untill Correc
grades = ['A', 'C', 'B', 7, True]
# grades = ['A', 'C', 'B']
for grade in grades:
    print(bump_up(grade))
