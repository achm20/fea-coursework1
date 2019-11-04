import global_stiffness_matrix as gsm
import numpy as np

d1x = 0
d2x = 0
d3x = 0
d4x = 0
d5x = 0
d6x = 0
d7x = 0
d8x = 0
d9x = 0
d10x = 0
d1y = 0
d2y = 0

M = gsm.M
M1 = np.delete(M, [0, 1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18], 0)
M2 = np.delete(M1, [0, 1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18], 1)

#Nodal Force Vector
f3y = 1000
f4y = 1000
f5y = 2000 - 6000
f6y = 2000
f7y = 1000
f8y = 1000
f9y = 0
f10y = 0

F = np.array([f3y, f4y, f5y, f6y, f7y, f8y, f9y, f10y])
a=1
