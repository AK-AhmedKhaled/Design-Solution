import sys
sys.path.append('../HtDD')
from generic_list_last_try import *
from graph import *

# Design a function that consumes a Starting 'Room' and a given label
# and Produces True if it possible to reach the Room of that given label
# from the point of that Room

# Room String -> Boolean

# consumes: a Starting 'Room' and a given label, and
# Produces True if it possible to reach the Room of that given label
# from the starting point 'that Room'

# def is_reachable(room, label):  # stub
#     return False

# the most beatiful Template ever! from House Graph
def is_reachable(room, label):
    # todo <listof Room> a work list accumulater
    # visited <list of String> a context preserving accumulater, names of rooms already visited
    def fn_for_room(room, todo, visited):
        # print_labels(room.exits)

        if room.name == label:
            return True
        elif is_member(visited, room.name):
            return fn_for_lor(todo, visited)
        else:
            return fn_for_lor(preload_todo(room.exits, todo), apppend(visited, room.name))
    def fn_for_lor(todo, visited):
        # print('visited:')
        # print_Xs(visited)
        # print('todo:')
        # print_labels(todo)
        if todo.head is None:
            return False
        else:
            return fn_for_room(first_r(todo), rest_rs(todo), visited)
    return fn_for_room(room, LOR(), LOX())


def is_reachable_test():
    assert is_reachable(graph.start.exits.head, 'F') == True
    assert is_reachable(graph.start.exits.head, 'D') == False  # from B reach 'D'?
    assert is_reachable(graph.start, 'F') == True
    # # DEBUG:  after that runs Vertix B will have exits _C_ _E_ _D_ where _D_ comes from?
    # assert is_reachable(graph.start.exits.head, 'D') == False  # from B reach 'D'?


# ==
if __name__ == '__main__':
    is_reachable_test()
    print('All Tests passed!')

# ==
