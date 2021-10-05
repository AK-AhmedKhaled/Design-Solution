# Cyclic Data
# what about zork game?

# A  -> B -> C
# A  -> B, A -> C
# A <-> B -> C -> A

# Terminology:
# vertices: Nodes
# edges: connectors


# key Props?
# cycles: loops
# two pointers to same element

# SPecial Cases:
# Acyclic Graph: just one direction pipe!



class Room(object):
    def __init__(self, name='', exits=None):
        self.name   = name
        self.exits  = exits
        self.next   = None
        self.next2  = None

# Room is Room(String, Python<Listof Room>) # i smell Natural Recursion
# Interp. Room is a mystriey place we know its Name, just see its exists if there, entries is locked.
# Examples:

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
class LOR(object):
    def __init__(self, head=None, tail=None):
        if head is not None and head.next is None:
            head.next = tail
        if head is not None and tail is None:
            self.head = self.tail = head
        else:
            self.head = head
            self.tail = tail


# LOR is LOR(Room)
# Interp. holds the adress of a Room to be considered this LOR s head
# Examples:

# # Template:
# # it Assumes you pass a Non- None lor  # lor != None  lor.head may be None
# def fn_for_lor(lor):
#     if lor.head is None:
#         return ...
#     else:
#         return ...fn_for_room(first_r(lor))
#                   fn_for_lor(rest_rs(lor))

# Implementation:


# (listof Room) -> Room
# produce the room which head hold its ref.
def first_r(lor):
    return lor.head  # if lor.head is None or else
# ====
# (listof Room) -> (listof Room)
# produce a new LOR with its head to point to the very Same seond Room of a given (listof Room)
def rest_rs(lor):
    if lor.head is None:
        return None
    else:
        return LOR(lor.head.next)
# ====
# (listof Room) -> None
# Traversal just prints to console names of each Room
def print_labels(lor):
    if lor.head is None:
        print('')
    else:
         print(first_r(lor).name)
         print_labels(rest_rs(lor))
# SEE
# print_labels(Is)
# OK?
# ====
# (listof Room) -> (listof Room)
# return """same""" LOR but adjust its "tail" ref AND last Room next ref to point to the given room
# our implementation of tail omit the Natural Recursion!
def append_r(lor, room):
    if lor.head is None:
        lor.head = lor.tail = room
    else:
        lor.tail.next = room
        lor.tail = room
    return lor
# ====
# # Example
# III = Room('III')
# III.next = None
#
# II  = Room('II')
# II.next = III
#
# I   = Room('I')
# I.next = II
#
# Is = LOR(I, III)
# =
# Same Example: vai append_r
I     = Room('I')
II    = Room('II')
III   = Room('III')
Is = LOR()
append_r(Is, I)
append_r(Is, II)
Is_final = append_r(Is, III)
# print_labels(Is_final)  # OK
# ====
# (listof Room) String -> Boolean
# produce True if a given room s label is match a given name
# def is_here(lor, label):  # stub
#     return False
# Template is from LOR
# Added: parameter, label<String>
def is_here(lor, label):
    def matched(curr_room, label):
        return curr_room.name == label
    if lor.head is None:
        return False
    else:
        return matched(first_r(lor), label) or is_here(rest_rs(lor), label)

def is_here_test():
    assert is_here(Is, 'VI') == False
    assert is_here(Is, 'II') == True
# ============================================
# (listof Room) (listof Room) -> (listof Room)
# connect two todos
def preload_todo(todo1, todo2):
    if todo1.head is None:
        return todo2
    elif todo2.head is None:
        return todo1
    else:
        todo1.tail.next = todo2.head
        new_todo = LOR(todo1.head, todo2.tail)
        return new_todo
# ===
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================

# =======================================================================
class Graph(object):
    """docstring for Graph."""
    def __init__(self, start=None):
        self.start = start


# Racket Shared Expression in Python to construct cyclical Structure !??? by Me.
def make_graph(_A_=None, _B_=None, _C_=None, _D_=None, _E_=None, _F_=None):
    def make_graph(_A_, _B_, _C_, _D_, _E_, _F_, i):
        if i == 10:
            # return _A_, _B_, _C_, _D_, _E_, _F_
            return Graph(_A_)
        else:
            _A_ = Room('A', LOR(_B_, _D_))
            _B_ = Room('B', LOR(_C_, _E_))
            _C_ = Room('C', LOR(_B_))
            _D_ = Room('D', LOR(_E_))
            _E_ = Room('E', LOR(_F_))
            _F_ = Room('F', LOR())
            return make_graph(_A_, _B_, _C_, _D_, _E_, _F_, i+1)
    return make_graph(_A_, _B_, _C_, _D_, _E_, _F_, 0)


# _A_, _B_, _C_, _D_, _E_, _F_ = make_graph()
graph = make_graph()
# SEE
# print(graph.start.name)
# print(graph.start.exits.head.name)
# print(graph.start.exits.head.next.name)
# OK!
# ============================================

# Template for House Graphs:

# I can deduct requirements and their contributions to make reach Template
# at Design level Modeling, the Systematiclly turn it to code
# What a beautiful Design Course!

# Requirements:
# - Structural Mutual Recursion
# - Wrapped in locals and a trimpoline
# - Tail Recursive with WorkList accumulater
# - context preserving to prevent go into loops

# def fn_for_room(room):
#     # todo <listof Room> a work list accumulater
#     # visited <list of String> a context preserving accumulater, names of rooms already visited
#     def fn_for_room(room, todo, visited):
#         if is_member(visited, room.name):
#             return fn_for_lor(preload_todo(room.exits, todo, visited))
#         return fn_for_lor(preload_todo(room.exits, todo, apppend(visited, (room.name)) # room.name
#      def fn_for_lor(todo, visited):
#          if todo.head is None:
#              return ...
#          return fn_for_room(first_r(todo), rset_rs(todo), visited)
#     return fn_for_room(room, LOR(), LOX())



# ==
