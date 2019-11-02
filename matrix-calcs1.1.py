import numpy as np
import math

Node_1 = {'x': 0, 'y': 0}
Node_2 = {'x': 0, 'y': 0.3}
Node_3 = {'x': 1.5, 'y': 0}
Node_4 = {'x': 1.5, 'y': 0.25}
Node_5 = {'x': 3, 'y': 0}
Node_6 = {'x': 3, 'y': 0.2}
Node_7 = {'x': 4.5, 'y': 0}
Node_8 = {'x': 4.5, 'y': 0.15}
Node_9 = {'x': 6, 'y': 0}
Node_10 = {'x': 6, 'y': 0.1}

L = 1.5
Beta = 2*(2*math.pi/360)
cb = math.cos(Beta)

Elem_1 = {'n1': Node_1, 'n2': Node_2, 'length': 0.2*L}
Elem_2 = {'n1': Node_1, 'n2': Node_3, 'length': L}
Elem_3 = {'n1': Node_2, 'n2': Node_4, 'length': L*cb}
Elem_4 = {'n1': Node_3, 'n2': Node_4, 'length': (1/6)*L}
Elem_5 = {'n1': Node_3, 'n2': Node_5, 'length': L}
Elem_6 = {'n1': Node_4, 'n2': Node_6, 'length': L*cb}
Elem_7 = {'n1': Node_5, 'n2': Node_6, 'length': (2/15)*L}
Elem_8 = {'n1': Node_5, 'n2': Node_7, 'length': L}
Elem_9 = {'n1': Node_6, 'n2': Node_8, 'length': L*cb}
Elem_10 = {'n1': Node_7, 'n2': Node_8, 'length': (1/10)*L}
Elem_11 = {'n1': Node_7, 'n2': Node_9, 'length': L}
Elem_12 = {'n1': Node_8, 'n2': Node_10, 'length': L*cb}
Elem_13 = {'n1': Node_9, 'n2': Node_10, 'length': (1/15)*L}

print(Elem_1)