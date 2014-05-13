#!/usr/bin/python

# Replace ID of residue <x> by internal residue counter.

import sys

# INPUT
# File to modify (1) and template (2)
file1=sys.argv[1]
file2=sys.argv[2]
#residue_to_modify = 'GLU A  78'
residue_to_modify = 'UNK A  78'

# CALLING SEQUENCE:
# $ python changenum.py <file_to_modify> <template> [> <redirect]

# Example:
# ATOM   1125  N   GLU A  78      26.151  24.600  35.425  1.00  0.00 
# ATOM   1126  CA  GLU A  78      27.346  24.685  34.554  1.00  0.00 
# ATOM   1127  C   GLU A  78      26.823  24.309  33.149  1.00  0.00 
# [...]

# becomes
# ATOM      1  N   GLU A  78      26.151  24.600  35.425  1.00  0.00 
# ATOM      2  CA  GLU A  78      27.346  24.685  34.554  1.00  0.00 
# ATOM      3  C   GLU A  78      26.823  24.309  33.149  1.00  0.00 
# [...]

# Algorithm outline:
# (1) Read original input
# (2) if current input not residue to modify:
#         pass
#     else:
#         modify residue ID and keep coordinate data

dat_orig=open(file1, 'r')
val_orig=dat_orig.readlines()

dat_temp=open(file2, 'r')
val_temp=dat_temp.readlines()

cnt_orig=0
cnt_temp=0
for l in val_orig:
    if l[17:26] == residue_to_modify and (cnt_temp < len(val_temp)): 
        # Replace ID and keep original geometry
        val_orig[cnt_orig] = l[0:4] + val_temp[cnt_temp][4:17] + l[17:]
        cnt_temp+=1
    cnt_orig+=1
for i in val_orig:
    print i,
