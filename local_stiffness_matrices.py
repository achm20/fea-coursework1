import nodes_and_elems as nae
import numpy as np

E = 200*(10**9)
A = 1*(10**-2)
L = 1.5
k = E*A/L

local1 = [[nae.l1 ** 2, nae.l1 * nae.m1, -(nae.l1 ** 2),
           -(nae.l1 * nae.m1)], [nae.l1 * nae.m1, nae.m1 ** 2,
                               -(nae.l1 * nae.m1), -(nae.m1 ** 2)], [
              -(nae.l1 ** 2), -(nae.l1 * nae.m1), nae.l1 ** 2,
              nae.l1 * nae.m1], [-(nae.l1 * nae.m1), -(nae.m1 ** 2),
                               nae.l1 * nae.m1, nae.m1 ** 2]]

k1 = k*np.array(local1)
#print(k1)

local2 = [[nae.l2 ** 2, nae.l2 * nae.m2, -(nae.l2 ** 2),
           -(nae.l2 * nae.m2)], [nae.l2 * nae.m2, nae.m2 ** 2,
                             -(nae.l2 * nae.m2), -(nae.m2 ** 2)], [
              -(nae.l2 ** 2), -(nae.l2 * nae.m2), nae.l2 ** 2,
    nae.l2 * nae.m2], [-(nae.l2 * nae.m2), -(nae.m2 ** 2),
                       nae.l2 * nae.m2, nae.m2 ** 2]]

k2 = k*np.array(local2)
#print(k2)

local3 = [[nae.l3 ** 2, nae.l3 * nae.m3, -(nae.l3 ** 2),
           -(nae.l3 * nae.m3)], [nae.l3 * nae.m3, nae.m3 ** 2,
                             -(nae.l3 * nae.m3), -(nae.m3 ** 2)], [
              -(nae.l3 ** 2), -(nae.l3 * nae.m3), nae.l3 ** 2,
                                              nae.l3 * nae.m3], [-(
        nae.l3 * nae.m3), -(nae.m3 ** 2), nae.l3 * nae.m3, nae.m3
                                                             ** 2]]

k3 = k*np.array(local3)
#print(k3)

local4 = [[nae.l4 ** 2, nae.l4 * nae.m4, -(nae.l4 ** 2),
           -(nae.l4 * nae.m4)], [nae.l4 * nae.m4, nae.m4 ** 2,
                             -(nae.l4 * nae.m4), -(nae.m4 ** 2)], [
              -(nae.l4 ** 2), -(nae.l4 * nae.m4), nae.l4 ** 2,
                                              nae.l4 * nae.m4], [-(
        nae.l4 * nae.m4), -(nae.m4 ** 2), nae.l4 * nae.m4, nae.m4
                                                             ** 2]]

k4 = k*np.array(local4)

local5 = [[nae.l5 ** 2, nae.l5 * nae.m5, -(nae.l5 ** 2),
           -(nae.l5 * nae.m5)], [nae.l5 * nae.m5, nae.m5 ** 2,
                             -(nae.l5 * nae.m5), -(nae.m5 ** 2)], [
              -(nae.l5 ** 2), -(nae.l5 * nae.m5), nae.l5 ** 2,
                                              nae.l5 * nae.m5], [-(
        nae.l5 * nae.m5), -(nae.m5 ** 2), nae.l5 * nae.m5, nae.m5
                                                             ** 2]]

k5 = k*np.array(local5)

local6 = [[nae.l6 ** 2, nae.l6 * nae.m6, -(nae.l6 ** 2),
           -(nae.l6 * nae.m6)], [nae.l6 * nae.m6, nae.m6 ** 2,
                             -(nae.l6 * nae.m6), -(nae.m6 ** 2)], [
              -(nae.l6 ** 2), -(nae.l6 * nae.m6), nae.l6 ** 2,
                                              nae.l6 * nae.m6], [-(
        nae.l6 * nae.m6), -(nae.m6 ** 2), nae.l6 * nae.m6, nae.m6
                                                             ** 2]]

k6 = k*np.array(local6)

