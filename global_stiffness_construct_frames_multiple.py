import global_stiffness_matrices_frames as gsmf
import nodes_and_elems_multiple as naem
import numpy as np
npe = 5

if npe < 3:
    M = np.zeros((30, 30))
    M[:6, :6] += gsmf.k_frame_global_1
    M[np.ix_([0, 1, 2, 6, 7, 8], [0, 1, 2, 6, 7, 8])] += \
    gsmf.k_frame_global_2
    M[np.ix_([3, 4, 5, 9, 10, 11], [3, 4, 5, 9, 10, 11])] += \
    gsmf.k_frame_global_3
    M[6:12, 6:12] += gsmf.k_frame_global_4
    M[np.ix_([6, 7, 8, 12, 13, 14], [6, 7, 8, 12, 13, 14])] += \
    gsmf.k_frame_global_5
    M[np.ix_([9, 10, 11, 15, 16, 17], [9, 10, 11, 15, 16, 17])] += \
    gsmf.k_frame_global_6
    M[12:18, 12:18] += gsmf.k_frame_global_7
    M[np.ix_([12, 13, 14, 18, 19, 20], [12, 13, 14, 18, 19, 20])] += \
    gsmf.k_frame_global_8
    M[np.ix_([15, 16, 17, 21, 22, 23], [15, 16, 17, 21, 22, 23])] += \
    gsmf.k_frame_global_9
    M[18:24, 18:24] += gsmf.k_frame_global_10
    M[np.ix_([18, 19, 20, 24, 25, 26], [18, 19, 20, 24, 25, 26])] += \
    gsmf.k_frame_global_11
    M[np.ix_([21, 22, 23, 27, 28, 29], [21, 22, 23, 27, 28, 29])] += \
    gsmf.k_frame_global_12
    M[24:30, 24:30] += gsmf.k_frame_global_13

if npe == 3:
    M = np.zeros((69, 69))
    M[:6, :6] += gsmf.k_frame_global_1
    M[3:9, 3:9] += gsmf.k_frame_global_1
    M[np.ix_([0, 1, 2, 9, 10, 11], [0, 1, 2, 9, 10, 11])] += \
        gsmf.k_frame_global_2
    M[9:15, 9:15] += gsmf.k_frame_global_2
    M[np.ix_([6, 7, 8, 15, 16, 17], [6, 7, 8, 15, 16, 17])] += \
        gsmf.k_frame_global_3
    M[15:21, 15:21] += gsmf.k_frame_global_3
    M[np.ix_([12, 13, 14, 21, 22, 23], [12, 13, 14, 21, 22, 23])] += \
        gsmf.k_frame_global_4
    M[18:24, 18:24] += gsmf.k_frame_global_4
    M[np.ix_([12, 13, 14, 27, 28, 29], [12, 13, 14, 27, 28, 29])] += \
        gsmf.k_frame_global_5
    M[24:30, 24:30] += gsmf.k_frame_global_5
    M[np.ix_([18, 19, 20, 33, 34, 35], [18, 19, 20, 33, 34, 35])] += \
        gsmf.k_frame_global_6
    M[30:36, 30:36] += gsmf.k_frame_global_6
    M[np.ix_([24, 25, 26, 39, 40, 41], [24, 25, 26, 39, 40, 41])] += \
        gsmf.k_frame_global_7
    M[np.ix_([30, 31, 32, 39, 40, 41], [30, 31, 32, 39, 40, 41])] += \
        gsmf.k_frame_global_7
    M[np.ix_([24, 25, 26, 45, 46, 47], [24, 25, 26, 45, 46, 47])] += \
        gsmf.k_frame_global_8
    M[np.ix_([36, 37, 38, 45, 46, 47], [36, 37, 38, 45, 46, 47])] += \
        gsmf.k_frame_global_8
    M[np.ix_([30, 31, 32, 51, 52, 53], [30, 31, 32, 51, 52, 53])] += \
        gsmf.k_frame_global_9
    M[np.ix_([42, 43, 44, 51, 52, 53], [42, 43, 44, 51, 52, 53])] += \
        gsmf.k_frame_global_9
    M[np.ix_([36, 37, 38, 57, 58, 59], [36, 37, 38, 57, 58, 59])] += \
        gsmf.k_frame_global_10
    M[np.ix_([42, 43, 44, 57, 58, 59], [42, 43, 44, 57, 58, 59])] += \
        gsmf.k_frame_global_10
    M[np.ix_([36, 37, 38, 60, 61, 62], [36, 37, 38, 60, 61, 62])] += \
        gsmf.k_frame_global_11
    M[np.ix_([48, 49, 50, 60, 61, 62], [48, 49, 50, 60, 61, 62])] += \
        gsmf.k_frame_global_11
    M[np.ix_([42, 43, 44, 63, 64, 65], [42, 43, 44, 63, 64, 65])] += \
        gsmf.k_frame_global_12
    M[np.ix_([54, 55, 56, 63, 64, 65], [54, 55, 56, 63, 64, 65])] += \
        gsmf.k_frame_global_12
    M[np.ix_([48, 49, 50, 66, 67, 68], [48, 49, 50, 66, 67, 68])] += \
        gsmf.k_frame_global_13
    M[np.ix_([54, 55, 56, 66, 67, 68], [54, 55, 56, 66, 67, 68])] += \
        gsmf.k_frame_global_13

a = 1