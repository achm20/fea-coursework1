import math
import nodes_and_elems as nae

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
Node_1_2_1 = {}
for count in range(3, 6):
    Node_1_2_1["nodes_per_el_%s" % count] = {'x': (Node_2['x'] -
    Node_1['x'])/(count-1), 'y': (Node_2['y'] - Node_1['y'])/(
            count-1)}

Node_1_2_2 = {}
for count in range(4, 6):
    Node_1_2_2["nodes_per_el_%s" % count] = {'x': (Node_2['x'] -
    Node_1['x'])*(2/(count-1)), 'y': (Node_2['y'] - Node_1[
        'y'])*(2/(count-1))}
else:
    Node_1_2_2["nodes_per_el_3"] = Node_2

Node_1_2_3 = {}
for count in range(5, 6):
    Node_1_2_3["nodes_per_el_%s" % count] = {'x': (Node_2['x'] -
    Node_1['x'])*(3/(count-1)), 'y': (Node_2['y'] - Node_1[
        'y'])*(3/(count-1))}
else:
    Node_1_2_3["nodes_per_el_4"] = Node_2

#Element 2 internal nodes
Node_1_3_1 = {}
for count in range(3, 6):
    Node_1_3_1["nodes_per_el_%s" % count] = {'x': (Node_3['x'] -
    Node_1['x'])/(count-1), 'y': (Node_3['y'] - Node_1['y'])/(
            count-1)}

Node_1_3_2 = {}
for count in range(4, 6):
    Node_1_3_2["nodes_per_el_%s" % count] = {'x': (Node_3['x'] -
    Node_1['x'])*(2/(count-1)), 'y': (Node_3['y'] - Node_1[
        'y'])*(2/(count-1))}
else:
    Node_1_3_2["nodes_per_el_3"] = Node_3

Node_1_3_3 = {}
for count in range(5, 6):
    Node_1_3_3["nodes_per_el_%s" % count] = {'x': (Node_3['x'] -
    Node_1['x'])*(3/(count-1)), 'y': (Node_3['y'] - Node_1[
        'y'])*(3/(count-1))}
else:
    Node_1_3_3["nodes_per_el_4"] = Node_3

#Element 3 internal nodes
Node_2_4_1 = {}
for count in range(3, 6):
    Node_2_4_1["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_2['x'])/(count-1), 'y': (Node_4['y'] - Node_2['y'])/(
            count-1)}

Node_2_4_2 = {}
for count in range(4, 6):
    Node_2_4_2["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_2['x'])*(2/(count-1)), 'y': (Node_4['y'] - Node_2[
        'y'])*(2/(count-1))}
else:
    Node_2_4_2["nodes_per_el_3"] = Node_4

Node_2_4_3 = {}
for count in range(5, 6):
    Node_2_4_3["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_2['x'])*(3/(count-1)), 'y': (Node_4['y'] - Node_2[
        'y'])*(3/(count-1))}
else:
    Node_2_4_3["nodes_per_el_4"] = Node_4

#Element 4 internal nodes
Node_3_4_1 = {}
for count in range(3, 6):
    Node_3_4_1["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_3['x'])/(count-1), 'y': (Node_4['y'] - Node_3['y'])/(
            count-1)}

Node_3_4_2 = {}
for count in range(4, 6):
    Node_3_4_2["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_3['x'])*(2/(count-1)), 'y': (Node_4['y'] - Node_3[
        'y'])*(2/(count-1))}
else:
    Node_3_4_2["nodes_per_el_3"] = Node_4

Node_3_4_3 = {}
for count in range(5, 6):
    Node_3_4_3["nodes_per_el_%s" % count] = {'x': (Node_4['x'] -
    Node_3['x'])*(3/(count-1)), 'y': (Node_4['y'] - Node_3[
        'y'])*(3/(count-1))}
else:
    Node_3_4_3["nodes_per_el_4"] = Node_4

#Element 5 internal nodes
Node_3_5_1 = {}
for count in range(3, 6):
    Node_3_5_1["nodes_per_el_%s" % count] = {'x': (Node_5['x'] -
    Node_3['x'])/(count-1), 'y': (Node_5['y'] - Node_3['y'])/(
            count-1)}

Node_3_5_2 = {}
for count in range(4, 6):
    Node_3_5_2["nodes_per_el_%s" % count] = {'x': (Node_5['x'] -
    Node_3['x'])*(2/(count-1)), 'y': (Node_5['y'] - Node_3[
        'y'])*(2/(count-1))}
else:
    Node_3_5_2["nodes_per_el_3"] = Node_5

