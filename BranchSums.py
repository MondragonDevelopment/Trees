from BinaryTree import *

def branchsums(node, result = 0, sums = []):
    if not node: return
    
    result += node.val
    if not node.left and not node.right:
        sums = sums.append(result)
        return
    
    branchsums(node.left, result, sums)
    branchsums(node.right, result, sums)
    return sums


if __name__ == '__main__':
    nodes = [TreeNode(x) for x in range(1, 11)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[3].left = nodes[7]
    nodes[3].right = nodes[8]
    nodes[4].left = nodes[9]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    root = nodes[0]
    #print(root.left.right.val)
    print(branchsums(root))
