import math

count = 3 #nodes per element
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

Node_el1 = {}
for count in range(3, 5):
    Node_el1["nodes_per_el_%s" % count] = {'x': (Node_2['x'] -
    Node_1['x'])/count-1, 'y': (Node_2['y'] - Node_1['y'])/count-1}
    #for key, value in sorted(Node_el1.items()):

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

l1 = (Elem_1['n2']['x'] - Elem_1['n1']['x'])/(Elem_1['length'])
l2 = (Elem_2['n2']['x'] - Elem_2['n1']['x'])/(Elem_2['length'])
l3 = (Elem_3['n2']['x'] - Elem_3['n1']['x'])/(Elem_3['length'])
l4 = (Elem_4['n2']['x'] - Elem_4['n1']['x'])/(Elem_4['length'])
l5 = (Elem_5['n2']['x'] - Elem_5['n1']['x'])/(Elem_5['length'])
l6 = (Elem_6['n2']['x'] - Elem_6['n1']['x'])/(Elem_6['length'])
l7 = (Elem_7['n2']['x'] - Elem_7['n1']['x'])/(Elem_7['length'])
l8 = (Elem_8['n2']['x'] - Elem_8['n1']['x'])/(Elem_8['length'])
l9 = (Elem_9['n2']['x'] - Elem_9['n1']['x'])/(Elem_9['length'])
l10 = (Elem_10['n2']['x'] - Elem_10['n1']['x'])/(Elem_10['length'])
l11 = (Elem_11['n2']['x'] - Elem_11['n1']['x'])/(Elem_11['length'])
l12 = (Elem_12['n2']['x'] - Elem_12['n1']['x'])/(Elem_12['length'])
l13 = (Elem_13['n2']['x'] - Elem_13['n1']['x'])/(Elem_13['length'])

m1 = (Elem_1['n2']['y'] - Elem_1['n1']['y']) / (Elem_1['length'])
m2 = (Elem_2['n2']['y'] - Elem_2['n1']['y']) / (Elem_2['length'])
m3 = (Elem_3['n2']['y'] - Elem_3['n1']['y']) / (Elem_3['length'])
m4 = (Elem_4['n2']['y'] - Elem_4['n1']['y']) / (Elem_4['length'])
m5 = (Elem_5['n2']['y'] - Elem_5['n1']['y']) / (Elem_5['length'])
m6 = (Elem_6['n2']['y'] - Elem_6['n1']['y']) / (Elem_6['length'])
m7 = (Elem_7['n2']['y'] - Elem_7['n1']['y']) / (Elem_7['length'])
m8 = (Elem_8['n2']['y'] - Elem_8['n1']['y']) / (Elem_8['length'])
m9 = (Elem_9['n2']['y'] - Elem_9['n1']['y']) / (Elem_9['length'])
m10 = (Elem_10['n2']['y'] - Elem_10['n1']['y']) / (Elem_10['length'])
m11 = (Elem_11['n2']['y'] - Elem_11['n1']['y']) / (Elem_11['length'])
m12 = (Elem_12['n2']['y'] - Elem_12['n1']['y']) / (Elem_12['length'])
m13 = (Elem_13['n2']['y'] - Elem_13['n1']['y']) / (Elem_13['length'])

