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

#Element 1 internal nodes
Node_el1_1 = {}
for count in range(3, 6):
    Node_el1_1["nodes_per_el_%s" % count] = {'x': (Node_2['x'] -
    Node_1['x'])/(count-1), 'y': (Node_2['y'] - Node_1['y'])/(
            count-1)}

Node_el1_2 = {}
for count in range(4, 6):
    Node_el1_2["nodes_per_el_%s" % count] = {'x': (Node_2['x'] -
    Node_1['x'])*(2/(count-1)), 'y': (Node_2['y'] - Node_1[
        'y'])*(2/(count-1))}
else:
    Node_el1_2["nodes_per_el_3"] = Node_2

Node_el1_3 = {}
for count in range(5, 6):
    Node_el1_3["nodes_per_el_%s" % count] = {'x': (Node_2['x'] -
    Node_1['x'])*(3/(count-1)), 'y': (Node_2['y'] - Node_1[
        'y'])*(3/(count-1))}
else:
    Node_el1_3["nodes_per_el_4"] = Node_2

#Element 2 internal nodes
Node_el2_1 = {}
for count in range(3, 6):
    Node_el2_1["nodes_per_el_%s" % count] = {'x': (Node_3['x'] -
    Node_1['x'])/(count-1), 'y': (Node_3['y'] - Node_1['y'])/(
            count-1)}

Node_el2_2 = {}
for count in range(4, 6):
    Node_el2_2["nodes_per_el_%s" % count] = {'x': (Node_3['x'] -
    Node_1['x'])*(2/(count-1)), 'y': (Node_3['y'] - Node_1[
        'y'])*(2/(count-1))}
else:
    Node_el2_2["nodes_per_el_3"] = Node_3

Node_el2_3 = {}
for count in range(5, 6):
    Node_el2_3["nodes_per_el_%s" % count] = {'x': (Node_3['x'] -
    Node_1['x'])*(3/(count-1)), 'y': (Node_3['y'] - Node_1[
        'y'])*(3/(count-1))}
else:
    Node_el2_3["nodes_per_el_4"] = Node_2

#Element 3 internal nodes
Node_el3_1 = {}
for count in range(3, 6):
    Node_el3_1["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_2['x'])/(count-1), 'y': (Node_4['y'] - Node_2['y'])/(
            count-1)}

Node_el3_2 = {}
for count in range(4, 6):
    Node_el3_2["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_2['x'])*(2/(count-1)), 'y': (Node_4['y'] - Node_2[
        'y'])*(2/(count-1))}
else:
    Node_el3_2["nodes_per_el_3"] = Node_4

Node_el3_3 = {}
for count in range(5, 6):
    Node_el3_3["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_2['x'])*(3/(count-1)), 'y': (Node_4['y'] - Node_2[
        'y'])*(3/(count-1))}
else:
    Node_el3_3["nodes_per_el_4"] = Node_4

#Element 4 internal nodes
Node_el4_1 = {}
for count in range(3, 6):
    Node_el4_1["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_3['x'])/(count-1), 'y': (Node_4['y'] - Node_3['y'])/(
            count-1)}

Node_el4_2 = {}
for count in range(4, 6):
    Node_el4_2["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_3['x'])*(2/(count-1)), 'y': (Node_4['y'] - Node_3[
        'y'])*(2/(count-1))}
else:
    Node_el4_2["nodes_per_el_3"] = Node_4

Node_el4_3 = {}
for count in range(5, 6):
    Node_el4_3["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_3['x'])*(3/(count-1)), 'y': (Node_4['y'] - Node_3[
        'y'])*(3/(count-1))}
else:
    Node_el4_3["nodes_per_el_4"] = Node_4

#Element 5 internal nodes
Node_el5_1 = {}
for count in range(3, 6):
    Node_el5_1["nodes_per_el_%s" % count] = {'x': (Node_5['x'] -
    Node_3['x'])/(count-1), 'y': (Node_5['y'] - Node_3['y'])/(
            count-1)}

Node_el5_2 = {}
for count in range(4, 6):
    Node_el5_2["nodes_per_el_%s" % count] = {'x': (Node_5['x'] -
    Node_3['x'])*(2/(count-1)), 'y': (Node_5['y'] - Node_3[
        'y'])*(2/(count-1))}
else:
    Node_el5_2["nodes_per_el_3"] = Node_5