Node_3_5_3 = {}
for count in range(5, 6):
    Node_3_5_3["nodes_per_el_%s" % count] = {'x': (Node_5['x'] -
    Node_3['x'])*(3/(count-1)), 'y': (Node_5['y'] - Node_3[
        'y'])*(3/(count-1))}
else:
    Node_3_5_3["nodes_per_el_4"] = Node_5

#Element 6 internal nodes
Node_4_6_1 = {}
for count in range(3, 6):
    Node_4_6_1["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_4['x'])/(count-1), 'y': (Node_6['y'] - Node_4['y'])/(
            count-1)}

Node_4_6_2 = {}
for count in range(4, 6):
    Node_4_6_2["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_4['x'])*(2/(count-1)), 'y': (Node_6['y'] - Node_4[
        'y'])*(2/(count-1))}
else:
    Node_4_6_2["nodes_per_el_3"] = Node_6

Node_4_6_3 = {}
for count in range(5, 6):
    Node_4_6_3["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_4['x'])*(3/(count-1)), 'y': (Node_6['y'] - Node_4[
        'y'])*(3/(count-1))}
else:
    Node_4_6_3["nodes_per_el_4"] = Node_6

#Element 7 internal nodes
Node_5_6_1 = {}
for count in range(3, 6):
    Node_5_6_1["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_5['x'])/(count-1), 'y': (Node_6['y'] - Node_5['y'])/(
            count-1)}

Node_5_6_2 = {}
for count in range(4, 6):
    Node_5_6_2["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_5['x'])*(2/(count-1)), 'y': (Node_6['y'] - Node_5[
        'y'])*(2/(count-1))}
else:
    Node_5_6_2["nodes_per_el_3"] = Node_6

Node_5_6_3 = {}
for count in range(5, 6):
    Node_5_6_3["nodes_per_el_%s" % count] = {'x': (Node_6['x'] -
    Node_5['x'])*(3/(count-1)), 'y': (Node_6['y'] - Node_5[
        'y'])*(3/(count-1))}
else:
    Node_5_6_3["nodes_per_el_4"] = Node_6

#Element 8 internal nodes
Node_5_7_1 = {}
for count in range(3, 6):
    Node_5_7_1["nodes_per_el_%s" % count] = {'x': (Node_7['x'] -
    Node_5['x'])/(count-1), 'y': (Node_7['y'] - Node_5['y'])/(
            count-1)}

Node_5_7_2 = {}
for count in range(4, 6):
    Node_5_7_2["nodes_per_el_%s" % count] = {'x': (Node_7['x'] -
    Node_5['x'])*(2/(count-1)), 'y': (Node_7['y'] - Node_5[
        'y'])*(2/(count-1))}
else:
    Node_5_7_2["nodes_per_el_3"] = Node_7

Node_5_7_3 = {}
for count in range(5, 6):
    Node_5_7_3["nodes_per_el_%s" % count] = {'x': (Node_7['x'] -
    Node_5['x'])*(3/(count-1)), 'y': (Node_7['y'] - Node_5[
        'y'])*(3/(count-1))}
else:
    Node_5_7_3["nodes_per_el_4"] = Node_7

#Element 9 internal nodes
Node_6_8_1 = {}
for count in range(3, 6):
    Node_6_8_1["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_6['x'])/(count-1), 'y': (Node_8['y'] - Node_6['y'])/(
            count-1)}

Node_6_8_2 = {}
for count in range(4, 6):
    Node_6_8_2["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_6['x'])*(2/(count-1)), 'y': (Node_8['y'] - Node_6[
        'y'])*(2/(count-1))}
else:
    Node_6_8_2["nodes_per_el_3"] = Node_8

Node_6_8_3 = {}
for count in range(5, 6):
    Node_6_8_3["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_6['x'])*(3/(count-1)), 'y': (Node_8['y'] - Node_6[
        'y'])*(3/(count-1))}
else:
    Node_6_8_3["nodes_per_el_4"] = Node_8

#Element 10 internal nodes
Node_7_8_1 = {}
for count in range(3, 6):
    Node_7_8_1["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_7['x'])/(count-1), 'y': (Node_8['y'] - Node_7['y'])/(
            count-1)}

Node_7_8_2 = {}
for count in range(4, 6):
    Node_7_8_2["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_7['x'])*(2/(count-1)), 'y': (Node_8['y'] - Node_7[
        'y'])*(2/(count-1))}
else:
    Node_7_8_2["nodes_per_el_3"] = Node_8

Node_7_8_3 = {}
for count in range(5, 6):
    Node_7_8_3["nodes_per_el_%s" % count] = {'x': (Node_8['x'] -
    Node_7['x'])*(3/(count-1)), 'y': (Node_8['y'] - Node_7[
        'y'])*(3/(count-1))}
