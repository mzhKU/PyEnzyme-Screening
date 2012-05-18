from pymol import cmd
from pymol import stored
from pymol.exporting import _resn_to_aa as one_letter

# *****************************************************************
# Saving every residue to separate file.
# Working example Thomas Holder.
# -----------------------------------------------------------------


# *****************************************************************
# CALLING SEQUENCE:
# PyMOL> run seq.py
# PyMOL> seq
# -----------------------------------------------------------------


# *****************************************************************
def seq(state, selection="name ca or resn hoh or resn lig"):
    print "Generating seqs."
    cmd.select("prot", selection)
    while cmd.pop("_tmp", "prot"):
        cmd.iterate("_tmp", "stored.x=(resn,resv)")
        #print stored.x[0], stored.x[1]

        # Special case 1: Waters.
        if stored.x[0] == 'HOH':
            filename = 'seq-x%s-%s.pdb' % (stored.x[1], state)
        # Special case 2: Substrate.
        elif stored.x[0] == 'LIG':
            filename = 'seq-x%s-%s.pdb' % (stored.x[1], state)
        # Other: protein back-bone.
        else:
            filename = 'seq-%s%d-%s.pdb' % (one_letter[stored.x[0]].lower(), stored.x[1], state)
        cmd.save(filename, "byres _tmp")
    cmd.delete('_tmp prot')

cmd.extend('seq', seq)
# ----------------------------------------------------------------- 
