#!/usr/bin/env python

# Resequence back bone files for sequential load in PyMOL

# Warning: Modifies file names!

import os
seq_orig_labeled = os.listdir(os.getcwd())
seq_zero_labeled = []

def reseq():
    for so in seq_orig_labeled:
        if len(so.split('-')) == 3 and '-1.pdb' in so:
            so_ini = so.split('-')[1][0]
            so_resi = int(so.split('-')[1][1:])
            sz = "%03d-seq-%s.pdb" % (so_resi, so_ini)
            sz_f = open(sz, 'w')
            seq_orig_dat = open(so, 'r')
            seq_orig_val = seq_orig_dat.readlines()
            for l in seq_orig_val:
                sz_f.write(l)
            seq_orig_dat.close()
            sz_f.close()

#reseq()
