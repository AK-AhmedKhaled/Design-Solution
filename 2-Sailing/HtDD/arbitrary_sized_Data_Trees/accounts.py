# Binary Search Tree
# Design a data definition to represent binary search trees

# node Data Definitions
class Account(object):
    def __init__(self, id, name):
        self.id   = id
        self.name = name
        self.left = None # pointer to BST
        self.right= None # pointer to BST

# Data Examples
account1 = new Account(  1, 'Ahmed Khaled')
account2 = new Account( 99, 'Bahaa')
account3 = new Account( 12, 'Magdy')
account4 = new Account(111, 'Ramez')
account5 = new Account( 38, 'Fahmy')
account6 = new Account( 73, 'Mourad')
account7 = new Account( 52, 'Beka')





# 1- define possible structure
class Accounts(object):
    def __init__(self, account):
        self.root = account


# 2- data definition

# Accounts is one-of:
    # - None  # empty tree
    # - (account left(Accounts) right(Accounts))


#  3- Interpretation.. None means empty BST (no node at all holding left and rigth BST)
#                    if not None, so there exist at least a 'node' = new account(id, String) with Accounts and Accounts:
#                             - id: account number
#                             - String: account name
#                             - Accounts <first argument> : left BST
#                             - Accounts <second argument>: right BST


# 4- Invariants:.. for a given node = new account(key, String)
#       - its key is greater than all the keys at the left  of it
#       - its key is smaller than all the keys at the right of it
#       - implicitely, the key is unique can not apear twice


# 5- Data Examples
BSTree0  = Accounts(None)
BSTree1  = Accounts(account1) # completely un balancd BST
BSTree3  = Accounts(account3) # balanced for the given set but after many..tons of additions ?



# 6- Data Driven Template
def fn_for_BST(bst):
    if bst is None:
        ...
    else:
        fn_for_Account(bst.root)
        fn_for_BST(bst.root.left)
        fn_for_BST(bst.root.right)
# ; Template Rules used:
# ;    one of:
# ;     - atomic ditinct: None
# ;     - compound: Account(Natural String LBST RBST)
# ;     - self-reference: LBST is BST
# ;     - self-reference: RBST is BST
