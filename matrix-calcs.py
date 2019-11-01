import numpy as np
import math

ECT = [[1, 1(0,0), 2(0,0.3)], [2, 1, 3], [3, 2, 4], [4, 3, 4], [5, 3, 5], [6, 4, 6], [7, 5, 6],
                [8, 5, 7], [9, 6, 8], [10, 7, 8], [11, 7, 9], [12, 8, 10], [13, 9, 10]]

ArrayECT = np.array(ECT, dtype=np.int32)

ToNC = [[1, 0, 0], [2, 0, 0.3], [3, 1.5, 0], [4, 1.5, 0.25], [5, 3, 0], [6, 3, 0.2], [7, 4.5, 0],
        [8, 4.5, 0.15], [9, 6, 0], [10, 6, 0.1]]

Array = np.array(ToNC, dtype=np.float32)

#L = 1.5
#Beta = 2*(2*math.pi/360)
#cb = math.cos(Beta)

print(ArrayECT)
print(ArrayECT.shape)




