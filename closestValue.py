from BSTNode import *

def findClosestVal(tree, target):
    res = float("inf")
    while tree:
        if tree.val == target:
            return target
        if abs(tree.val - target) < abs(res - target):
            res = tree.val
        if target < tree.val:
            tree = tree.left
        else:
            tree = tree.right
    return res

def findClosestVal2(node, target, closest = float('inf')):
    if node:
        closest = node.val if abs(node.val - target) < abs(closest - target) else closest
        if target < node.val: return findClosestVal2(node.left, target, closest)
        else: return findClosestVal2(node.right, target, closest)
    else: return closest

if __name__ == '__main__':
    v = [10,5,2,1,5,15,13,14,22]
    r = construct(v)

    print(search(r, 12))
    print(findClosestVal(r, 11))
    print(findClosestVal2(r, 7))
