# When we make an Generic and Abstract Function
# in Case we pass a function to act as a predicate, and it does not exist or prepared yet...
# There are Two Cases:
# [OPTIONAL]:

# function that definition of a predicate upnormal() checks for i > 13.14487 and return Boolean
# we make it locally

# arr = [11.4, 13.66, 15.8, 32.1, 27.53, 7.35]
# THRESHOLD = 13.14487
# # (ListOf Number) -> (ListOf Number)
# def upnormal(list):
#     upnormals = []
#     def is_upnormal(x):
#         return x > 13.14487
#
#     for i in list:
#         if is_upnormal(i):
#             upnormals.append(i)
#     return upnormals
# #
# print(upnormal(arr))
# =========================================
# def is_upnormal(x):
#     return x > 13.14487
#
# def upnormal2(fn ,list):
#     upnormals = []
#     for i in list:
#         if fn(i):
#             upnormals.append(i)
#     return upnormals
#
# print(upnormal2(is_upnormal, arr))
# =========================================
# =========================================
# =========================================

# [FORCED]:
# WRONG APPROACH
# THIS CASE is popular to face you, ready made is not specific for your problem
# arr = [11.4, 13.66, 15.8, 32.1, 27.53, 7.35]
# THRESHOLD = 13.14487
#
# def is_upnormal(x):
#     return x > threshold
#
# # (X -> Boolean) (ListOf Number) threshold -> (ListOf Number)
# def upnormal2(fn ,list, threshold):
#     upnormals = []
#     for i in list:
#         if fn(i):
#             upnormals.append(i)
#     return upnormals
#
# print(upnormal2(is_upnormal, arr, THRESHOLD))

# ==========================================================
arr = [11.4, 13.66, 15.8, 32.1, 27.53, 7.35]
THRESHOLD = 13.14487

# Evaluating local Definition for each call to upnormal2
# with a new value of threshold, works that way...

# def is_upnormal_0(x):
#     return x > currThreshold"

# (X -> Boolean) (ListOf Number) threshold -> (ListOf Number)
def upnormal2(list, threshold):
    upnormals = []
    def is_upnormal(x):
        return x > threshold

    for i in list:
        if is_upnormal(i):
            upnormals.append(i)
    return upnormals
print(upnormal2(arr, THRESHOLD))
# ==========================================================
# ==========================================================
# ==========================================================
# أنا استفدت ايه؟
# Simple fix to that is to make is_upnormal(x, threshold), But why is useful
# because some times an abstract general function its predicate is designed to
# recieve only one argument and your problem equire to that helper to
# make its answer based on access to your outer function argument,
# if that is the case, define your own worked predicate locally to enable access to argement
