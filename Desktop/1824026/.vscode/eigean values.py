import numpy as np
from numpy.linalg import eig
a = np.array([[0, 2], 
              [2, 3]])
w,v=eig(a)
print('E-value:', w)
print('E-vector', v)
E-value: [-1.  4.]
E-vector [[-0.89442719 -0.4472136 ]
 [ 0.4472136  -0.89442719]]
 a = np.array([[2, 2, 4], 
              [1, 3, 5],
              [2, 3, 4]])
w,v=eig(a)
print('E-value:', w)
print('E-vector', v)