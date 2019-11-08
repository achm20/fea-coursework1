import global_stiffness_matrices_rodsandframes as gsmrf
import numpy as np

M = np.zeros((30, 30))
M[np.ix_([0, 1, 3, 4], [0, 1, 3, 4])] += \
    gsmrf.k_frame_global_1
M[np.ix_([0, 1, 2, 6, 7, 8], [0, 1, 2, 6, 7, 8])] += \
    gsmrf.k_frame_global_2
M[np.ix_([3, 4, 5, 9, 10, 11], [3, 4, 5, 9, 10, 11])] += \
    gsmrf.k_frame_global_3
M[np.ix_([6, 7, 9, 10], [6, 7, 9, 10])] += \
    gsmrf.k_frame_global_4
M[np.ix_([6, 7, 8, 12, 13, 14], [6, 7, 8, 12, 13, 14])] += \
    gsmrf.k_frame_global_5
M[np.ix_([9, 10, 11, 15, 16, 17], [9, 10, 11, 15, 16, 17])] += \
    gsmrf.k_frame_global_6
M[np.ix_([12, 13, 15, 16], [12, 13, 15, 16])] += \
    gsmrf.k_frame_global_7
M[np.ix_([12, 13, 14, 18, 19, 20], [12, 13, 14, 18, 19, 20])] += \
    gsmrf.k_frame_global_8
M[np.ix_([15, 16, 17, 21, 22, 23], [15, 16, 17, 21, 22, 23])] += \
    gsmrf.k_frame_global_9
M[np.ix_([18, 19, 21, 22], [18, 19, 21, 22])] += \
    gsmrf.k_frame_global_10
M[np.ix_([18, 19, 20, 24, 25, 26], [18, 19, 20, 24, 25, 26])] += \
    gsmrf.k_frame_global_11
M[np.ix_([21, 22, 23, 27, 28, 29], [21, 22, 23, 27, 28, 29])] += \
    gsmrf.k_frame_global_12
M[np.ix_([24, 25, 27, 28], [24, 25, 27, 28])] += \
    gsmrf.k_frame_global_13

a = 1