#!/usr/bin/python

# **************************************************
# ..................................................
# Fix selected side chains.
# ..................................................
# **************************************************


# DESCRIPTION:
# The script loads the 'opt.mop' file and sets the
# optimization flags to '+0', i.e. constrains the
# atom.

# PARAMETERS:
# Choose the side chains in the list below:
residues_to_fix = [
        '38'
        # '50',
        #'133',
        #'156',
        #         '277',
        #         '280'
                  ]

# CALLING SEQUENCE:
# python fix.py 1-3-opt-*.mop

import sys
from os.path import splitext 

opt_dat = open(sys.argv[1], 'r')
opt_val = opt_dat.readlines()
opt_dat.close()

mop_string = ''

tmp_dat = open(sys.argv[1], 'w')
print "Fixing side chains in:", splitext(sys.argv[1])[0]

for line in opt_val:
    # Only consider lines with more than 4 elements,
    # ends up being lines with atom data.
    if len(line.split()) != 0:
        # Discard the last character of the '3' element,
        # its a closing brace ')'.
        if line.split()[3][:-1] in residues_to_fix:
            # Replace the optimization flags.
            mop_string += line[:34] + '0' + line[35:50] + '0' + line[51:66] + '0' + line[67:]
        else:
            mop_string += line
    else:
        mop_string += line
    
tmp_dat.write(mop_string)
tmp_dat.close()



