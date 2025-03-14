from BSTNode import *


def isSameTree(p, q) -> bool:
        if (not p and q) or (not q and p): return False
        elif not p and not q: return True
        if p.val != q.val: return False

        return True if isSameTree(p.left, q.left) and isSameTree(p.right, q.right) else False

def sameTree(p,q):
        if not p and not q: return True
        if p and q and p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        return False

if __name__ == '__main__':
        p5 = TreeNode(2)
        p4 = TreeNode(2, p5)
        p3 = TreeNode(2)
        p2 = TreeNode(2, None, p4)
        p = TreeNode(2, p2, p3)

        q5 = TreeNode(2)
        q4 = TreeNode(2)
        q3 = TreeNode(2, q5)
        q2 = TreeNode(2, q4)
        q = TreeNode(2, q2, q3)

        print(isSameTree(p,q))
        print(sameTree(p, q))
        