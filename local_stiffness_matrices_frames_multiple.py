import nodes_and_elems_multiple as naem
import numpy as np
npe = 5

E = 73.1*(10**9)
poisson = 0.33
A = 4*(10**-4)
b = 0.02
d = 0.02
I = (b*d**3)/12
L = 1.5
G = 28*(10**9) #shear modulus
ks = 5/6 #Timoshenko shear coefficient
g = (E*I)/(G*ks*A)

#--------------------------------------------------------------------

#ELEMENT LENGTHS FOR DIFFERENT NUMBER OF NODES PER ELEMENT
if npe == 3:
    length1 = naem.Length_Elem_1_el['nodes_per_el_3']['length']
    length2 = naem.Length_Elem_2_el['nodes_per_el_3']['length']
    length3 = naem.Length_Elem_3_el['nodes_per_el_3']['length']
    length4 = naem.Length_Elem_4_el['nodes_per_el_3']['length']
    length5 = naem.Length_Elem_5_el['nodes_per_el_3']['length']
    length6 = naem.Length_Elem_6_el['nodes_per_el_3']['length']
    length7 = naem.Length_Elem_7_el['nodes_per_el_3']['length']
    length8 = naem.Length_Elem_8_el['nodes_per_el_3']['length']
    length9 = naem.Length_Elem_9_el['nodes_per_el_3']['length']
    length10 = naem.Length_Elem_10_el['nodes_per_el_3']['length']
    length11 = naem.Length_Elem_11_el['nodes_per_el_3']['length']
    length12 = naem.Length_Elem_12_el['nodes_per_el_3']['length']
    length13 = naem.Length_Elem_13_el['nodes_per_el_3']['length']

elif npe == 4:
    length1 = naem.Length_Elem_1_el['nodes_per_el_4']['length']
    length2 = naem.Length_Elem_2_el['nodes_per_el_4']['length']
    length3 = naem.Length_Elem_3_el['nodes_per_el_4']['length']
    length4 = naem.Length_Elem_4_el['nodes_per_el_4']['length']
    length5 = naem.Length_Elem_5_el['nodes_per_el_4']['length']
    length6 = naem.Length_Elem_6_el['nodes_per_el_4']['length']
    length7 = naem.Length_Elem_7_el['nodes_per_el_4']['length']
    length8 = naem.Length_Elem_8_el['nodes_per_el_4']['length']
    length9 = naem.Length_Elem_9_el['nodes_per_el_4']['length']
    length10 = naem.Length_Elem_10_el['nodes_per_el_4']['length']
    length11 = naem.Length_Elem_11_el['nodes_per_el_4']['length']
    length12 = naem.Length_Elem_12_el['nodes_per_el_4']['length']
    length13 = naem.Length_Elem_13_el['nodes_per_el_4']['length']

else:
    length1 = naem.Length_Elem_1_el['nodes_per_el_5']['length']
    length2 = naem.Length_Elem_2_el['nodes_per_el_5']['length']
    length3 = naem.Length_Elem_3_el['nodes_per_el_5']['length']
    length4 = naem.Length_Elem_4_el['nodes_per_el_5']['length']
    length5 = naem.Length_Elem_5_el['nodes_per_el_5']['length']
    length6 = naem.Length_Elem_6_el['nodes_per_el_5']['length']
    length7 = naem.Length_Elem_7_el['nodes_per_el_5']['length']
    length8 = naem.Length_Elem_8_el['nodes_per_el_5']['length']
    length9 = naem.Length_Elem_9_el['nodes_per_el_5']['length']
    length10 = naem.Length_Elem_10_el['nodes_per_el_5']['length']
    length11 = naem.Length_Elem_11_el['nodes_per_el_5']['length']
    length12 = naem.Length_Elem_12_el['nodes_per_el_5']['length']
    length13 = naem.Length_Elem_13_el['nodes_per_el_5']['length']

k_rod1 = A*E/length1
k_rod2 = A*E/length2
k_rod3 = A*E/length3
k_rod4 = A*E/length4
k_rod5 = A*E/length5
k_rod6 = A*E/length6
k_rod7 = A*E/length7
k_rod8 = A*E/length8
k_rod9 = A*E/length9
k_rod10 = A*E/length10
k_rod11 = A*E/length11
k_rod12 = A*E/length12
k_rod13 = A*E/length13

