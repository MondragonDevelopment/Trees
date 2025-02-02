class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
def insert(node, val, left):
    if node is None: return TreeNode(val)
    #if node.val == val: return node 
    if left == True:
        node.left = insert(node.left, val)
    else: 
        node.right = insert(node.right, val)
    return node
"""