else:
    Node_7_8_3["nodes_per_el_4"] = Node_8

#Element 11 internal nodes
Node_7_9_1 = {}
for count in range(3, 6):
    Node_7_9_1["nodes_per_el_%s" % count] = {'x': (Node_9['x'] -
    Node_7['x'])/(count-1), 'y': (Node_9['y'] - Node_7['y'])/(
            count-1)}

Node_7_9_2 = {}
for count in range(4, 6):
    Node_7_9_2["nodes_per_el_%s" % count] = {'x': (Node_9['x'] -
    Node_7['x'])*(2/(count-1)), 'y': (Node_9['y'] - Node_7[
        'y'])*(2/(count-1))}
else:
    Node_7_9_2["nodes_per_el_3"] = Node_9

Node_7_9_3 = {}
for count in range(5, 6):
    Node_7_9_3["nodes_per_el_%s" % count] = {'x': (Node_9['x'] -
    Node_7['x'])*(3/(count-1)), 'y': (Node_9['y'] - Node_7[
        'y'])*(3/(count-1))}
else:
    Node_7_9_3["nodes_per_el_4"] = Node_9

#Element 12 internal nodes
Node_8_10_1 = {}
for count in range(3, 6):
    Node_8_10_1["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_8['x'])/(count-1), 'y': (Node_10['y'] - Node_8['y'])/(
            count-1)}

Node_8_10_2 = {}
for count in range(4, 6):
    Node_8_10_2["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_8['x'])*(2/(count-1)), 'y': (Node_10['y'] - Node_8[
        'y'])*(2/(count-1))}
else:
    Node_8_10_2["nodes_per_el_3"] = Node_10

Node_8_10_3 = {}
for count in range(5, 6):
    Node_8_10_3["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_8['x'])*(3/(count-1)), 'y': (Node_10['y'] - Node_8[
        'y'])*(3/(count-1))}
else:
    Node_8_10_3["nodes_per_el_4"] = Node_10

#Element 13 internal nodes
Node_9_10_1 = {}
for count in range(3, 6):
    Node_9_10_1["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_9['x'])/(count-1), 'y': (Node_10['y'] - Node_9['y'])/(
            count-1)}

Node_9_10_2 = {}
for count in range(4, 6):
    Node_9_10_2["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_9['x'])*(2/(count-1)), 'y': (Node_10['y'] - Node_9[
        'y'])*(2/(count-1))}
else:
    Node_9_10_1["nodes_per_el_3"] = Node_10

Node_9_10_3 = {}
for count in range(5, 6):
    Node_9_10_3["nodes_per_el_%s" % count] = {'x': (Node_10['x'] -
    Node_9['x'])*(3/(count-1)), 'y': (Node_10['y'] - Node_9[
        'y'])*(3/(count-1))}
else:
    Node_9_10_3["nodes_per_el_4"] = Node_10

#--------------------------------------------------------------------

L = 1.5
Beta = 2*(2*math.pi/360)
cb = math.cos(Beta)

#Element_1_x data
Elem_1_1 = {'n1': Node_1, 'n2': Node_1_2_1}
Elem_1_2 = {'n1': Node_1_2_1, 'n2': Node_1_2_2}
Elem_1_3 = {'n1': Node_1_2_2, 'n2': Node_1_2_3}
Elem_1_4 = {'n1': Node_1_2_3, 'n2': Node_2}

Length_Elem_1_el = {}
for count in range(3, 6):
    Length_Elem_1_el["nodes_per_el_%s" % count] = {'length': (0.2*L)/(
            count-1)}

#Element_2_x data
Elem_2_1 = {'n1': Node_1, 'n2': Node_1_3_1}
Elem_2_2 = {'n1': Node_1_3_1, 'n2': Node_1_3_2}
Elem_2_3 = {'n1': Node_1_3_2, 'n2': Node_1_3_3}
Elem_2_4 = {'n1': Node_1_3_3, 'n2': Node_3}

Length_Elem_2_el = {}
for count in range(3, 6):
    Length_Elem_2_el["nodes_per_el_%s" % count] = {'length': L/(count-1)}

#Element_3_x data
Elem_3_1 = {'n1': Node_2, 'n2': Node_2_4_1}
Elem_3_2 = {'n1': Node_2_4_1, 'n2': Node_2_4_2}
Elem_3_3 = {'n1': Node_2_4_2, 'n2': Node_2_4_3}
Elem_3_4 = {'n1': Node_2_4_3, 'n2': Node_4}

