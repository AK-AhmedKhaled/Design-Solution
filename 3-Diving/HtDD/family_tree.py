# Harry Potter Family Tree
class Wizard(object):
    def __init__(self, name, house, children):
        self.name       = name
        self.house      = house
        self.children   = children
        self.next       = None

# Wizard is Wizard(String, String, (listof Wizard))

# interp. a Wizard of name, house, list of children!

class LOWiz(object):
    def __init__(self, wizard=None):
        self.head = wizard

# (listof Wizard):LOWiz -> Wizard
def first_Wiz(loxiz):
    return loxiz.head
# ===============================
# (listof Wizard):LOWiz -> (listof Wizard):LOWiz
def rest_Wiz(loxiz):
    if loxiz is None or loxiz.head.next is None:
        return None
    else:
        new_lowiz = LOWiz(loxiz.head.next)
        return new_lowiz
# ===================
def last_wiz(head):
    if head.next is None:
        return head
    else:
        return last_wiz(head.next)
# ======
# (Listof Wizard) (Listof Wizard) -> (Listof Wizard)
def append_two_lists(low1, low2):
    if low2.head is None:
        return low1
    if low1.head is None:
        low1.head = low2.head
        return low1
    else:
        lastwiz = last_wiz(low1.head)
        lastwiz.next =  low2.head
        return low1
# ===========================================
def print_list(low):
    if low is None:
        print(' ')
        return None
    else:
        print(first_Wiz(low))
        print_list(rest_Wiz(low))

# ===================================
#
wa  = Wizard('A', 'S', None)
wb  = Wizard('B', 'G', None)
wc  = Wizard('C', 'R', None)
wd  = Wizard('D', 'H', None)
we  = Wizard('E', 'R', None)
# ===
wf_child = LOWiz()
wf_child.head = wb
wf  = Wizard('F', 'R', wf_child)
# ===
wg_child = LOWiz(wa)
wg  = Wizard('G', 'S', wg_child)
# ===
wh_child = LOWiz(wc)
wc.next = wd
wh  = Wizard('H', 'S', wh_child)
# ===
wi  = Wizard('I', 'H', None)
# ===
wj_child = LOWiz(we)
we.next = wf
wf.next = wg
wj = Wizard('J', 'R', wj_child)
# ===
wk_child = LOWiz(wh)
wh.next = wi
wi.next = wj
wk = Wizard('K', 'G', wk_child)
# ============================================
# # Template: mutual reference
# def fn_for_wiz(wizard):
#     def fn_for_wiz(wizard):
#         return ... wizard.name
#                    wizard.house
#                    fn_for_low(wizard.children)
#     def fn_for_low(low):
#         if low is None:
#             return ...
#         else:
#             return ...fn_for_wiz(first_X(low))
#                       fn_for_low(rest_lox(low))
#     return fn_for_wiz(wizard)
# ===============================================
# # Template with Accumulator
# def fn_for_wiz(wizard):
#     # acc<parent_house>: String
#     # invarian? ...
#     def fn_for_wiz(wizard, parent_house):
#         return ...parent_house
#                   wizard.name
#                   wizard.house
#                   fn_for_low(wizard.children, parent_house)
#     def fn_for_low(low, parent_house):
#         if low is None:
#             return ...parent_house
#         else:
#             return ...parent_house
#                       fn_for_wiz(first_X(low) , ...parent_house)
#                       fn_for_low(rest_lox(low), ...parent_house)
#     return fn_for_wiz(wizard, ...)
# ===============================================
# IMAGE:

                        #wk# K G

        #wh# H S        #wi# I H          #wj# J R

   #wc# C R   #wd# D H          #we# E R  #wf# F R   #wg# G S

                                          #wb# B G   #wa# A S
# ==
# print_list(append_two_lists(wj_child, wk_child))
