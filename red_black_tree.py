import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.color = 'red'

def RightRotate(X):
    Y = X.left
    X.left = Y.right
    if (Y.right != None):
        Y.right.parent = X
    Y.parent = X.parent
    if (X.parent == None):
        root = Y
    elif (X == X.parent.right):
        X.parent.right = Y
    else:
        X.parent.left = Y
    Y.right = X
    X.parent = Y

def LeftRotate(X):
    Y = X.right
    X.right = Y.left
    if (Y.left != None):
        Y.left.parent = X
    Y.parent = X.parent
    if (X.parent == None):
        root = Y
    elif (X == X.parent.left):
        X.parent.left = Y
    else:
        X.parent.right = Y
    Y.left = X
    X.parent = Y

def insert(node, key):
    new_node = Node(key)
    if node is None:
        new_node.color = 'black'
        return new_node
    elif node.key is None:
        node.key = key
        return node

    parent = None
    current = node
    while current is not None:
        parent = current
        if new_node.key < current.key:
            current = current.left
        else:
            current = current.right

    new_node.parent = parent
    if new_node.key < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node

    while (new_node != node and new_node.parent.color == 'red'):
        if (new_node.parent == new_node.parent.parent.right):
            u = new_node.parent.parent.left
            if u is None:
                u = Node(None)
                u.color = 'red'
            if (u.color == 'red'):
                u.color = 'black'
                new_node.parent.color = 'black'
                new_node.parent.parent.color = 'red'
                new_node = new_node.parent.parent
            else:
                if (new_node == new_node.parent.left):
                    new_node = new_node.parent
                    RightRotate(new_node)
                new_node.parent.color = 'black'
                new_node.parent.parent.color = 'red'
                LeftRotate(new_node.parent.parent)
        else:
            u = new_node.parent.parent.right
            if u is None:
                u = Node(None)
                u.color = 'red'
            if (u.color == 'red'):
                u.color = 'black'
                new_node.parent.color = 'black'
                new_node.parent.parent.color = 'red'
                new_node = new_node.parent.parent
            else:
                if (new_node == new_node.parent.right):
                    new_node = new_node.parent
                    LeftRotate(new_node)
                new_node.parent.color = 'black'
                new_node.parent.parent.color = 'red'
                RightRotate(new_node.parent.parent)
    node.color = 'black'
    return node

def search(node, key):
    while node is not None and node.key != key:
        if key < node.key:
            node = node.left
        else:
            node = node.right
    return node

x = random.sample(range(5000), 1000)
value = x[800]

root = None
for i in x:
    if root is None:
        root = Node(key=i)
        root.color = 'black'
    else:
        root = insert(root, key=i)

start = timer()
found = search(root, value)

print(timer() - start)

if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)