k_beam1 = E*I/length1**3
k_beam2 = E*I/length2**3
k_beam3 = E*I/length3**3
k_beam4 = E*I/length4**3
k_beam5 = E*I/length5**3
k_beam6 = E*I/length6**3
k_beam7 = E*I/length7**3
k_beam8 = E*I/length8**3
k_beam9 = E*I/length9**3
k_beam10 = E*I/length10**3
k_beam11 = E*I/length11**3
k_beam12 = E*I/length12**3
k_beam13 = E*I/length13**3

#if s = 1, then local stiffness matrices for bernoulli beam frame
# is used
#if s = 2, then local stiffness matrices for timoshenko beam frame
# is used

s = 2
if s == 1:
    k_frame_local_1 = [[k_rod1, 0, 0, -k_rod1, 0, 0],
                        [0, 12*k_beam1, 6*length1*k_beam1, 0, -12*k_beam1,
                         6*length1*k_beam1],
                        [0, 6*length1*k_beam1, 4*(length1**2)*k_beam1, 0,
                         -6*length1*k_beam1, 2*(length1**2)*k_beam1],
                        [-k_rod1, 0, 0, k_rod1, 0, 0],
                        [0, -12*k_beam1, -6*length1*k_beam1, 0, 12*k_beam1,
                         -6*length1*k_beam1],
                        [0, 6*length1*k_beam1, 2*(length1**2)*k_beam1, 0,
                         -6*length1*k_beam1, 4*(length1**2)*k_beam1]]
if s == 1:
    k_frame_local_2 = [[k_rod2, 0, 0, -k_rod2, 0, 0],
                   [0, 12 * k_beam2, 6 * length2 * k_beam2, 0, -12 * k_beam2,
                    6 * length2 * k_beam2],
                   [0, 6 * length2 * k_beam2, 4 * (
                           length2 ** 2) * k_beam2, 0,
                    -6 * length2 * k_beam2, 2 * (
                            length2 ** 2) * k_beam2],
                   [-k_rod2, 0, 0, k_rod2, 0, 0],
                   [0, -12 * k_beam2, -6 * length2 * k_beam2, 0, 12 * k_beam2,
                    -6 * length2 * k_beam2],
                   [0, 6 * length2 * k_beam2, 2 * (length2 ** 2) *
                    k_beam2, 0,
                    -6 * length2 * k_beam2, 4 * (length2 ** 2) *
                    k_beam2]]
if s == 1:
    k_frame_local_3 = [[k_rod3, 0, 0, -k_rod3, 0, 0],
            [0, 12 * k_beam3, 6 * length3 * k_beam3, 0, -12 * k_beam3,
            6 * length3 * k_beam3],
            [0, 6 * length3 * k_beam3, 4 * (
            length3 ** 2) * k_beam3, 0,
            -6 * length3 * k_beam3, 2 * (
            length3 ** 2) * k_beam3],
            [-k_rod3, 0, 0, k_rod3, 0, 0],
            [0, -12 * k_beam3, -6 * length3 * k_beam3, 0, 12 * k_beam3,
            -6 * length3 * k_beam3],
            [0, 6 * length3 * k_beam3, 2 * (length3 ** 2) *
            k_beam3, 0,
            -6 * length3 * k_beam3, 4 * (length3 ** 2) *
            k_beam3]]
if s == 1:
    k_frame_local_4 = [[k_rod4, 0, 0, -k_rod4, 0, 0],
            [0, 12 * k_beam4, 6 * length4 * k_beam4, 0, -12 * k_beam4,
            6 * length4 * k_beam4],
            [0, 6 * length4 * k_beam4, 4 * (
            length4 ** 2) * k_beam4, 0,
            -6 * length4 * k_beam4, 2 * (
            length4 ** 2) * k_beam4],
            [-k_rod4, 0, 0, k_rod4, 0, 0],
            [0, -12 * k_beam4, -6 * length4 * k_beam4, 0, 12 * k_beam4,
            -6 * length4 * k_beam4],
            [0, 6 * length4 * k_beam4, 2 * (length4 ** 2) *
            k_beam4, 0,
            -6 * length4 * k_beam4, 4 * (length4 ** 2) *
            k_beam4]]