Node_el5_3 = {}
for count in range(5, 6):
    Node_el5_3["nodes_per_el_%s" % count] = {'x': (Node_5['x'] -
    Node_3['x'])*(3/(count-1)), 'y': (Node_5['y'] - Node_3[
        'y'])*(3/(count-1))}
else:
    Node_el5_3["nodes_per_el_4"] = Node_5

#Element 6 internal nodes
Node_el6_1 = {}
for count in range(3, 6):
    Node_el6_1["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_4['x'])/(count-1), 'y': (Node_6['y'] - Node_4['y'])/(
            count-1)}

Node_el6_2 = {}
for count in range(4, 6):
    Node_el6_2["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_4['x'])*(2/(count-1)), 'y': (Node_6['y'] - Node_4[
        'y'])*(2/(count-1))}
else:
    Node_el6_2["nodes_per_el_3"] = Node_6

Node_el6_3 = {}
for count in range(5, 6):
    Node_el6_3["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_4['x'])*(3/(count-1)), 'y': (Node_6['y'] - Node_4[
        'y'])*(3/(count-1))}
else:
    Node_el6_3["nodes_per_el_4"] = Node_6

#Element 7 internal nodes
Node_el7_1 = {}
for count in range(3, 6):
    Node_el7_1["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_5['x'])/(count-1), 'y': (Node_6['y'] - Node_5['y'])/(
            count-1)}

Node_el7_2 = {}
for count in range(4, 6):
    Node_el7_2["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_5['x'])*(2/(count-1)), 'y': (Node_6['y'] - Node_5[
        'y'])*(2/(count-1))}
else:
    Node_el7_2["nodes_per_el_3"] = Node_6

Node_el7_3 = {}
for count in range(5, 6):
    Node_el7_3["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_5['x'])*(3/(count-1)), 'y': (Node_6['y'] - Node_5[
        'y'])*(3/(count-1))}
else:
    Node_el7_3["nodes_per_el_4"] = Node_6

#Element 8 internal nodes
Node_el8_1 = {}
for count in range(3, 6):
    Node_el8_1["nodes_per_el_%s" % count] = {'x': (Node_7['x'] -
    Node_5['x'])/(count-1), 'y': (Node_7['y'] - Node_5['y'])/(
            count-1)}

Node_el8_2 = {}
for count in range(4, 6):
    Node_el8_2["nodes_per_el_%s" % count] = {'x': (Node_7['x'] -
    Node_5['x'])*(2/(count-1)), 'y': (Node_7['y'] - Node_5[
        'y'])*(2/(count-1))}
else:
    Node_el8_2["nodes_per_el_3"] = Node_7

Node_el8_3 = {}
for count in range(5, 6):
    Node_el8_3["nodes_per_el_%s" % count] = {'x': (Node_7['x'] -
    Node_5['x'])*(3/(count-1)), 'y': (Node_7['y'] - Node_5[
        'y'])*(3/(count-1))}
else:
    Node_el8_3["nodes_per_el_4"] = Node_7

#Element 9 internal nodes
Node_el9_1 = {}
for count in range(3, 6):
    Node_el9_1["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_6['x'])/(count-1), 'y': (Node_8['y'] - Node_6['y'])/(
            count-1)}

Node_el9_2 = {}
for count in range(4, 6):
    Node_el9_2["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_6['x'])*(2/(count-1)), 'y': (Node_8['y'] - Node_6[
        'y'])*(2/(count-1))}
else:
    Node_el9_2["nodes_per_el_3"] = Node_8

Node_el9_3 = {}
for count in range(5, 6):
    Node_el9_3["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_6['x'])*(3/(count-1)), 'y': (Node_8['y'] - Node_6[
        'y'])*(3/(count-1))}
else:
    Node_el9_3["nodes_per_el_4"] = Node_8

#Element 10 internal nodes
Node_el10_1 = {}
for count in range(3, 6):
    Node_el10_1["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_7['x'])/(count-1), 'y': (Node_8['y'] - Node_7['y'])/(
            count-1)}

Node_el10_2 = {}
for count in range(4, 6):
    Node_el10_2["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_7['x'])*(2/(count-1)), 'y': (Node_8['y'] - Node_7[
        'y'])*(2/(count-1))}
else:
    Node_el10_2["nodes_per_el_3"] = Node_8

Node_el10_3 = {}
for count in range(5, 6):
    Node_el10_3["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_7['x'])*(3/(count-1)), 'y': (Node_8['y'] - Node_7[
        'y'])*(3/(count-1))}
else:
    Node_el10_3["nodes_per_el_4"] = Node_8

