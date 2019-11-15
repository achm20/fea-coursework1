import global_stiffness_construct_frames_multiple as gscfm
import global_stiffness_matrices_frames as gsmf
import local_stiffness_matrices_frames_multiple as lsmfm
import nodes_and_elems as nae
import numpy as np
from numpy.linalg import inv

M = gscfm.M
M1 = np.delete(M, [0, 1, 2, 3, 4, 5, 9, 10, 11], 0)
M2 = np.delete(M1, [0, 1, 2, 3, 4, 5, 9, 10, 11], 1)


def f(x):
    Pinf = 0.59
    Vinf = 100
    Gammazero = 95.71
    b = 6
    return Pinf*Vinf*Gammazero*(1-((2*x/b)**2))**(1/2)


npe = lsmfm.npe
total_lift = 26655

if npe == 3:
    xinterval = 0.75
    t1_3_1 = f(3*xinterval)
    t2_4_1 = f(3*xinterval)
    t3 = f(2*xinterval)
    t3_4_1 = f(2*xinterval)
    t4 = f(2*xinterval)
    t3_5_1 = f(xinterval)
    t4_6_1 = f(xinterval)
    t5 = f(0)
    t5_6_1 = f(0)
    t6 = f(0)
    t5_7_1 = f(xinterval)
    t6_8_1 = f(xinterval)
    t7 = f(2*xinterval)
    t7_8_1 = f(2*xinterval)
    t8 = f(2*xinterval)
    t7_9_1 = f(3*xinterval)
    t8_10_1 = f(3*xinterval)

    f5yy = total_lift/((t1_3_1/t5) + (t2_4_1/t5) + (t3/t5) + (
            t3_4_1/t5) + (t4/t5) + (t3_5_1/t5) + (t4_6_1/t5) + (
                         t5_6_1/t5) + (t6/t5) + (t5_7_1/t5) + (
                         t6_8_1/t5) + (t7/t5) + (t7_8_1/t5) + (
                         t8/t5) + (t7_9_1/t5) + (t8_10_1/t5) + 1)

    f5y = f5yy - 1724
    f1_3_1y = (t1_3_1/t5)*f5yy - 1724
    f2_4_1y = (t2_4_1/t5)*f5yy
    f3y = (t3/t5)*f5yy - 1724
    f3_4_1y = (t3_4_1/t5)*f5yy
    f3_5_1y = (t3_5_1/t5)*f5yy - 1724
    f4y = (t4/t5)*f5yy
    f4_6_1y = (t4_6_1/t5)*f5yy
    f5_6_1y = (t5_6_1/t5)*f5yy
    f5_7_1y = (t5_7_1/t5)*f5yy - 1724
    f6y = (t6/t5)*f5yy
    f6_8_1y = (t6_8_1/t5)*f5yy
    f7y = (t7/t5)*f5yy - 1724
    f7_8_1y = (t7_8_1/t5)*f5yy
    f7_9_1y = (t7_9_1/t5)*f5yy - 1724
    f8y = (t8/t5)*f5yy
    f8_10_1y = (t8_10_1/t5)*f5yy
    f9y = 0
    f9_10_1y = 0
    f10y = 0

    f1_3_1x = 0
    f2_4_1x = 0
    f3x = 0
    f3_4_1x = 0
    f3_5_1x = 0
    f4x = 0
    f4_6_1x = 0
    f5x = 0
    f5_6_1x = 0
    f5_7_1x = 0
    f6x = 0
    f6_8_1x = 0
    f7x = 0
    f7_8_1x = 0
    f7_9_1x = 0
    f8x = 0
    f8_10_1x = 0
    f9x = 0
    f9_10_1x = 0
    f10x = 0

    m1_3_1 = 0
    m2_4_1 = 0
    m3 = 0
    m3_4_1 = 0
    m3_5_1 = 0
    m4 = 0
    m4_6_1 = 0
    m5 = 0
    m5_6_1 = 0
    m5_7_1 = 0
    m6 = 0
    m6_8_1 = 0
    m7 = 0
    m7_8_1 = 0
    m7_9_1 = 0
    m8 = 0
    m8_10_1 = 0
    m9 = 0
    m9_10_1 = 0
    m10 = 0

#Global displacement calcs
F = np.array([f1_3_1x, f1_3_1y, m1_3_1, f2_4_1x, f2_4_1y, m2_4_1,
              f3x, f3y, m3, f3_4_1x, f3_4_1y, m3_4_1, f3_5_1x, f3_5_1y,
              m3_5_1,  f4x, f4y, m4, f4_6_1x, f4_6_1y, m4_6_1, f5x,
              f5y, m5, f5_6_1x, f5_6_1y, m5_6_1, f5_7_1x, f5_7_1y,
              m5_7_1, f6x, f6y, m6, f6_8_1x, f6_8_1y, m6_8_1, f7x,
              f7y, m7, f7_8_1x, f7_8_1y, m7_8_1, f7_9_1x, f7_9_1y,
              m7_9_1, f8x, f8y, m8, f8_10_1x, f8_10_1y, m8_10_1,
              f9x, f9y, m9, f9_10_1x, f9_10_1y, m9_10_1, f10x,
              f10y, m10]).reshape((60, 1))

