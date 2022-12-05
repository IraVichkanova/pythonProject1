import numpy as np
np.warnings.filterwarnings('ignore')

A1 = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
A4 = np.array([2, 5, 11])

print(np.linalg.lstsq(A1, A4))