#Element 11 internal nodes
Node_el11_1 = {}
for count in range(3, 6):
    Node_el11_1["nodes_per_el_%s" % count] = {'x': (Node_9['x'] -
    Node_7['x'])/(count-1), 'y': (Node_9['y'] - Node_7['y'])/(
            count-1)}

Node_el11_2 = {}
for count in range(4, 6):
    Node_el11_2["nodes_per_el_%s" % count] = {'x': (Node_9['x'] -
    Node_7['x'])*(2/(count-1)), 'y': (Node_9['y'] - Node_7[
        'y'])*(2/(count-1))}
else:
    Node_el11_2["nodes_per_el_3"] = Node_9

Node_el11_3 = {}
for count in range(5, 6):
    Node_el11_3["nodes_per_el_%s" % count] = {'x': (Node_9['x'] -
    Node_7['x'])*(3/(count-1)), 'y': (Node_9['y'] - Node_7[
        'y'])*(3/(count-1))}
else:
    Node_el11_3["nodes_per_el_4"] = Node_9

#Element 12 internal nodes
Node_el12_1 = {}
for count in range(3, 6):
    Node_el12_1["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_8['x'])/(count-1), 'y': (Node_10['y'] - Node_8['y'])/(
            count-1)}

Node_el12_2 = {}
for count in range(4, 6):
    Node_el12_2["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_8['x'])*(2/(count-1)), 'y': (Node_10['y'] - Node_8[
        'y'])*(2/(count-1))}
else:
    Node_el12_2["nodes_per_el_3"] = Node_10

Node_el12_3 = {}
for count in range(5, 6):
    Node_el12_3["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_8['x'])*(3/(count-1)), 'y': (Node_10['y'] - Node_8[
        'y'])*(3/(count-1))}
else:
    Node_el12_3["nodes_per_el_4"] = Node_10

#Element 13 internal nodes
Node_el13_1 = {}
for count in range(3, 6):
    Node_el13_1["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_9['x'])/(count-1), 'y': (Node_10['y'] - Node_9['y'])/(
            count-1)}

Node_el13_2 = {}
for count in range(4, 6):
    Node_el13_2["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_9['x'])*(2/(count-1)), 'y': (Node_10['y'] - Node_9[
        'y'])*(2/(count-1))}
else:
    Node_el1_13["nodes_per_el_3"] = Node_10

Node_el13_3 = {}
for count in range(5, 6):
    Node_el13_3["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_9['x'])*(3/(count-1)), 'y': (Node_10['y'] - Node_9[
        'y'])*(3/(count-1))}
else:
    Node_el13_3["nodes_per_el_4"] = Node_10

#--------------------------------------------------------------------

L = 1.5
Beta = 2*(2*math.pi/360)
cb = math.cos(Beta)

Elem_1_1 = {'n1': Node_1, 'n2': Node_el1_1}
Elem_1_2 = {'n1': Node_el1_1, 'n2': Node_el1_2}
Elem_1_3 = {'n1': Node_el1_2, 'n2': Node_el1_3}
Elem_1_4 = {'n1': Node_el1_3, 'n2': Node_2}

Length_Elem_1_el = {}
for count in range(3, 6):
    Length_Elem_1_el["nodes_per_el_%s" % count] = {(0.2*L)/(count-1)}



# Elem_1 = {'n1': Node_1, 'n2': Node_2, 'length': 0.2*L}
# Elem_2 = {'n1': Node_1, 'n2': Node_3, 'length': L}
# Elem_3 = {'n1': Node_2, 'n2': Node_4, 'length': L*cb}
# Elem_4 = {'n1': Node_3, 'n2': Node_4, 'length': (1/6)*L}
# Elem_5 = {'n1': Node_3, 'n2': Node_5, 'length': L}
# Elem_6 = {'n1': Node_4, 'n2': Node_6, 'length': L*cb}
# Elem_7 = {'n1': Node_5, 'n2': Node_6, 'length': (2/15)*L}
# Elem_8 = {'n1': Node_5, 'n2': Node_7, 'length': L}
# Elem_9 = {'n1': Node_6, 'n2': Node_8, 'length': L*cb}
# Elem_10 = {'n1': Node_7, 'n2': Node_8, 'length': (1/10)*L}
# Elem_11 = {'n1': Node_7, 'n2': Node_9, 'length': L}
# Elem_12 = {'n1': Node_8, 'n2': Node_10, 'length': L*cb}
# Elem_13 = {'n1': Node_9, 'n2': Node_10, 'length': (1/15)*L}

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

