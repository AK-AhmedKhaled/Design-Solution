# Lambda Expression

# when a function we will wont use it outside, we likely to define it as a local
# when this local function defined and used(called) only once in its scope
# usually function bodies are short, so very clear to see what it does even ..
#   function descriptive name always be less clear readable than the direct code  isLessThan? or '<' clearer ?

# making anonymous function using lambda: enhance readabillity.
# lambda is say: here is a function without a name, without its own local scope setup/definition
    # ... you can use it once


# Lambda Expression
    # A lambda function is a small anonymous function.
    # A lambda function can take any number of arguments, but can only have one expression.


# W3 Examples
# Example1
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Example2:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