if s == 1:
    k_frame_local_5 = [[k_rod5, 0, 0, -k_rod5, 0, 0],
            [0, 12 * k_beam5, 6 * length5 * k_beam5, 0, -12 * k_beam5,
            6 * length5 * k_beam5],
            [0, 6 * length5 * k_beam5, 4 * (
            length5 ** 2) * k_beam5, 0,
            -6 * length5 * k_beam5, 2 * (
            length5 ** 2) * k_beam5],
            [-k_rod5, 0, 0, k_rod5, 0, 0],
            [0, -12 * k_beam5, -6 * length5 * k_beam5, 0, 12 * k_beam5,
            -6 * length5 * k_beam5],
            [0, 6 * length5 * k_beam5, 2 * (length5 ** 2) *
            k_beam5, 0,
            -6 * length5 * k_beam5, 4 * (length5 ** 2) *
            k_beam5]]
if s == 1:
    k_frame_local_6 = [[k_rod6, 0, 0, -k_rod6, 0, 0],
            [0, 12 * k_beam6, 6 * length6 * k_beam6, 0, -12 * k_beam6,
            6 * length6 * k_beam6],
            [0, 6 * length6 * k_beam6, 4 * (
            length6 ** 2) * k_beam6, 0,
            -6 * length6 * k_beam6, 2 * (
            length6 ** 2) * k_beam6],
            [-k_rod6, 0, 0, k_rod6, 0, 0],
            [0, -12 * k_beam6, -6 * length6 * k_beam6, 0, 12 * k_beam6,
            -6 * length6 * k_beam6],
            [0, 6 * length6 * k_beam6, 2 * (length6 ** 2) *
            k_beam6, 0,
            -6 * length6 * k_beam6, 4 * (length6 ** 2) *
            k_beam6]]
if s == 1:
    k_frame_local_7 = [[k_rod7, 0, 0, -k_rod7, 0, 0],
            [0, 12 * k_beam7, 6 * length7 * k_beam7, 0, -12 * k_beam7,
            6 * length7 * k_beam7],
            [0, 6 * length7 * k_beam7, 4 * (
            length7 ** 2) * k_beam7, 0,
            -6 * length7 * k_beam7, 2 * (
            length7 ** 2) * k_beam7],
            [-k_rod7, 0, 0, k_rod7, 0, 0],
            [0, -12 * k_beam7, -6 * length7 * k_beam7, 0, 12 * k_beam7,
            -6 * length7 * k_beam7],
            [0, 6 * length7 * k_beam7, 2 * (length7 ** 2) *
            k_beam7, 0,
            -6 * length7 * k_beam7, 4 * (length7 ** 2) *
            k_beam7]]
if s == 1:
    k_frame_local_8 = [[k_rod8, 0, 0, -k_rod8, 0, 0],
            [0, 12 * k_beam8, 6 * length8 * k_beam8, 0, -12 * k_beam8,
            6 * length8 * k_beam8],
            [0, 6 * length8 * k_beam8, 4 * (
            length8 ** 2) * k_beam8, 0,
            -6 * length8 * k_beam8, 2 * (
            length8 ** 2) * k_beam8],
            [-k_rod8, 0, 0, k_rod8, 0, 0],
            [0, -12 * k_beam8, -6 * length8 * k_beam8, 0, 12 * k_beam8,
            -6 * length8 * k_beam8],
            [0, 6 * length8 * k_beam8, 2 * (length8 ** 2) *
            k_beam8, 0,
            -6 * length8 * k_beam8, 4 * (length8 ** 2) *
            k_beam8]]
if s == 1:
    k_frame_local_9 = [[k_rod9, 0, 0, -k_rod9, 0, 0],
            [0, 12 * k_beam9, 6 * length9 * k_beam9, 0, -12 * k_beam9,
            6 * length9 * k_beam9],
            [0, 6 * length9 * k_beam9, 4 * (
            length9 ** 2) * k_beam9, 0,
            -6 * length9 * k_beam9, 2 * (
            length9 ** 2) * k_beam9],
            [-k_rod9, 0, 0, k_rod9, 0, 0],
            [0, -12 * k_beam9, -6 * length9 * k_beam9, 0, 12 * k_beam9,
            -6 * length9 * k_beam9],
            [0, 6 * length9 * k_beam9, 2 * (length9 ** 2) *
            k_beam9, 0,
            -6 * length9 * k_beam9, 4 * (length9 ** 2) *
            k_beam9]]
