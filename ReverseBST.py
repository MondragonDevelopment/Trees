import numpy as np
import pandas as pd
from BinaryTree import *

"""
data = pd.read_csv('C:/Users/Fernando/Documents/Code/Python/Notebooks/data/Auto.csv')
print(data.columns)
print(data.describe)
"""
def invertTree(root):
    if not root: return
    dummy = TreeNode()
    if root.left or root.right:
        dummy.left = root.left
        root.left = root.right
        root.right = dummy.left
    invertTree(root.left)
    invertTree(root.right)
    return root

"""
values = np.array([10,6,8,7,9])
indices = np.argsort(values)
print(indices)
"""
