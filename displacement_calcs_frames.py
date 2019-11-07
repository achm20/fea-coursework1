import global_stiffness_construct_frames as gscf
import global_stiffness_matrices_frames as gsmf
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
#print(D)

#Local displacement calcs

#Element 2
global_disp_vector_el2 = np.array([0, 0, 0, D[0, 0], D[1, 0], D[2,
                                                                0]])
T_global_disp_vector_el2 = np.array(
    global_disp_vector_el2).reshape(6, 1)
local_disp_el2 = np.matmul(gsmf.Transform2, T_global_disp_vector_el2)


#Element 3
global_disp_vector_el3 = np.array([0, 0, 0, D[3, 0], D[4, 0], D[5,
                                                                0]])
T_global_disp_vector_el3 = np.array(
    global_disp_vector_el3).reshape(6, 1)
local_disp_el3 = np.matmul(gsmf.Transform3, T_global_disp_vector_el3)


#Element 4
global_disp_vector_el4 = np.array([D[0, 0], D[1, 0], D[2, 0], D[3,
                                                                0],
                                   D[4, 0], D[5, 0]])
T_global_disp_vector_el4 = np.array(
    global_disp_vector_el4).reshape(6, 1)
local_disp_el4 = np.matmul(gsmf.Transform4, T_global_disp_vector_el4)


#Element 5
global_disp_vector_el5 = np.array([D[0, 0], D[1, 0], D[2, 0], D[6,
                                                                0],
                                   D[7, 0], D[8, 0]])
T_global_disp_vector_el5 = np.array(
    global_disp_vector_el5).reshape(6, 1)
local_disp_el5 = np.matmul(gsmf.Transform5, T_global_disp_vector_el5)


#Element 6
global_disp_vector_el6 = np.array([D[3, 0], D[4, 0], D[5, 0], D[9,
                                                                0],
                                   D[10, 0], D[11, 0]])
T_global_disp_vector_el6 = np.array(
    global_disp_vector_el6).reshape(6, 1)
local_disp_el6 = np.matmul(gsmf.Transform6, T_global_disp_vector_el6)


#Element 7
global_disp_vector_el5 = np.array([D[0, 0], D[1, 0], D[2, 0], D[6,
                                                                0],
                                   D[7, 0], D[8, 0]])
T_global_disp_vector_el5 = np.array(
    global_disp_vector_el5).reshape(6, 1)
local_disp_el5 = np.matmul(gsmf.Transform5, T_global_disp_vector_el5)


#Element 8
global_disp_vector_el5 = np.array([D[0, 0], D[1, 0], D[2, 0], D[6,
                                                                0],
                                   D[7, 0], D[8, 0]])
T_global_disp_vector_el5 = np.array(
    global_disp_vector_el5).reshape(6, 1)
local_disp_el5 = np.matmul(gsmf.Transform5, T_global_disp_vector_el5)


#Element 9
global_disp_vector_el5 = np.array([D[0, 0], D[1, 0], D[2, 0], D[6,
                                                                0],
                                   D[7, 0], D[8, 0]])
T_global_disp_vector_el5 = np.array(
    global_disp_vector_el5).reshape(6, 1)
local_disp_el5 = np.matmul(gsmf.Transform5, T_global_disp_vector_el5)


#Element 10
global_disp_vector_el5 = np.array([D[0, 0], D[1, 0], D[2, 0], D[6,
                                                                0],
                                   D[7, 0], D[8, 0]])
T_global_disp_vector_el5 = np.array(
    global_disp_vector_el5).reshape(6, 1)
local_disp_el5 = np.matmul(gsmf.Transform5, T_global_disp_vector_el5)


#Element 11
global_disp_vector_el5 = np.array([D[0, 0], D[1, 0], D[2, 0], D[6,
                                                                0],
                                   D[7, 0], D[8, 0]])
T_global_disp_vector_el5 = np.array(
    global_disp_vector_el5).reshape(6, 1)
local_disp_el5 = np.matmul(gsmf.Transform5, T_global_disp_vector_el5)


#Element 12
global_disp_vector_el5 = np.array([D[0, 0], D[1, 0], D[2, 0], D[6,
                                                                0],
                                   D[7, 0], D[8, 0]])
T_global_disp_vector_el5 = np.array(
    global_disp_vector_el5).reshape(6, 1)
local_disp_el5 = np.matmul(gsmf.Transform5, T_global_disp_vector_el5)


#Element 13
global_disp_vector_el5 = np.array([D[0, 0], D[1, 0], D[2, 0], D[6,
                                                                0],
                                   D[7, 0], D[8, 0]])
T_global_disp_vector_el5 = np.array(
    global_disp_vector_el5).reshape(6, 1)
local_disp_el5 = np.matmul(gsmf.Transform5, T_global_disp_vector_el5)


print(D)
a = 1