Length_Elem_3_el = {}
for count in range(3, 6):
    Length_Elem_3_el["nodes_per_el_%s" % count] = {'length': (L*cb)/(count-1)}

#Element_4_x data
Elem_4_1 = {'n1': Node_3, 'n2': Node_3_4_1}
Elem_4_2 = {'n1': Node_3_4_1, 'n2': Node_3_4_2}
Elem_4_3 = {'n1': Node_3_4_2, 'n2': Node_3_4_3}
Elem_4_4 = {'n1': Node_3_4_3, 'n2': Node_4}

Length_Elem_4_el = {}
for count in range(3, 6):
    Length_Elem_4_el["nodes_per_el_%s" % count] = {'length': ((1/6)*L)/(
            count-1)}

#Element_5_x data
Elem_5_1 = {'n1': Node_3, 'n2': Node_3_5_1}
Elem_5_2 = {'n1': Node_3_5_1, 'n2': Node_3_5_2}
Elem_5_3 = {'n1': Node_3_5_2, 'n2': Node_3_5_3}
Elem_5_4 = {'n1': Node_3_5_3, 'n2': Node_5}

Length_Elem_5_el = {}
for count in range(3, 6):
    Length_Elem_5_el["nodes_per_el_%s" % count] = {'length': L/(count-1)}

#Element_6_x data
Elem_6_1 = {'n1': Node_4, 'n2': Node_4_6_1}
Elem_6_2 = {'n1': Node_4_6_1, 'n2': Node_4_6_2}
Elem_6_3 = {'n1': Node_4_6_2, 'n2': Node_4_6_3}
Elem_6_4 = {'n1': Node_4_6_3, 'n2': Node_6}

Length_Elem_6_el = {}
for count in range(3, 6):
    Length_Elem_6_el["nodes_per_el_%s" % count] = {'length': (L*cb)/(count-1)}

#Element_7_x data
Elem_7_1 = {'n1': Node_5, 'n2': Node_5_6_1}
Elem_7_2 = {'n1': Node_5_6_1, 'n2': Node_5_6_2}
Elem_7_3 = {'n1': Node_5_6_2, 'n2': Node_5_6_3}
Elem_7_4 = {'n1': Node_5_6_3, 'n2': Node_6}

Length_Elem_7_el = {}
for count in range(3, 6):
    Length_Elem_7_el["nodes_per_el_%s" % count] = {'length': ((2/15)*L)/(
            count-1)}

#Element_8_x data
Elem_8_1 = {'n1': Node_5, 'n2': Node_5_7_1}
Elem_8_2 = {'n1': Node_5_7_1, 'n2': Node_5_7_2}
Elem_8_3 = {'n1': Node_5_7_2, 'n2': Node_5_7_3}
Elem_8_4 = {'n1': Node_5_7_3, 'n2': Node_7}

Length_Elem_8_el = {}
for count in range(3, 6):
    Length_Elem_8_el["nodes_per_el_%s" % count] = {'length': L/(count-1)}

#Element_9_x data
Elem_9_1 = {'n1': Node_6, 'n2': Node_6_8_1}
Elem_9_2 = {'n1': Node_6_8_1, 'n2': Node_6_8_2}
Elem_9_3 = {'n1': Node_6_8_2, 'n2': Node_6_8_3}
Elem_9_4 = {'n1': Node_6_8_3, 'n2': Node_8}

Length_Elem_9_el = {}
for count in range(3, 6):
    Length_Elem_9_el["nodes_per_el_%s" % count] = {'length': (L*cb)/(count-1)}

#Element_10_x data
Elem_10_1 = {'n1': Node_7, 'n2': Node_7_8_1}
Elem_10_2 = {'n1': Node_7_8_1, 'n2': Node_7_8_2}
Elem_10_3 = {'n1': Node_7_8_2, 'n2': Node_7_8_3}
Elem_10_4 = {'n1': Node_7_8_3, 'n2': Node_8}

Length_Elem_10_el = {}
for count in range(3, 6):
    Length_Elem_10_el["nodes_per_el_%s" % count] = {'length': ((1/10)*L)/(
            count-1)}

#Element_11_x data
Elem_11_1 = {'n1': Node_7, 'n2': Node_7_9_1}
Elem_11_2 = {'n1': Node_7_9_1, 'n2': Node_7_9_2}
Elem_11_3 = {'n1': Node_7_9_2, 'n2': Node_7_9_3}
Elem_11_4 = {'n1': Node_7_9_3, 'n2': Node_9}

Length_Elem_11_el = {}
for count in range(3, 6):
    Length_Elem_11_el["nodes_per_el_%s" % count] = {'length': L/(count-1)}

