from BinaryTree import *

def nodeDepth(node, depth=0):
    if not node: return 0
    return depth + nodeDepth(node.left, depth + 1) + nodeDepth(node.right, depth + 1)

def numb(node):
    if not node: return 0
    return 1 + numb(node.left) + numb(node.right)

if __name__ == '__main__':
    nodes = [TreeNode(x) for x in range(1, 11)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[3].left = nodes[7]
    nodes[3].right = nodes[8]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]

    r = nodes[0]
    print(nodeDepth(r))
    print(numb(r))
