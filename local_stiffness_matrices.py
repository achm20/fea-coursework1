import nodes_and_elems as nae
import numpy as np

E = 73.1*(10**9)
A = 4*(10**-4)
L = 1.5

k_rod1 = A*E/nae.Elem_1['length']
k_rod2 = A*E/nae.Elem_2['length']
k_rod3 = A*E/nae.Elem_3['length']
k_rod4 = A*E/nae.Elem_4['length']
k_rod5 = A*E/nae.Elem_5['length']
k_rod6 = A*E/nae.Elem_6['length']
k_rod7 = A*E/nae.Elem_7['length']
k_rod8 = A*E/nae.Elem_8['length']
k_rod9 = A*E/nae.Elem_9['length']
k_rod10 = A*E/nae.Elem_10['length']
k_rod11 = A*E/nae.Elem_11['length']
k_rod12 = A*E/nae.Elem_12['length']
k_rod13 = A*E/nae.Elem_13['length']

global1 = [[nae.l1 ** 2, nae.l1 * nae.m1, -(nae.l1 ** 2),
           -(nae.l1 * nae.m1)], [nae.l1 * nae.m1, nae.m1 ** 2,
                               -(nae.l1 * nae.m1), -(nae.m1 ** 2)], [
              -(nae.l1 ** 2), -(nae.l1 * nae.m1), nae.l1 ** 2,
              nae.l1 * nae.m1], [-(nae.l1 * nae.m1), -(nae.m1 ** 2),
                               nae.l1 * nae.m1, nae.m1 ** 2]]

k1 = k_rod1*np.array(global1)

global2 = [[nae.l2 ** 2, nae.l2 * nae.m2, -(nae.l2 ** 2),
           -(nae.l2 * nae.m2)], [nae.l2 * nae.m2, nae.m2 ** 2,
                             -(nae.l2 * nae.m2), -(nae.m2 ** 2)], [
              -(nae.l2 ** 2), -(nae.l2 * nae.m2), nae.l2 ** 2,
    nae.l2 * nae.m2], [-(nae.l2 * nae.m2), -(nae.m2 ** 2),
                       nae.l2 * nae.m2, nae.m2 ** 2]]

k2 = k_rod2*np.array(global2)

global3 = [[nae.l3 ** 2, nae.l3 * nae.m3, -(nae.l3 ** 2),
           -(nae.l3 * nae.m3)], [nae.l3 * nae.m3, nae.m3 ** 2,
                             -(nae.l3 * nae.m3), -(nae.m3 ** 2)], [
              -(nae.l3 ** 2), -(nae.l3 * nae.m3), nae.l3 ** 2,
                                              nae.l3 * nae.m3], [-(
        nae.l3 * nae.m3), -(nae.m3 ** 2), nae.l3 * nae.m3, nae.m3
                                                             ** 2]]

k3 = k_rod3*np.array(global3)

global4 = [[nae.l4 ** 2, nae.l4 * nae.m4, -(nae.l4 ** 2),
           -(nae.l4 * nae.m4)], [nae.l4 * nae.m4, nae.m4 ** 2,
                             -(nae.l4 * nae.m4), -(nae.m4 ** 2)], [
              -(nae.l4 ** 2), -(nae.l4 * nae.m4), nae.l4 ** 2,
                                              nae.l4 * nae.m4], [-(
        nae.l4 * nae.m4), -(nae.m4 ** 2), nae.l4 * nae.m4, nae.m4
                                                             ** 2]]

k4 = k_rod4*np.array(global4)

global5 = [[nae.l5 ** 2, nae.l5 * nae.m5, -(nae.l5 ** 2),
           -(nae.l5 * nae.m5)], [nae.l5 * nae.m5, nae.m5 ** 2,
                             -(nae.l5 * nae.m5), -(nae.m5 ** 2)], [
              -(nae.l5 ** 2), -(nae.l5 * nae.m5), nae.l5 ** 2,
                                              nae.l5 * nae.m5], [-(
        nae.l5 * nae.m5), -(nae.m5 ** 2), nae.l5 * nae.m5, nae.m5
                                                             ** 2]]

k5 = k_rod5*np.array(global5)

global6 = [[nae.l6 ** 2, nae.l6 * nae.m6, -(nae.l6 ** 2),
           -(nae.l6 * nae.m6)], [nae.l6 * nae.m6, nae.m6 ** 2,
                             -(nae.l6 * nae.m6), -(nae.m6 ** 2)], [
              -(nae.l6 ** 2), -(nae.l6 * nae.m6), nae.l6 ** 2,
                                              nae.l6 * nae.m6], [-(
        nae.l6 * nae.m6), -(nae.m6 ** 2), nae.l6 * nae.m6, nae.m6
                                                             ** 2]]

