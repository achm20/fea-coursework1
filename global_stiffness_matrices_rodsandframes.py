import nodes_and_elems as nae
import numpy as np
import local_stiffness_matrices_rodsandframes as lsmrf

Transform1 = np.array([[nae.l1, nae.m1, 0, 0],
              [-nae.m1, nae.l1, 0, 0],
              [0, 0, nae.l1, nae.m1],
              [0, 0, -nae.m1, nae.l1]])

Transform2 = np.array([[nae.l2, nae.m2, 0, 0, 0, 0],
              [-nae.m2, nae.l2, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, nae.l2, nae.m2, 0],
              [0, 0, 0, -nae.m2, nae.l2, 0],
              [0, 0, 0, 0, 0, 1]])

Transform3 = np.array([[nae.l3, nae.m3, 0, 0, 0, 0],
              [-nae.m3, nae.l3, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, nae.l3, nae.m3, 0],
              [0, 0, 0, -nae.m3, nae.l3, 0],
              [0, 0, 0, 0, 0, 1]])

Transform4 = np.array([[nae.l4, nae.m4, 0, 0],
              [-nae.m4, nae.l4, 0, 0],
              [0, 0, nae.l4, nae.m4],
              [0, 0, -nae.m4, nae.l4]])

Transform5 = np.array([[nae.l5, nae.m5, 0, 0, 0, 0],
              [-nae.m5, nae.l5, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, nae.l5, nae.m5, 0],
              [0, 0, 0, -nae.m5, nae.l5, 0],
              [0, 0, 0, 0, 0, 1]])

Transform6 = np.array([[nae.l6, nae.m6, 0, 0, 0, 0],
              [-nae.m6, nae.l6, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, nae.l6, nae.m6, 0],
              [0, 0, 0, -nae.m6, nae.l6, 0],
              [0, 0, 0, 0, 0, 1]])

Transform7 = np.array([[nae.l7, nae.m7, 0, 0],
              [-nae.m7, nae.l7, 0, 0],
              [0, 0, nae.l7, nae.m7],
              [0, 0, -nae.m7, nae.l7]])

Transform8 = np.array([[nae.l8, nae.m8, 0, 0, 0, 0],
              [-nae.m8, nae.l8, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, nae.l8, nae.m8, 0],
              [0, 0, 0, -nae.m8, nae.l8, 0],
              [0, 0, 0, 0, 0, 1]])

Transform9 = np.array([[nae.l9, nae.m9, 0, 0, 0, 0],
              [-nae.m9, nae.l9, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, nae.l9, nae.m9, 0],
              [0, 0, 0, -nae.m9, nae.l9, 0],
              [0, 0, 0, 0, 0, 1]])

Transform10 = np.array([[nae.l10, nae.m10, 0, 0],
              [-nae.m10, nae.l10, 0, 0],
              [0, 0, nae.l10, nae.m10],
              [0, 0, -nae.m10, nae.l10]])

Transform11 = np.array([[nae.l11, nae.m11, 0, 0, 0, 0],
              [-nae.m11, nae.l11, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, nae.l11, nae.m11, 0],
              [0, 0, 0, -nae.m11, nae.l11, 0],
              [0, 0, 0, 0, 0, 1]])

Transform12 = np.array([[nae.l12, nae.m12, 0, 0, 0, 0],
              [-nae.m12, nae.l12, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, nae.l12, nae.m12, 0],
              [0, 0, 0, -nae.m12, nae.l12, 0],
              [0, 0, 0, 0, 0, 1]])

Transform13 = np.array([[nae.l13, nae.m13, 0, 0],
              [-nae.m13, nae.l13, 0, 0],
              [0, 0, nae.l13, nae.m13],
              [0, 0, -nae.m13, nae.l13]])

T_Transform1 = np.transpose(Transform1)
T_Transform2 = np.transpose(Transform2)
T_Transform3 = np.transpose(Transform3)
T_Transform4 = np.transpose(Transform4)
T_Transform5 = np.transpose(Transform5)
T_Transform6 = np.transpose(Transform6)
T_Transform7 = np.transpose(Transform7)
T_Transform8 = np.transpose(Transform8)
T_Transform9 = np.transpose(Transform9)
T_Transform10 = np.transpose(Transform10)
T_Transform11 = np.transpose(Transform11)
T_Transform12 = np.transpose(Transform12)
T_Transform13 = np.transpose(Transform13)

#k frame local 1 * Transformation Matrix 1
k_frame_Transform1 = np.matmul(lsmrf.k_rod1, Transform1)
#k frame local 2 * Transformation Matrix 2
k_frame_Transform2 = np.matmul(lsmrf.k_frame_local_2, Transform2)
#k frame local 3 * Transformation Matrix 3
k_frame_Transform3 = np.matmul(lsmrf.k_frame_local_3, Transform3)
#k frame local 4 * Transformation Matrix 4
k_frame_Transform4 = np.matmul(lsmrf.k_rod4, Transform4)
#k frame local 5 * Transformation Matrix 5
k_frame_Transform5 = np.matmul(lsmrf.k_frame_local_5, Transform5)
#k frame local 6 * Transformation Matrix 6
k_frame_Transform6 = np.matmul(lsmrf.k_frame_local_6, Transform6)
#k frame local 7 * Transformation Matrix 7
k_frame_Transform7 = np.matmul(lsmrf.k_rod7, Transform7)
#k frame local 8 * Transformation Matrix 8
k_frame_Transform8 = np.matmul(lsmrf.k_frame_local_8, Transform8)
#k frame local 9 * Transformation Matrix 9
k_frame_Transform9 = np.matmul(lsmrf.k_frame_local_9, Transform9)
#k frame local 10 * Transformation Matrix 10
k_frame_Transform10 = np.matmul(lsmrf.k_rod10, Transform10)
#k frame local 11 * Transformation Matrix 11
k_frame_Transform11 = np.matmul(lsmrf.k_frame_local_11, Transform11)
#k frame local 12 * Transformation Matrix 12
k_frame_Transform12 = np.matmul(lsmrf.k_frame_local_12, Transform12)
#k frame local 13 * Transformation Matrix 13
k_frame_Transform13 = np.matmul(lsmrf.k_rod13, Transform13)

k_frame_global_1 = np.matmul(T_Transform1, k_frame_Transform1)
k_frame_global_2 = np.matmul(T_Transform2, k_frame_Transform2)
k_frame_global_3 = np.matmul(T_Transform3, k_frame_Transform3)
k_frame_global_4 = np.matmul(T_Transform4, k_frame_Transform4)
k_frame_global_5 = np.matmul(T_Transform5, k_frame_Transform5)
k_frame_global_6 = np.matmul(T_Transform6, k_frame_Transform6)
k_frame_global_7 = np.matmul(T_Transform7, k_frame_Transform7)
k_frame_global_8 = np.matmul(T_Transform8, k_frame_Transform8)
k_frame_global_9 = np.matmul(T_Transform9, k_frame_Transform9)
k_frame_global_10 = np.matmul(T_Transform10, k_frame_Transform10)
k_frame_global_11 = np.matmul(T_Transform11, k_frame_Transform11)
k_frame_global_12 = np.matmul(T_Transform12, k_frame_Transform12)
k_frame_global_13 = np.matmul(T_Transform13, k_frame_Transform13)

a = 1
