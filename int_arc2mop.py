#!/usr/bin/env python

# DESCRIPTION:
# - Linear interpolation between the two given structures in MOPAC
#   format and combine into one PDB file for viewing in PyMOL.
# - Preserves optimization flags "+0/+1" and writes in '.arc' format

# ARGUMENTS:
# - Initial/Final State: MOPAC '.arc' files, header deleted,
#                        only initial keyword line remained
#                        and coordinates
# - Name

# CALLING SEQUENCE:
# $ python cat_arc2pdb.py $starting_state $final_state $name

import sys
reac, prod, name = sys.argv[1], sys.argv[2], sys.argv[3]

react_data, inter_data = open(reac, 'r'), open(prod, 'r') 
react_value, inter_value = react_data.readlines(), inter_data.readlines() 

n = 10
diff = []
diff_frac = []
interpolation = [] 

# Run over coordinates
for i in enumerate(react_value): 
    # Change in each coordinate for every atom.
    if ("charge" not in inter_value[i[0]]) and (inter_value[i[0]] != '\n') and (inter_value[i[0]].strip()):
        dx, dy, dz =\
        "%12.8f" % (float(inter_value[i[0]][20:32]) - float(react_value[i[0]][20:32])),\
        "%12.8f" % (float(inter_value[i[0]][36:48]) - float(react_value[i[0]][36:48])),\
        "%12.8f" % (float(inter_value[i[0]][52:64]) - float(react_value[i[0]][52:64]))
        diff.append([dx, dy, dz])

# Divide translation distance of
# atom_i^{prod, [x, y, z]} - atom_i^{reac, [x, y, z]}
# by number of interpolation frames
for atom_diff in diff:
    diff_frac.append([float(c)/float(n) for c in atom_diff]) 

# Run over n interpolation frames i
for i in range(n): 
    # Current interpolation frame
    set = []
    # Run over atoms of current interpolation frame i
    atm_cnt = 0
    for k in enumerate(react_value):
        # ''.strip() evaluates to False.
        if ("charge" not in inter_value[k[0]]) and (inter_value[k[0]] != '\n') and (inter_value[k[0]].strip()):
            xi = float(react_value[k[0]][20:32]) + diff_frac[atm_cnt][0]*i
            yi = float(react_value[k[0]][36:48]) + diff_frac[atm_cnt][1]*i
            zi = float(react_value[k[0]][52:64]) + diff_frac[atm_cnt][2]*i
            set.append('%6.3f %7.3f %7.3f' % (xi, yi, zi))
            atm_cnt += 1
    interpolation.append(set)

# Control
print 'Number of vectors in the diff-list:', len(diff)
print 'len(interpolation)', len(interpolation)
print 'len(set)', len(set)

def make_MOPAC_files(name):
    step=1
    for model in interpolation:
        write_mop_file = open('1-3-opt-%s-%03i.mop' % (name.upper(),step), 'w')
        write_string_mop = ''
        # Include keyword line
        write_string_mop += react_value[0] + '\n\n'
        atm_cnt = 0
        for atom in model:
            write_string_mop += react_value[atm_cnt+3][:21]\
                                + atom[:7]\
                                + react_value[atm_cnt+3][33:35]\
                                + atom[7:15]\
                                + react_value[atm_cnt+3][49:51]\
                                + atom[15:23]\
                                + react_value[atm_cnt+3][64:67] + '\n'
            atm_cnt += 1
        write_mop_file.write(write_string_mop)
        step+=1
        write_mop_file.close()

make_MOPAC_files(name)