M3 = inv(M2)
D = np.matmul(M3, F)
print(D)

#--------------------------------------------------------------------
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
global_disp_vector_el7 = np.array([D[6, 0], D[7, 0], D[8, 0], D[9,
                                                                0],
                                   D[10, 0], D[11, 0]])
T_global_disp_vector_el7 = np.array(
    global_disp_vector_el7).reshape(6, 1)
local_disp_el7 = np.matmul(gsmf.Transform7, T_global_disp_vector_el7)


#Element 8
global_disp_vector_el8 = np.array([D[6, 0], D[7, 0], D[8, 0], D[12,
                                                                0],
                                   D[13, 0], D[14, 0]])
T_global_disp_vector_el8 = np.array(
    global_disp_vector_el8).reshape(6, 1)
local_disp_el8 = np.matmul(gsmf.Transform8, T_global_disp_vector_el8)


#Element 9
global_disp_vector_el9 = np.array([D[9, 0], D[10, 0], D[11, 0], D[15,
                                                                0],
                                   D[16, 0], D[17, 0]])
T_global_disp_vector_el9 = np.array(
    global_disp_vector_el9).reshape(6, 1)
local_disp_el9 = np.matmul(gsmf.Transform9, T_global_disp_vector_el9)


#Element 10
global_disp_vector_el10 = np.array([D[12, 0], D[13, 0], D[14, 0],
                                    D[15,
                                                                0],
                                   D[16, 0], D[17, 0]])
T_global_disp_vector_el10 = np.array(
    global_disp_vector_el10).reshape(6, 1)
local_disp_el10 = np.matmul(gsmf.Transform10,
                            T_global_disp_vector_el10)


#Element 11
global_disp_vector_el11 = np.array([D[12, 0], D[13, 0], D[14, 0],
                                    D[18,
                                                                0],
                                   D[19, 0], D[20, 0]])
T_global_disp_vector_el11 = np.array(
    global_disp_vector_el11).reshape(6, 1)
local_disp_el11 = np.matmul(gsmf.Transform11,
                            T_global_disp_vector_el11)


#Element 12
global_disp_vector_el12 = np.array([D[15, 0], D[16, 0], D[17, 0],
                                    D[21,
                                                                0],
                                   D[22, 0], D[23, 0]])
T_global_disp_vector_el12 = np.array(
    global_disp_vector_el12).reshape(6, 1)
local_disp_el12 = np.matmul(gsmf.Transform12,
                            T_global_disp_vector_el12)


#Element 13
global_disp_vector_el13 = np.array([D[18, 0], D[19, 0], D[20, 0],
                                    D[21,
                                                                0],
                                   D[22, 0], D[23, 0]])
T_global_disp_vector_el13 = np.array(
    global_disp_vector_el13).reshape(6, 1)
local_disp_el13 = np.matmul(gsmf.Transform13,
                            T_global_disp_vector_el13)

#--------------------------------------------------------------------
#Element Strain calcs

#Element 2 strain
e_el2 = (local_disp_el2[3, 0] - local_disp_el2[0, 0])/nae.Elem_2[
    'length']


#Element 3 strain
e_el3 = (local_disp_el3[3, 0] - local_disp_el3[0, 0])/nae.Elem_3[
    'length']


#Element 4 strain
e_el4 = (local_disp_el4[3, 0] - local_disp_el4[0, 0])/nae.Elem_4[
    'length']


#Element 5 strain
e_el5 = (local_disp_el5[3, 0] - local_disp_el5[0, 0])/nae.Elem_5[
    'length']


#Element 6 strain
e_el6 = (local_disp_el6[3, 0] - local_disp_el6[0, 0])/nae.Elem_6[
    'length']


#Element 7 strain
e_el7 = (local_disp_el7[3, 0] - local_disp_el7[0, 0])/nae.Elem_7[
    'length']


#Element 8 strain
e_el8 = (local_disp_el8[3, 0] - local_disp_el8[0, 0])/nae.Elem_8[
    'length']


#Element 9 strain
e_el9 = (local_disp_el9[3, 0] - local_disp_el9[0, 0])/nae.Elem_9[
    'length']


#Element 10 strain
e_el10 = (local_disp_el10[3, 0] - local_disp_el10[0, 0])/nae.Elem_10[
    'length']


#Element 11 strain
e_el11 = (local_disp_el11[3, 0] - local_disp_el11[0, 0])/nae.Elem_11[
    'length']


#Element 12 strain
e_el12 = (local_disp_el12[3, 0] - local_disp_el12[0, 0])/nae.Elem_12[
    'length']


#Element 13 strain
e_el13 = (local_disp_el13[3, 0] - local_disp_el13[0, 0])/nae.Elem_13[
    'length']

a = 1