import global_stiffness_matrices_frames as gsmf
import numpy as np

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
