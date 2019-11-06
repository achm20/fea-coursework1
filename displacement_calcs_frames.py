import global_stiffness_construct_frames as gscf
import numpy as np
from numpy.linalg import inv

d1x = 0
d2x = 0
d1y = 0
d2y = 0
phi1 = 0
phi2 = 0

M = gscf.M
M1 = np.delete(M, [0, 1, 2, 3, 4, 5], 0)
M2 = np.delete(M1, [0, 1, 2, 3, 4, 5], 1)

def f(x):
    Pinf = 0.59
    Vinf = 100
    Gammazero = 95.71
    b = 6
    return Pinf*Vinf*Gammazero*(1-((2*x/b)**2))**(1/2)

f3y = f(-1.5) -8010
f4y = f(-1.5)
f5y = f(0) - 8010
f6y = f(0)
f7y = f(1.5) - 8010
f8y = f(1.5)
f9y = 0
f10y = 0
f3x = 0
f4x = 0
f5x = 0
f6x = 0
f7x = 0
f8x = 0
f9x = 0
f10x = 0
m3 = 0
m4 = 0
m5 = 0
m6 = 0
m7 = 0
m8 = 0
m9 = 0
m10 = 0

#Global displacement calcs
F = np.array([f3x, f3y, m3, f4x, f4y, m4, f5x, f5y, m5, f6x, f6y,
              m6, f7x, f7y, m7, f8x, f8y, m8, f9x, f9y, m9, f10x,
              f10y, m10]).reshape((24, 1))

M3 = inv(M2)
D = np.matmul(M3, F)
print(D)

#Local displacement calcs


a = 1