if s == 1:
    k_frame_local_10 = [[k_rod10, 0, 0, -k_rod10, 0, 0],
            [0, 12 * k_beam10, 6 * length10 * k_beam10, 0, -12 * k_beam10,
            6 * length10 * k_beam10],
            [0, 6 * length10 * k_beam10, 4 * (
            length10 ** 2) * k_beam10, 0,
            -6 * length10 * k_beam10, 2 * (
            length10 ** 2) * k_beam10],
            [-k_rod10, 0, 0, k_rod10, 0, 0],
            [0, -12 * k_beam10, -6 * length10 * k_beam10, 0, 12 * k_beam10,
            -6 * length10 * k_beam10],
            [0, 6 * length10 * k_beam10, 2 * (length10 ** 2) *
            k_beam10, 0,
            -6 * length10 * k_beam10, 4 * (length10 ** 2) *
            k_beam10]]
if s == 1:
    k_frame_local_11 = [[k_rod11, 0, 0, -k_rod11, 0, 0],
            [0, 12 * k_beam11, 6 * length11 * k_beam11, 0, -12 * k_beam11,
            6 * length11 * k_beam11],
            [0, 6 * length11 * k_beam11, 4 * (
            length11 ** 2) * k_beam11, 0,
            -6 * length11 * k_beam11, 2 * (
            length11 ** 2) * k_beam11],
            [-k_rod11, 0, 0, k_rod11, 0, 0],
            [0, -12 * k_beam11, -6 * length11 * k_beam11, 0, 12 * k_beam11,
            -6 * length11 * k_beam11],
            [0, 6 * length11 * k_beam11, 2 * (length11 ** 2) *
            k_beam11, 0,
            -6 * length11 * k_beam11, 4 * (length11 ** 2) *
            k_beam11]]
if s == 1:
    k_frame_local_12 = [[k_rod12, 0, 0, -k_rod12, 0, 0],
            [0, 12 * k_beam12, 6 * length12 * k_beam12, 0, -12 * k_beam12,
            6 * length12 * k_beam12],
            [0, 6 * length12 * k_beam12, 4 * (
            length12 ** 2) * k_beam12, 0,
            -6 * length12 * k_beam12, 2 * (
            length12 ** 2) * k_beam12],
            [-k_rod12, 0, 0, k_rod12, 0, 0],
            [0, -12 * k_beam12, -6 * length12 * k_beam12, 0, 12 * k_beam12,
            -6 * length12 * k_beam12],
            [0, 6 * length12 * k_beam12, 2 * (length12 ** 2) *
            k_beam12, 0,
            -6 * length12 * k_beam12, 4 * (length12 ** 2) *
            k_beam12]]
if s == 1:
    k_frame_local_13 = [[k_rod13, 0, 0, -k_rod13, 0, 0],
            [0, 12 * k_beam13, 6 * length13 * k_beam13, 0, -12 * k_beam13,
            6 * length13 * k_beam13],
            [0, 6 * length13 * k_beam13, 4 * (
            length13 ** 2) * k_beam13, 0,
            -6 * length13 * k_beam13, 2 * (
            length13 ** 2) * k_beam13],
            [-k_rod13, 0, 0, k_rod13, 0, 0],
            [0, -12 * k_beam13, -6 * length13 * k_beam13, 0, 12 * k_beam13,
            -6 * length13 * k_beam13],
            [0, 6 * length13 * k_beam13, 2 * (length13 ** 2) *
            k_beam13, 0,
            -6 * length13 * k_beam13, 4 * (length13 ** 2) *
            k_beam13]]

