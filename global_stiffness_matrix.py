import nodes_and_elems as nae
import local_stiffness_matrices as lsm
import numpy as np

M = np.zeros((20,20))
M[:4, :4] += lsm.k1
M[np.ix_([0, 1, 4, 5], [0, 1, 4, 5])] += lsm.k2
M[np.ix_([2, 3, 6, 7], [2, 3, 6, 7])] += lsm.k3
M[4:8, 4:8] += lsm.k4
M[np.ix_([4, 5, 8, 9], [4, 5, 8, 9])] += lsm.k5
M[np.ix_([6, 7, 10, 11], [6, 7, 10, 11])] += lsm.k6
M[8:12, 8:12] += lsm.k7
M[np.ix_([8, 9, 12, 13], [8, 9, 12, 13])] += lsm.k8
M[np.ix_([10, 11, 14, 15], [10, 11, 14, 15])] += lsm.k9
M[12:16, 12:16] += lsm.k10
M[np.ix_([12, 13, 16, 17], [12, 13, 16, 17])] += lsm.k11
M[np.ix_([14, 15, 18, 19], [14, 15, 18, 19])] += lsm.k12
M[16:20, 16:20] += lsm.k13

print(M)
