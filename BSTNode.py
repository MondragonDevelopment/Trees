class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(node, val):
    if node is None: return TreeNode(val)
    #if node.val == val: return node 
    if val < node.val:
        node.left = insert(node.left, val)
    else: 
        node.right = insert(node.right, val)
    return node

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val, end = ' ')
        inOrder(root.right)

def construct(values):
    r = TreeNode(values.pop(0))
    for num in values:
        r = insert(r, num)
    return r

def search(node, val):
    if node is None: return False
    if node.val == val: return True
    elif val < node.val: return search(node.left, val)
    else: return search(node.right, val)
