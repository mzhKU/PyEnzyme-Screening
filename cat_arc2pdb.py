#!/usr/bin/env python

# DESCRIPTION:
# - Linear interpolation between the two given structures in MOPAC
#   format and combine into one PDB file for viewing in PyMOL.

# ARGUMENTS:
# - Initial/Final State: MOPAC '.arc' files, header deleted,
#                        only initial keyword line remained
#                        and coordinates
# - Name

# REQUIRES:
# - PDB files of optimized reactant/product state ('HEADER', 'TER' and 'END' records discarded)
#   in working directory for correct PDB label writing

# CALLING SEQUENCE:
# $ python cat_arc2pdb.py $<starting_state.arc> $<final_state.arc> $name

import sys
reac, prod, name = sys.argv[1], sys.argv[2], sys.argv[3]

react_data, inter_data = open(reac, 'r'), open(prod, 'r') 
react_value, inter_value = react_data.readlines(), inter_data.readlines() 

react_pdb_data, inter_pdb_data = open(reac[:-3]+'pdb', 'r'), open(prod[:-3]+'pdb', 'r')
react_pdb_val, inter_pdb_val = react_pdb_data.readlines(), inter_pdb_data.readlines()

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

# Control
print 'Number of vectors in the diff-list:', len(diff)

# Run over n interpolation frames i
for i in range(n): 
    # Current interpolation frame
    set = []
    # Run over atoms of current interpolation frame i
    atm_cnt = 0
    for k in enumerate(react_value):
        if ("charge" not in inter_value[k[0]]) and (inter_value[k[0]] != '\n') and (inter_value[k[0]].strip()):
            xi = float(react_value[k[0]][20:32]) + diff_frac[atm_cnt][0]*i
            yi = float(react_value[k[0]][36:48]) + diff_frac[atm_cnt][1]*i
            zi = float(react_value[k[0]][52:64]) + diff_frac[atm_cnt][2]*i
            set.append('%6.3f %7.3f %7.3f' % (xi, yi, zi))
            atm_cnt += 1
    interpolation.append(set)

print 'len(interpolation)', len(interpolation)
print 'len(set)', len(set)

def make_cat_file(name):
    write_PDB_file = open('polation-%s.pdb' % name, 'w')
    step=1
    for model in interpolation:
        write_string = ''
        write_string += 'MODEL %s\n' % str(step)
        atm_cnt = 0
        for atom in model:
            write_string += react_pdb_val[atm_cnt][:31] + atom + react_pdb_val[atm_cnt][54:]
            atm_cnt += 1
        write_string += 'ENDMDL\n'
        step+=1
        write_PDB_file.write(write_string)
    write_PDB_file.close()

make_cat_file(name)
