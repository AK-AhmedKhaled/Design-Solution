# # Global Scope: Definitions
# x = 1
# y = 2
# def local_scope(z=1):
#     # Definitions: z parameter is included to local_scope definitions
#     y = 3
#     def local(x):
#         # Definitions: x
#
#         # Exepression
#         return x*z
#
#     # Exepression
#     return (x + y)* local(y)
#
# # Exepression
# print(x+local_scope()+y)
# ===========================================

# x = 1
# def local(x=2):
#     return x*x
# print(x+local()+x)
#
# # Evaluation:
#     # - renaming: definition by defintion and for each renaming also its reference on the local (globally unique name)
                         # x -> x0
#     # - lifting: all Definitions (only) to most top level scope
                         # x0 = 2
#     # - replacing: All local call by its renamed Exepression
                        # local() -> x0*x0
                        # x  = 1
                        # x0 = 2
                        # print(x+x0*x0+x)
# ===========================================

# # use Local To Encapsulate our Implementaion to the world in easy way
# def interface(param):
#     # Definitions
#     def fn_for_any():
#         return 0
#     counter = 0
#     # Exepression: has access to global but enjoys access its local, and the outside world not.
#     return 0 + fn_for_any() * counter
# # use Local to avoid re-Computation? especially on recursive functions
# y = x + 1
# z = 2*y + x + 1
#
# y = x + 1
# z = 2*y + y

# =========================
# x=0
# if x==0:
#     print('its zero')
# else:
#     y = 1
# print(y)  #  NameError: name 'y' is not defined!!

# ====================================================
# What is the Difference between this two cases?

# i = 0
# while i<10:
#     i = 0
#     i += 1
#     print(i)

# i = 0
# while i<10:
#     i+=1
#     print(i)
# ====================================================
# in recursive functions any local has an effect on the final result must be defined in parameter list!
# Correct
# def printList(arr, i=0):
#     if i == len(arr):
#         return
#     print(arr[i])
#     i += 1
#     printList(arr, i)
# printList(['a', 'b', 'c'])

# # WRONG
# def printList(arr):
#     i = 0
#     if i == len(arr):
#         return
#     print(arr[i])
#     i += 1
#     printList(arr, i)
# printList(['a', 'b', 'c'])
# =
