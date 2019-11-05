import nodes_and_elems as nae
import numpy as np

E = 200*(10**9)
A = 1*(10**-2)
b = 0.1
d = 0.1
I = (b*d**3)/12
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

k_beam1 = E*I/((nae.Elem_1['length'])**3)
k_beam2 = E*I/((nae.Elem_2['length'])**3)
k_beam3 = E*I/((nae.Elem_3['length'])**3)
k_beam4 = E*I/((nae.Elem_4['length'])**3)
k_beam5 = E*I/((nae.Elem_5['length'])**3)
k_beam6 = E*I/((nae.Elem_6['length'])**3)
k_beam7 = E*I/((nae.Elem_7['length'])**3)
k_beam8 = E*I/((nae.Elem_8['length'])**3)
k_beam9 = E*I/((nae.Elem_9['length'])**3)
k_beam10 = E*I/((nae.Elem_10['length'])**3)
k_beam11 = E*I/((nae.Elem_11['length'])**3)
k_beam12 = E*I/((nae.Elem_12['length'])**3)
k_beam13 = E*I/((nae.Elem_13['length'])**3)