#Element_12_x data
Elem_12_1 = {'n1': Node_8, 'n2': Node_8_10_1}
Elem_12_2 = {'n1': Node_8_10_1, 'n2': Node_8_10_2}
Elem_12_3 = {'n1': Node_8_10_2, 'n2': Node_8_10_3}
Elem_12_4 = {'n1': Node_8_10_3, 'n2': Node_10}

Length_Elem_12_el = {}
for count in range(3, 6):
    Length_Elem_12_el["nodes_per_el_%s" % count] = {'length': (L*cb)/(count-1)}

#Element_13_x data
Elem_13_1 = {'n1': Node_9, 'n2': Node_9_10_1}
Elem_13_2 = {'n1': Node_9_10_1, 'n2': Node_9_10_2}
Elem_13_3 = {'n1': Node_9_10_2, 'n2': Node_9_10_3}
Elem_13_4 = {'n1': Node_9_10_3, 'n2': Node_10}

Length_Elem_13_el = {}
for count in range(3, 6):
    Length_Elem_13_el["nodes_per_el_%s" % count] = {'length': ((1/15)*L)/(
            count-1)}

l1 = (nae.Elem_1['n2']['x'] - nae.Elem_1['n1']['x'])/(nae.Elem_1['length'])
l2 = (nae.Elem_2['n2']['x'] - nae.Elem_2['n1']['x'])/(nae.Elem_2['length'])
l3 = (nae.Elem_3['n2']['x'] - nae.Elem_3['n1']['x'])/(nae.Elem_3['length'])
l4 = (nae.Elem_4['n2']['x'] - nae.Elem_4['n1']['x'])/(nae.Elem_4['length'])
l5 = (nae.Elem_5['n2']['x'] - nae.Elem_5['n1']['x'])/(nae.Elem_5['length'])
l6 = (nae.Elem_6['n2']['x'] - nae.Elem_6['n1']['x'])/(nae.Elem_6['length'])
l7 = (nae.Elem_7['n2']['x'] - nae.Elem_7['n1']['x'])/(nae.Elem_7['length'])
l8 = (nae.Elem_8['n2']['x'] - nae.Elem_8['n1']['x'])/(nae.Elem_8['length'])
l9 = (nae.Elem_9['n2']['x'] - nae.Elem_9['n1']['x'])/(nae.Elem_9['length'])
l10 = (nae.Elem_10['n2']['x'] - nae.Elem_10['n1']['x'])/(nae.Elem_10['length'])
l11 = (nae.Elem_11['n2']['x'] - nae.Elem_11['n1']['x'])/(nae.Elem_11['length'])
l12 = (nae.Elem_12['n2']['x'] - nae.Elem_12['n1']['x'])/(nae.Elem_12['length'])
l13 = (nae.Elem_13['n2']['x'] - nae.Elem_13['n1']['x'])/(nae.Elem_13['length'])

m1 = (nae.Elem_1['n2']['y'] - nae.Elem_1['n1']['y']) / (nae.Elem_1['length'])
m2 = (nae.Elem_2['n2']['y'] - nae.Elem_2['n1']['y']) / (nae.Elem_2['length'])
m3 = (nae.Elem_3['n2']['y'] - nae.Elem_3['n1']['y']) / (nae.Elem_3['length'])
m4 = (nae.Elem_4['n2']['y'] - nae.Elem_4['n1']['y']) / (nae.Elem_4['length'])
m5 = (nae.Elem_5['n2']['y'] - nae.Elem_5['n1']['y']) / (nae.Elem_5['length'])
m6 = (nae.Elem_6['n2']['y'] - nae.Elem_6['n1']['y']) / (nae.Elem_6['length'])
m7 = (nae.Elem_7['n2']['y'] - nae.Elem_7['n1']['y']) / (nae.Elem_7['length'])
m8 = (nae.Elem_8['n2']['y'] - nae.Elem_8['n1']['y']) / (nae.Elem_8['length'])
m9 = (nae.Elem_9['n2']['y'] - nae.Elem_9['n1']['y']) / (nae.Elem_9['length'])
m10 = (nae.Elem_10['n2']['y'] - nae.Elem_10['n1']['y']) / (nae.Elem_10['length'])
m11 = (nae.Elem_11['n2']['y'] - nae.Elem_11['n1']['y']) / (nae.Elem_11['length'])
m12 = (nae.Elem_12['n2']['y'] - nae.Elem_12['n1']['y']) / (nae.Elem_12['length'])
m13 = (nae.Elem_13['n2']['y'] - nae.Elem_13['n1']['y']) / (nae.Elem_13['length'])