else:
    k_frame_local_1 = ((E*I)/(length1*((length1**2) +
                                       12*g)))*np.array([[(
                       A/I)*((length1**2)+2*g), 0, 0, -(
                       A/I)*((length1**2)+2*g), 0, 0], [0, 12,
                      6*length1, 0, -12, 6*length1], [0, 6*L,
                      ((4*length1**2) + 12*g), 0, -6*length1,
                      ((2*length1**2) - 12*g)], [-(
                      A/I)*((length1**2)+2*g), 0, 0, (
                      A/I)*((length1**2)+2*g), 0, 0], [0, -12,
                      -6*length1, 0, 12, -6*length1], [0,
                      6*length1, ((2*length1**2) - 12*g), 0,
                      -6*length1, ((4*length1**2) + 12*g)]])

    k_frame_local_2 = ((E*I)/(length2*((length2**2) +
                                       12*g)))*np.array([[(
                      A/I) * ((length2 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length2 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length2, 0, -12, 6 * length2], [0, 6 * L,
                      ((4 * length2 ** 2) + 12 * g), 0,
                      -6 * length2, ((2 * length2 ** 2) - 12 *
                      g)], [-(A/I) * ((length2 ** 2) + 2 * g), 0, 0,
                      (A/I) * ((length2 ** 2) + 2 * g), 0, 0], [0,
                      -12, -6 * length2, 0, 12, -6 * length2], [0,
                      6 * length2, ((2 * length2 ** 2) - 12 * g), 0,
                      -6 * length2, ((4 * length2 ** 2) + 12 * g)]])

    k_frame_local_3 = ((E*I)/(length3*((length3**2) +
                                       12*g)))*np.array([[(
                      A/I) * ((length3 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length3 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length3, 0, -12, 6 * length3], [0, 6 * L,
                      ((4 * length3 ** 2) + 12 * g), 0, -6 * length3,
                      ((2 * length3 ** 2) - 12 * g)], [-(
                      A/I) * ((length3 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length3 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length3, 0, 12, -6 * length3], [0,
                      6 * length3, ((2 * length3 ** 2) - 12 * g), 0,
                      -6 * length3, ((4 * length3 ** 2) + 12 * g)]])

    k_frame_local_4 = ((E*I)/(length4*((length4**2) +
                                       12*g)))*np.array([[(
                      A/I) * ((length4 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length4 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length4, 0, -12, 6 * length4], [0, 6 * L,
                      ((4 * length4 ** 2) + 12 * g), 0, -6 * length4,
                      ((2 * length4 ** 2) - 12 * g)], [-(
                      A/I) * ((length4 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length4 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length4, 0, 12, -6 * length4], [0,
                      6 * length4, ((2 * length4 ** 2) - 12 * g), 0,
                      -6 * length4, ((4 * length4 ** 2) + 12 * g)]])

    k_frame_local_5 = ((E*I)/(length5*((length5**2) +
                                       12*g)))*np.array([[(
                      A/I) * ((length5 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length5 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length5, 0, -12, 6 * length5], [0, 6 * L,
                      ((4 * length5 ** 2) + 12 * g), 0, -6 * length5,
                      ((2 * length5 ** 2) - 12 * g)], [-(
                      A/I) * ((length5 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length5 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length5, 0, 12, -6 * length5], [0,
                      6 * length5, ((2 * length5 ** 2) - 12 * g), 0,
                      -6 * length5, ((4 * length5 ** 2) + 12 * g)]])

    k_frame_local_6 = ((E*I)/(length6*((length6**2) +
                                       12*g)))*np.array([[(
                      A/I) * ((length6 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length6 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length6, 0, -12, 6 * length6], [0, 6 * L,
                      ((4 * length6 ** 2) + 12 * g), 0, -6 * length6,
                      ((2 * length6 ** 2) - 12 * g)], [-(
                      A/I) * ((length6 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length6 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length6, 0, 12, -6 * length6], [0,
                      6 * length6, ((2 * length6 ** 2) - 12 * g), 0,
                      -6 * length6, ((4 * length6 ** 2) + 12 * g)]])

    k_frame_local_7 = ((E*I)/(length7*((length7**2) +
                                       12*g)))*np.array([[(
                      A/I) * ((length7 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length7 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length7, 0, -12, 6 * length7], [0, 6 * L,
                      ((4 * length7 ** 2) + 12 * g), 0, -6 * length7,
                      ((2 * length7 ** 2) - 12 * g)], [-(
                      A/I) * ((length7 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length7 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length7, 0, 12, -6 * length7], [0,
                      6 * length7, ((2 * length7 ** 2) - 12 * g), 0,
                      -6 * length7, ((4 * length7 ** 2) + 12 * g)]])

    k_frame_local_8 = ((E*I)/(length8*((length8**2) +
                                       12*g)))*np.array([[(
                      A/I) * ((length8 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length8 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length8, 0, -12, 6 * length8], [0, 6 * L,
                      ((4 * length8 ** 2) + 12 * g), 0, -6 * length8,
                      ((2 * length8 ** 2) - 12 * g)], [-(
                      A/I) * ((length8 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length8 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length8, 0, 12, -6 * length8], [0,
                      6 * length8, ((2 * length8 ** 2) - 12 * g), 0,
                      -6 * length8, ((4 * length8 ** 2) + 12 * g)]])

    k_frame_local_9 = ((E*I)/(length9*((length9**2) +
                                       12*g)))*np.array([[(
                      A/I) * ((length9 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length9 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length9, 0, -12, 6 * length9], [0, 6 * L,
                      ((4 * length9 ** 2) + 12 * g), 0, -6 * length9,
                      ((2 * length9 ** 2) - 12 * g)], [-(
                      A/I) * ((length9 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length9 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length9, 0, 12, -6 * length9], [0,
                      6 * length9, ((2 * length9 ** 2) - 12 * g), 0,
                      -6 * length9, ((4 * length9 ** 2) + 12 * g)]])

    k_frame_local_10 = ((E*I)/(length10*((length10**2) +
                                         12*g)))*np.array([[(
                      A/I) * ((length10 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length10 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length10, 0, -12, 6 * length10], [0, 6 * L,
                      ((4 * length10 ** 2) + 12 * g), 0, -6 * length10,
                      ((2 * length10 ** 2) - 12 * g)], [-(
                      A/I) * ((length10 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length10 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length10, 0, 12, -6 * length10], [0,
                      6 * length10, ((2 * length10 ** 2) - 12 * g), 0,
                      -6 * length10, ((4 * length10 ** 2) + 12 * g)]])

    k_frame_local_11 = ((E*I)/(length11*((length11**2) +
                                         12*g)))*np.array([[(
                      A/I) * ((length11 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length11 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length11, 0, -12, 6 * length11], [0, 6 * L,
                      ((4 * length11 ** 2) + 12 * g), 0, -6 * length11,
                      ((2 * length11 ** 2) - 12 * g)], [-(
                      A/I) * ((length11 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length11 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length11, 0, 12, -6 * length11], [0,
                      6 * length11, ((2 * length11 ** 2) - 12 * g), 0,
                      -6 * length11, ((4 * length11 ** 2) + 12 * g)]])

    k_frame_local_12 = ((E*I)/(length12*((length12**2) +
                                         12*g)))*np.array([[(
                      A/I) * ((length12 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length12 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length12, 0, -12, 6 * length12], [0, 6 * L,
                      ((4 * length12 ** 2) + 12 * g), 0, -6 * length12,
                      ((2 * length12 ** 2) - 12 * g)], [-(
                      A/I) * ((length12 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length12 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length12, 0, 12, -6 * length12], [0,
                      6 * length12, ((2 * length12 ** 2) - 12 * g), 0,
                      -6 * length12, ((4 * length12 ** 2) + 12 * g)]])

    k_frame_local_13 = ((E*I)/(length13*((length13**2) +
                                         12*g)))*np.array([[(
                      A/I) * ((length13 ** 2) + 2 * g), 0, 0, -(
                      A/I) * ((length13 ** 2) + 2 * g), 0, 0], [0, 12,
                      6 * length13, 0, -12, 6 * length13], [0, 6 * L,
                      ((4 * length13 ** 2) + 12 * g), 0, -6 * length13,
                      ((2 * length13 ** 2) - 12 * g)], [-(
                      A/I) * ((length13 ** 2) + 2 * g), 0, 0, (
                      A/I) * ((length13 ** 2) + 2 * g), 0, 0], [0, -12,
                      -6 * length13, 0, 12, -6 * length13], [0,
                      6 * length13, ((2 * length13 ** 2) - 12 * g), 0,
                      -6 * length13, ((4 * length13 ** 2) + 12 * g)]])

a=1