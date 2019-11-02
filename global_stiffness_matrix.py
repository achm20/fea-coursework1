import nodes_and_elems as nae
import local_stiffness_matrices as lsm
import numpy as np

M = np.zeros((6,6))
M[:4, :4] += lsm.k1
M[np.ix_([0, 1, 4, 5], [0, 1, 4, 5])] += lsm.k2
M[np.ix_([2, 3, 6, 7], [2, 3, 6, 7])] += lsm.k3
M[] +=lsm.k4

print(M)

#M[:2,:2] += M1
#M[1:3, 1:3] += M2