local7 = [[nae.l7 ** 2, nae.l7 * nae.m7, -(nae.l7 ** 2),
           -(nae.l7 * nae.m7)], [nae.l7 * nae.m7, nae.m7 ** 2,
                             -(nae.l7 * nae.m7), -(nae.m7 ** 2)], [
              -(nae.l7 ** 2), -(nae.l7 * nae.m7), nae.l7 ** 2,
                                              nae.l7 * nae.m7], [-(
        nae.l7 * nae.m7), -(nae.m7 ** 2), nae.l7 * nae.m7, nae.m7
                                                             ** 2]]

k7 = k*np.array(local7)

local8 = [[nae.l8 ** 2, nae.l8 * nae.m8, -(nae.l8 ** 2),
           -(nae.l8 * nae.m8)], [nae.l8 * nae.m8, nae.m8 ** 2,
                             -(nae.l8 * nae.m8), -(nae.m8 ** 2)], [
              -(nae.l8 ** 2), -(nae.l8 * nae.m8), nae.l8 ** 2,
                                              nae.l8 * nae.m8], [-(
        nae.l8 * nae.m8), -(nae.m8 ** 2), nae.l8 * nae.m8, nae.m8
                                                             ** 2]]

k8 = k*np.array(local8)

local9 = [[nae.l9 ** 2, nae.l9 * nae.m9, -(nae.l9 ** 2),
           -(nae.l9 * nae.m9)], [nae.l9 * nae.m9, nae.m9 ** 2,
                             -(nae.l9 * nae.m9), -(nae.m9 ** 2)], [
              -(nae.l9 ** 2), -(nae.l9 * nae.m9), nae.l9 ** 2,
                                              nae.l9 * nae.m9], [-(
        nae.l9 * nae.m9), -(nae.m9 ** 2), nae.l9 * nae.m9, nae.m9
                                                             ** 2]]

k9 = k*np.array(local9)

local10 = [[nae.l10 ** 2, nae.l10 * nae.m10, -(nae.l10 ** 2),
            -(nae.l10 * nae.m10)], [nae.l10 * nae.m10, nae.m10 ** 2,
                                -(nae.l10 * nae.m10), -(nae.m10 **
                                                         2)], [
              -(nae.l10 ** 2), -(nae.l10 * nae.m10), nae.l10 ** 2,
                                          nae.l10 * nae.m10], [-(
    nae.l10 * nae.m10), -(nae.m10 ** 2), nae.l10 * nae.m10, nae.m10
                                                           ** 2]]

k10 = k*np.array(local10)

local11 = [[nae.l11 ** 2, nae.l11 * nae.m11, -(nae.l11 ** 2),
            -(nae.l11 * nae.m11)], [nae.l11 * nae.m11, nae.m11 ** 2,
                               -(nae.l11 * nae.m11), -(nae.m11 **
                                                       2)], [
              -(nae.l11 ** 2), -(nae.l11 * nae.m11), nae.l11 ** 2,
                                                nae.l11 * nae.m11],
           [-(nae.l11 * nae.m11), -(nae.m11 ** 2), nae.l11 *
            nae.m11, nae.m11 ** 2]]

k11 = k*np.array(local11)

local12 = [[nae.l12 ** 2, nae.l12 * nae.m12, -(nae.l12 ** 2),
            -(nae.l12 * nae.m12)], [nae.l12 * nae.m12, nae.m12 ** 2,
                               -(nae.l12 * nae.m12), -(nae.m12 ** 2)], [
              -(nae.l12 ** 2), -(nae.l12 * nae.m12), nae.l12 ** 2,
                                                nae.l12 * nae.m12], [-(
        nae.l12 * nae.m12), -(nae.m12 ** 2), nae.l12 * nae.m12, nae.m12
                                                                ** 2]]

k12 = k*np.array(local12)

local13 = [[nae.l13 ** 2, nae.l13 * nae.m13, -(nae.l13 ** 2),
            -(nae.l13 * nae.m13)], [nae.l13 * nae.m13, nae.m13 ** 2,
                               -(nae.l13 * nae.m13), -(nae.m13 ** 2)], [
              -(nae.l13 ** 2), -(nae.l13 * nae.m13), nae.l13 ** 2,
                                                nae.l13 * nae.m13], [-(
        nae.l13 * nae.m13), -(nae.m13 ** 2), nae.l13 * nae.m13, nae.m13
                                                                ** 2]]

k13 = k*np.array(local13)