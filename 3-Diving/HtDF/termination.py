# https://upload.wikimedia.org/wikipedia/commons/b/b9/Collatz-stopping-time.svg

# Sierpinski_tri and our new friend hailstone functions use generative recursion
# means they are Not build on a well formed self refferential type comment
# we do not have a previous proof of stopping?
# How do we know that every recursion if go to stop and terminate?

# Answer Three Questions: ensures  a solid thinking about generative recursion you develope
# Three part Termination Argument:
    # 1- BASE CASE:
            # ???
    # 2- REDUCTION STEP:
            # ???
    # 3- "Argument" that repeated Apllication of reduction step will eventually reach the base case
            # ???

def hailstone(n):
    if n == 1:
        return [1]
    else:
        if n%2 == 0:
            return [n]+hailstone(n/2)
        else:
            return [n]+hailstone(n*3+1)

# 1- BASE CASE:
        # n is equal to 1  (n == 1)
# 2- REDUCTION STEP:
        # if n is even then n/2   (good reduction)
        # if n is odd  then n*3+1 (very bad reduction, impossible to terminate!)
# 3- "Argument" that repeated Apllication of reduction step will eventually reach the base case
        # ??? Mathmaticiens Did NOT found a proof to how any initial n hits number 1.
        # as Computer Scientist it is IMPOSSIBLE to call this function recursivly!!