k6 = k_rod6*np.array(global6)

global7 = [[nae.l7 ** 2, nae.l7 * nae.m7, -(nae.l7 ** 2),
           -(nae.l7 * nae.m7)], [nae.l7 * nae.m7, nae.m7 ** 2,
                             -(nae.l7 * nae.m7), -(nae.m7 ** 2)], [
              -(nae.l7 ** 2), -(nae.l7 * nae.m7), nae.l7 ** 2,
                                              nae.l7 * nae.m7], [-(
        nae.l7 * nae.m7), -(nae.m7 ** 2), nae.l7 * nae.m7, nae.m7
                                                             ** 2]]

k7 = k_rod7*np.array(global7)

global8 = [[nae.l8 ** 2, nae.l8 * nae.m8, -(nae.l8 ** 2),
           -(nae.l8 * nae.m8)], [nae.l8 * nae.m8, nae.m8 ** 2,
                             -(nae.l8 * nae.m8), -(nae.m8 ** 2)], [
              -(nae.l8 ** 2), -(nae.l8 * nae.m8), nae.l8 ** 2,
                                              nae.l8 * nae.m8], [-(
        nae.l8 * nae.m8), -(nae.m8 ** 2), nae.l8 * nae.m8, nae.m8
                                                             ** 2]]

k8 = k_rod8*np.array(global8)

global9 = [[nae.l9 ** 2, nae.l9 * nae.m9, -(nae.l9 ** 2),
           -(nae.l9 * nae.m9)], [nae.l9 * nae.m9, nae.m9 ** 2,
                             -(nae.l9 * nae.m9), -(nae.m9 ** 2)], [
              -(nae.l9 ** 2), -(nae.l9 * nae.m9), nae.l9 ** 2,
                                              nae.l9 * nae.m9], [-(
        nae.l9 * nae.m9), -(nae.m9 ** 2), nae.l9 * nae.m9, nae.m9
                                                             ** 2]]

k9 = k_rod9*np.array(global9)

global10 = [[nae.l10 ** 2, nae.l10 * nae.m10, -(nae.l10 ** 2),
            -(nae.l10 * nae.m10)], [nae.l10 * nae.m10, nae.m10 ** 2,
                                -(nae.l10 * nae.m10), -(nae.m10 **
                                                         2)], [
              -(nae.l10 ** 2), -(nae.l10 * nae.m10), nae.l10 ** 2,
                                          nae.l10 * nae.m10], [-(
    nae.l10 * nae.m10), -(nae.m10 ** 2), nae.l10 * nae.m10, nae.m10
                                                           ** 2]]

k10 = k_rod10*np.array(global10)

global11 = [[nae.l11 ** 2, nae.l11 * nae.m11, -(nae.l11 ** 2),
            -(nae.l11 * nae.m11)], [nae.l11 * nae.m11, nae.m11 ** 2,
                               -(nae.l11 * nae.m11), -(nae.m11 **
                                                       2)], [
              -(nae.l11 ** 2), -(nae.l11 * nae.m11), nae.l11 ** 2,
                                                nae.l11 * nae.m11],
           [-(nae.l11 * nae.m11), -(nae.m11 ** 2), nae.l11 *
            nae.m11, nae.m11 ** 2]]

k11 = k_rod11*np.array(global11)

global12 = [[nae.l12 ** 2, nae.l12 * nae.m12, -(nae.l12 ** 2),
            -(nae.l12 * nae.m12)], [nae.l12 * nae.m12, nae.m12 ** 2,
                               -(nae.l12 * nae.m12), -(nae.m12 ** 2)], [
              -(nae.l12 ** 2), -(nae.l12 * nae.m12), nae.l12 ** 2,
                                                nae.l12 * nae.m12], [-(
        nae.l12 * nae.m12), -(nae.m12 ** 2), nae.l12 * nae.m12, nae.m12
                                                                ** 2]]

k12 = k_rod12*np.array(global12)

global13 = [[nae.l13 ** 2, nae.l13 * nae.m13, -(nae.l13 ** 2),
            -(nae.l13 * nae.m13)], [nae.l13 * nae.m13, nae.m13 ** 2,
                               -(nae.l13 * nae.m13), -(nae.m13 ** 2)], [
              -(nae.l13 ** 2), -(nae.l13 * nae.m13), nae.l13 ** 2,
                                                nae.l13 * nae.m13], [-(
        nae.l13 * nae.m13), -(nae.m13 ** 2), nae.l13 * nae.m13, nae.m13
                                                                ** 2]]

k13 = k_rod13*np.array(global13)