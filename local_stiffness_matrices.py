import nodes_and_elems as nae

E = 200**9
A = 1**-2
L = 1.5

local1 = [[nae.l1 ** 2, nae.l1 * nae.m1, -(nae.l1 ** 2),
           -(nae.l1 * nae.m1)], [nae.l1 * nae.m1, nae.m1 ** 2,
                               -(nae.l1 * nae.m1), -(nae.m1 ** 2)], [
              -(nae.l1 ** 2), -(nae.l1 * nae.m1), nae.l1 ** 2,
              nae.l1 * nae.m1], [-(nae.l1 * nae.m1), -(nae.m1 ** 2),
                               nae.l1 * nae.m1, nae.m1 ** 2]]

local1 = [[nae.l1 ** 2, nae.l1 * nae.m1, -(nae.l1 ** 2),
           -(nae.l1 * nae.m1)], [nae.l1 * nae.m1, nae.m1 ** 2,
                               -(nae.l1 * nae.m1), -(nae.m1 ** 2)], [
              -(nae.l1 ** 2), -(nae.l1 * nae.m1), nae.l1 ** 2,
              nae.l1 * nae.m1], [-(nae.l1 * nae.m1), -(nae.m1 ** 2),
                               nae.l1 * nae.m1, nae.m1 ** 2]]

k1 = (E*A/L)*local1

local2 = [[nae.l2 ** 2, nae.l2 * nae.m2, -(nae.l2 ** 2),
           -(nae.l2 * nae.m2)], [nae.l2 * nae.m2, nae.m2 ** 2,
                             -(nae.l2 * nae.m2), -(nae.m2 ** 2)], [
              -(nae.l2 ** 2), -(nae.l2 * nae.m2), nae.l2 ** 2,
    nae.l2 * nae.m2], [-(nae.l2 * nae.m2), -(nae.m2 ** 2), nae.l2 * nae.m2, nae.m2
                                                                 ** 2]]

print(k1)

