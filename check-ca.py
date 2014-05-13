from pymol import cmd, CmdException
from pymol import stored
import os.path

# Writes script 'fix-rest-ca.py' to run on command line,
# set optimization constraints of residues in selection.
# Mainly used for setting constraints of
# mutant structure optimization,
# constrained WT optimization is configured
# with 'format_mopac.py' script.

# Restrictions:
# - Loaded PDB file name must be of pattern
#   '<State>-res-<Mutation>-ste-ini.pdb', where
#   <State>:    Integer representing the species of the reaction,
#               eg. '1' for ES complex, '3' for intermediate
#   <Mutation>: Eg. N35F
# - Reference position (substrate) must be properly labeled.

# Requires:
# Loaded structure '<LABEL>-<GNORM>-<CUTOFF>.mop'

# CALLING SEQUENCE (No komma between function and argument):
# PyMOL> check_rest_ca_resi <REF>

# Arguments
optimize_within_radius = '10.0'

def check_rest_ca_resi(reference):
    objects = cmd.get_names('objects')
    constrained=[]
    for ob in objects:
        # Local storage.
        stored.rest_ca_wat = []
        # Reference object for selection expansion and invert selection.  
        cmd.select("sub", '/' + ob + '///' + reference + '/')
        cmd.select("rest", "(byres (sub expand %s))" % optimize_within_radius)
        cmd.select("rest", "((byobj sub) and not rest)")
        # Select all alpha carbons and waters of the current object.
        cmd.select("rest_ca_wat", "(rest and name ca) or (rest and resn HOH)")
        # Collect alpha carbon resn.
        cmd.iterate("rest_ca_wat", "stored.rest_ca_wat.append(resi)") 
        write_fix(stored.rest_ca_wat, ob, optimize_within_radius)

def write_fix(rest_ca_wat, ob, optimize_within_radius):
    s = """\
residues_to_fix = %s\n\
import sys\n\
from os.path import splitext \n\
opt_dat = open(sys.argv[1], 'r')\n\
opt_val = opt_dat.readlines()\n\
opt_dat.close()\n\
mop_string = ''\n\
tmp_dat = open(sys.argv[1], 'w')\n\
print "Fixing side chains in:", splitext(sys.argv[1])[0]\n\
for line in opt_val:\n\
    if len(line.split()) != 0:\n\
        # '-1' required to discard ')' character from MOPAC residue label
        if line.split()[3][:-1] in residues_to_fix:\n\
            #mop_string += line[:34] + '0' + line[35:50] + '0' + line[51:66] + '0' + line[67:]\n\
            mop_string += line.replace("+1", "+0")
        else:\n\
            mop_string += line\n\
    else:\n\
        mop_string += line\n\
tmp_dat.write(mop_string)\n\
tmp_dat.close()
""" % rest_ca_wat
    print s
    d=open('fix-%s-%s.py' % (os.path.splitext(ob)[0], optimize_within_radius), 'w')
    d.write(s)
    d.close()

cmd.extend('check_rest_ca_resi', check_rest_ca_resi)
