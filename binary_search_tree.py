import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self, key, parent = None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def insert(node, key):
    if node is None: node = Node(key)
    elif key < node.key: node.left = insert(node.left, key)
    else: node.right = insert(node.right, key)
    return node

def search(node, key):
    if node is None or node.key == key: return node
    if key < node.key: return search(node.left, key)
    return search(node.right, key)

def delete_node(node):
    if node.left == None and node.right == None:
        return None
    elif node.left != None and node.right == None:
        return node.left
    elif node.right != None and node.left != None:
        return node.right
    else:
        s = node.right
        while s.left != None:
            node.parent = s
            s = s.left
        node.key = s.key
        if s == node.right:
            node.right = s.right
        else:
            node.parent.left = s.right
        return node

def delete(node):
    if node.parent == None:
        node = delete_node(node)
    elif node == node.parent.left:
        node.parent.left = delete_node(node)
    else:
        node.parent.right = delete_node(node)

x = random.sample(range(5000), 1000)
value = x[800]

root = None
for i in x:
    root = insert(root, i)

start = timer()
found = search(root, value)

print(timer() - start)

if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)
