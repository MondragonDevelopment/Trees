import numpy as np
import pandas as pd

"""
data = pd.read_csv('C:/Users/Fernando/Documents/Code/Python/Notebooks/data/Auto.csv')
print(data.columns)
print(data.describe)
"""

values = np.array([10,6,8,7,9])
indices = np.argsort(values)
print(indices)
