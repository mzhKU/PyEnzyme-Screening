#!/usr/bin/env python

# ****************************************************
# Fix reacting atoms in interpolation input files.
#
# DESCRIPTION
# - Determine line number of reacting atom relative
#   to other atoms of the residue.
# - 'variable': Atom is within enzyme sequence and can
#               change in line number when mutations
#               are added.
# - 'constant': Atom is independent of mutations and
#               ususally is constantly offset from
#               last atom line (see 'offset')
# - 'offset':   Line number of last atom in structure
#               minus line number of atom above
#               atom to constrain.
# ****************************************************

# CALLING SEQUENCE:
# $ python fix_reacting_atoms.py $<.mop>

import sys
inp=sys.argv[1]

# ----------------------------------------------------
# ADJUST:
# 'resi': Residue ID (PyMOL convention)
# 'rel_pos': Relative position of atom within residue,
#            starting with 'cnt' = 1.
resi_to_fix = '78'
rel_pos = 9
offset  = 32
# ----------------------------------------------------

# Original file
dat=open(inp, 'r')
val=dat.readlines()
dat.close()

# Internal counter
cnt = 1

tmp=open(inp+'.tmp', 'w')
line_to_constrain = len(val) - offset
# Fix variable atom (enzyme)
for i in enumerate(val):
    # Identify atom line if not keyword line, new line or empty string line
    if ("charge" not in val[i[0]]) and (val[i[0]] != '\n') and (val[i[0]].strip()):
        close_par= i[1].find(")")
        resi = i[1][close_par-3:close_par].strip()
        if resi == resi_to_fix:
            print "Res:", resi
            if cnt == rel_pos:
                print i[1].replace("+1", "+0")
                tmp.write(i[1].replace("+1", "+0"))
            else:
                tmp.write(i[1])
            cnt+=1
        elif i[0] == line_to_constrain:
            print i[1].replace("+1", "+0")
            tmp.write(i[1].replace("+1", "+0"))
        else:
            tmp.write(i[1])
    # Keyword or new line
    else:
        tmp.write(i[1])
tmp.close()
