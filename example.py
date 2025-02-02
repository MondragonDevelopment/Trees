from BST import *

values = [10,5,15,2,5,13,22,1,14]
T = Tree()

for i in range(len(values)):
    T[i] = values[i]

def traverse(tree):
    n = 0
    while n in tree:
        print(tree[n])
        n += 1
    

traverse(T)
