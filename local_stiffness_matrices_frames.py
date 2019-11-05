import nodes_and_elems as nae
import numpy as np

E = 200*(10**9)
A = 1*(10**-2)
b = 0.1
d = 0.1
I = (b*d**3)/12
L = 1.5

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




