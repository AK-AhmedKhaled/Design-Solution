# Generic List: Last TRY
# This list is Designed basiclly to hold Strings names of that Room
# But i want it to be Generic

class X(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next  = next

class LOX(object):
    def __init__(self, head=None):
        self.head = head


labelc = X('C', None)
labelb = X('B', labelc)
labela = X('A', labelb)

myLabels = LOX(labela)


# Template
# def fn_for_lox():
#     if lox.head is None:
#         return ...
#     else:
#         return ...fn_for_x(first_X(lox))
#                   fn_for_lox(rest_Xs(lox))

def first_X(lox):
    return lox.head

def second_X(lox):
    return lox.head.next

def rest_Xs(lox):
    if lox.head is None:
        return None
    else:
        return LOX(lox.head.next)

# ==============================================
# ==============================================
# ==============================================
# ==============================================
def apppend(lox, x):
    # head<Object address>: context preserving accumulater
    def apppend(lox, x, head):  # x: is value not X: node
        if lox.head is None:
            lox.head = X(x)
            return lox
        else:
            if lox.head.next is None:
                lox.head.next = X(x)

                lox.head = head
                return lox
            else:
                return apppend(rest_Xs(lox), x, head)
    return apppend(lox, x, lox.head)



def print_Xs(lox):
    if lox.head is None:
        print('')
    else:
        print(first_X(lox).value)
        print_Xs(rest_Xs(lox))

# print_Xs(myLabels)

# (listof String) String -> Boolean
# produce True if a given rooms labels is match a given name
# def is_member(lox, label):  # stub
#     return False
# Template is from LOX
# Added: parameter, label<String>
def is_member(lox, label):
    def matched(room_name, label):
        return room_name == label
    if lox.head is None:
        return False
    else:
        return matched(first_X(lox).value, label) or is_member(rest_Xs(lox), label)

def is_member_test():
    assert is_member(myLabels, 'D') == False
    assert is_member(myLabels, 'C') == True

def equals_X_by_X(lox1, lox2):
    return True

# !!!
# (listof Number) -> (listof Number)
# takes the first (Number)th elements produces a new list of them
def take(lon, number):
    return lon

# !!!
# (listof Number) -> (listof Number)
# takes the last elements o a given list after dropping (Number)th elements
def drop(lon, number):
    return lon


if __name__=='__main__':
    # is_member_test()
    print('All Tests passed!')
# ==
