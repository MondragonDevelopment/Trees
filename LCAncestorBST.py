from BSTNode import *

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def search(node, root, stack):
        stack.append(root)
        if node.val == root.val: return
        elif node.val < root.val: search(node, root.left, stack)
        else: search(node, root.right, stack)
    
    l1, l2 = [], []
    search(p, root, l1)
    search(q, root, l2)

    print(len(l1), len(l2))
    res = root
    while l1 and l2:
        curr = l1.pop(0)
        print(curr.val)
        if curr.val == l2.pop(0).val:
            res = curr
        else: break
    return res

if __name__ == '__main__':
    r = construct([6,2,8,0,4,7,9,3,5])
    p = search(r, 2)
    q = search(r, 4)
    print(lowestCommonAncestor(r, p, q).val)
