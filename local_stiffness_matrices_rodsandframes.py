import nodes_and_elems as nae
import numpy as np

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

length1 = nae.Elem_1['length']
length2 = nae.Elem_2['length']
length3 = nae.Elem_3['length']
length4 = nae.Elem_4['length']
length5 = nae.Elem_5['length']
length6 = nae.Elem_6['length']
length7 = nae.Elem_7['length']
length8 = nae.Elem_8['length']
length9 = nae.Elem_9['length']
length10 = nae.Elem_10['length']
length11 = nae.Elem_11['length']
length12 = nae.Elem_12['length']
length13 = nae.Elem_13['length']

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

k_frame_local_1 = k_rod1*np.array([[1, 0, -1, 0], [0, 0, 0, 0],
                                   [-1, 0, 1, 0], [0, 0, 0, 0]])

k_frame_local_4 = k_rod4*np.array([[1, 0, -1, 0], [0, 0, 0, 0],
                                   [-1, 0, 1, 0], [0, 0, 0, 0]])

k_frame_local_7 = k_rod7*np.array([[1, 0, -1, 0], [0, 0, 0, 0],
                                   [-1, 0, 1, 0], [0, 0, 0, 0]])

k_frame_local_10 = k_rod10*np.array([[1, 0, -1, 0], [0, 0, 0, 0],
                                   [-1, 0, 1, 0], [0, 0, 0, 0]])

k_frame_local_13 = k_rod13*np.array([[1, 0, -1, 0], [0, 0, 0, 0],
                                   [-1, 0, 1, 0], [0, 0, 0, 0]])

#if s = 1, then local stiffness matrices for bernoulli beam frame
# is used
#if s = 2, then local stiffness matrices for timoshenko beam frame
# is used

s = 2

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

else:
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

a=1