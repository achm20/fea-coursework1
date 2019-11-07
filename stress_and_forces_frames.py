import displacement_calcs_frames as dcf
import local_stiffness_matrices_frames as lsmf
import numpy as np

E = 73.1*(10**9)
A = 4*(10**-4)

# Local Element direct stresses ------------------------------------
stress_el2 = E*dcf.e_el2
stress_el3 = E*dcf.e_el3
stress_el4 = E*dcf.e_el4
stress_el5 = E*dcf.e_el5
stress_el6 = E*dcf.e_el6
stress_el7 = E*dcf.e_el7
stress_el8 = E*dcf.e_el8
stress_el9 = E*dcf.e_el9
stress_el10 = E*dcf.e_el10
stress_el11 = E*dcf.e_el11
stress_el12 = E*dcf.e_el12
stress_el13 = E*dcf.e_el13

#Local element axial forces -----------------------------------------

axial_force_el2 = A*stress_el2
axial_force_el3 = A*stress_el3
axial_force_el4 = A*stress_el4
axial_force_el5 = A*stress_el5
axial_force_el6 = A*stress_el6
axial_force_el7 = A*stress_el7
axial_force_el8 = A*stress_el8
axial_force_el9 = A*stress_el9
axial_force_el10 = A*stress_el10
axial_force_el11 = A*stress_el11
axial_force_el12 = A*stress_el12
axial_force_el13 = A*stress_el13

#Local element forces check------------------------------------------

f_local_el2 = np.matmul(lsmf.k_frame_local_2, dcf.local_disp_el2)
f_local_el3 = np.matmul(lsmf.k_frame_local_3, dcf.local_disp_el3)
f_local_el4 = np.matmul(lsmf.k_frame_local_4, dcf.local_disp_el4)
f_local_el5 = np.matmul(lsmf.k_frame_local_5, dcf.local_disp_el5)
f_local_el6 = np.matmul(lsmf.k_frame_local_6, dcf.local_disp_el6)
f_local_el7 = np.matmul(lsmf.k_frame_local_7, dcf.local_disp_el7)
f_local_el8 = np.matmul(lsmf.k_frame_local_8, dcf.local_disp_el8)
f_local_el9 = np.matmul(lsmf.k_frame_local_9, dcf.local_disp_el9)
f_local_el10 = np.matmul(lsmf.k_frame_local_10, dcf.local_disp_el10)
f_local_el11 = np.matmul(lsmf.k_frame_local_11, dcf.local_disp_el11)
f_local_el12 = np.matmul(lsmf.k_frame_local_12, dcf.local_disp_el12)
f_local_el13 = np.matmul(lsmf.k_frame_local_13, dcf.local_disp_el13)

a = 1
