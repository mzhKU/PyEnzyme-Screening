#!/usr/bin/env python

# Compare predicted and computed overall charge of double mutants.

# FUNCTIONALITY:
# Possible changes in charge are defined initially, program sums up changes.
# Identify mutations from file name.

WT_charge = 4

# |dQ| = 0
dQ_is_zero      = [
                   # A to X
                   ('A', 'N'), ('A', 'C'), ('A', 'Q'),
                   ('A', 'G'), ('A', 'H'), ('A', 'I'),
                   ('A', 'L'), ('A', 'M'), ('A', 'F'),
                   ('A', 'P'), ('A', 'S'), ('A', 'T'),
                   ('A', 'W'), ('A', 'Y'), ('A', 'V'),

                   # N to X
                   ('N', 'A'), ('N', 'C'), ('N', 'Q'),
                   ('N', 'G'), ('N', 'H'), ('N', 'I'),
                   ('N', 'L'), ('N', 'M'), ('N', 'F'),
                   ('N', 'P'), ('N', 'S'), ('N', 'T'),
                   ('N', 'W'), ('N', 'Y'), ('N', 'V'),

                   # C to X
                   ('C', 'N'), ('C', 'A'), ('C', 'Q'),
                   ('C', 'G'), ('C', 'H'), ('C', 'I'),
                   ('C', 'L'), ('C', 'M'), ('C', 'F'),
                   ('C', 'P'), ('C', 'S'), ('C', 'T'),
                   ('C', 'W'), ('C', 'Y'), ('C', 'V'),

                   # Q to X
                   ('Q', 'N'), ('Q', 'C'), ('Q', 'A'),
                   ('Q', 'G'), ('Q', 'H'), ('Q', 'I'),
                   ('Q', 'L'), ('Q', 'M'), ('Q', 'F'),
                   ('Q', 'P'), ('Q', 'S'), ('Q', 'T'),
                   ('Q', 'W'), ('Q', 'Y'), ('Q', 'V'),

                   # G to X
                   ('G', 'N'), ('G', 'C'), ('G', 'Q'),
                   ('G', 'A'), ('G', 'H'), ('G', 'I'),
                   ('G', 'L'), ('G', 'M'), ('G', 'F'),
                   ('G', 'P'), ('G', 'S'), ('G', 'T'),
                   ('G', 'W'), ('G', 'Y'), ('G', 'V'),

                   # H to X
                   ('H', 'N'), ('H', 'C'), ('H', 'Q'),
                   ('H', 'G'), ('H', 'A'), ('H', 'I'),
                   ('H', 'L'), ('H', 'M'), ('H', 'F'),
                   ('H', 'P'), ('H', 'S'), ('H', 'T'),
                   ('H', 'W'), ('H', 'Y'), ('H', 'V'),

                   # I to X
                   ('I', 'N'), ('I', 'C'), ('I', 'Q'),
                   ('I', 'G'), ('I', 'H'), ('I', 'A'),
                   ('I', 'L'), ('I', 'M'), ('I', 'F'),
                   ('I', 'P'), ('I', 'S'), ('I', 'T'),
                   ('I', 'W'), ('I', 'Y'), ('I', 'V'),

                   # L to X
                   ('L', 'N'), ('L', 'C'), ('L', 'Q'),
                   ('L', 'G'), ('L', 'H'), ('L', 'I'),
                   ('L', 'A'), ('L', 'M'), ('L', 'F'),
                   ('L', 'P'), ('L', 'S'), ('L', 'T'),
                   ('L', 'W'), ('L', 'Y'), ('L', 'V'),

                   # M to X
                   ('M', 'N'), ('M', 'C'), ('M', 'Q'),
                   ('M', 'G'), ('M', 'H'), ('M', 'I'),
                   ('M', 'L'), ('M', 'A'), ('M', 'F'),
                   ('M', 'P'), ('M', 'S'), ('M', 'T'),
                   ('M', 'W'), ('M', 'Y'), ('M', 'V'),

                   # F to X
                   ('F', 'N'), ('F', 'C'), ('F', 'Q'),
                   ('F', 'G'), ('F', 'H'), ('F', 'I'),
                   ('F', 'L'), ('F', 'M'), ('F', 'A'),
                   ('F', 'P'), ('F', 'S'), ('F', 'T'),
                   ('F', 'W'), ('F', 'Y'), ('F', 'V'),

                   # P to X
                   ('P', 'N'), ('P', 'C'), ('P', 'Q'),
                   ('P', 'G'), ('P', 'H'), ('P', 'I'),
                   ('P', 'L'), ('P', 'M'), ('P', 'F'),
                   ('P', 'P'), ('P', 'S'), ('P', 'T'),
                   ('P', 'W'), ('P', 'Y'), ('P', 'V'),

                   # S to X
                   ('S', 'N'), ('S', 'C'), ('S', 'Q'),
                   ('S', 'G'), ('S', 'H'), ('S', 'I'),
                   ('S', 'L'), ('S', 'M'), ('S', 'F'),
                   ('S', 'P'), ('S', 'A'), ('S', 'T'),
                   ('S', 'W'), ('S', 'Y'), ('S', 'V'),

                   # T to X
                   ('T', 'N'), ('T', 'C'), ('T', 'Q'),
                   ('T', 'G'), ('T', 'H'), ('T', 'I'),
                   ('T', 'L'), ('T', 'M'), ('T', 'F'),
                   ('T', 'P'), ('T', 'S'), ('T', 'A'),
                   ('T', 'W'), ('T', 'Y'), ('T', 'V'),

                   # W to X
                   ('W', 'N'), ('W', 'C'), ('W', 'Q'),
                   ('W', 'G'), ('W', 'H'), ('W', 'I'),
                   ('W', 'L'), ('W', 'M'), ('W', 'F'),
                   ('W', 'P'), ('W', 'S'), ('W', 'T'),
                   ('W', 'A'), ('W', 'Y'), ('W', 'V'),

                   # Y to X
                   ('Y', 'N'), ('Y', 'C'), ('Y', 'Q'),
                   ('Y', 'G'), ('Y', 'H'), ('Y', 'I'),
                   ('Y', 'L'), ('Y', 'M'), ('Y', 'F'),
                   ('Y', 'P'), ('Y', 'S'), ('Y', 'T'),
                   ('Y', 'W'), ('Y', 'Y'), ('Y', 'V'),

                   # V to X
                   ('V', 'N'), ('V', 'C'), ('V', 'Q'),
                   ('V', 'G'), ('V', 'H'), ('V', 'I'),
                   ('V', 'L'), ('V', 'M'), ('V', 'F'),
                   ('V', 'P'), ('V', 'S'), ('V', 'T'),
                   ('V', 'W'), ('V', 'Y'), ('V', 'A'),

                   # K to R
                   ('K', 'R'),
                   
                   # R to K
                   ('R', 'K')]

# |dQ| = 1
dQ_is_plus_one  = [('A', 'K'), ('A', 'R'),
                   ('N', 'K'), ('N', 'R'),
                   ('C', 'K'), ('C', 'R'),
                   ('Q', 'K'), ('Q', 'R'),
                   ('G', 'K'), ('G', 'R'),
                   ('H', 'K'), ('H', 'R'),
                   ('I', 'K'), ('I', 'R'),
                   ('L', 'K'), ('L', 'R'),
                   ('M', 'K'), ('M', 'R'),
                   ('F', 'K'), ('F', 'R'),
                   ('P', 'K'), ('P', 'R'),
                   ('S', 'K'), ('S', 'R'),
                   ('T', 'K'), ('T', 'R'),
                   ('W', 'K'), ('W', 'R'),
                   ('Y', 'K'), ('Y', 'R'),
                   ('V', 'K'), ('V', 'R')]

dQ_is_minus_one  = [('A', 'D'), ('A', 'E'),
                    ('N', 'D'), ('N', 'E'),
                    ('C', 'D'), ('C', 'E'),
                    ('Q', 'D'), ('Q', 'E'),
                    ('G', 'D'), ('G', 'E'),
                    ('H', 'D'), ('H', 'E'),
                    ('I', 'D'), ('I', 'E'),
                    ('L', 'D'), ('L', 'E'),
                    ('M', 'D'), ('M', 'E'),
                    ('F', 'D'), ('F', 'E'),
                    ('P', 'D'), ('P', 'E'),
                    ('S', 'D'), ('S', 'E'),
                    ('T', 'D'), ('T', 'E'),
                    ('W', 'D'), ('W', 'E'),
                    ('Y', 'D'), ('Y', 'E'),
                    ('V', 'D'), ('V', 'E')]
 
# |dQ| = 2
dQ_is_plus_two  = [('D', 'K'), ('D', 'R'),
                   ('E', 'K'), ('E', 'R')]

dQ_is_minus_two = [('K', 'D'), ('K', 'E'),
                   ('R', 'D'), ('R', 'E')]

# 1) Get mutations from file name
import sys
input = sys.argv[1]
name = input.split('-')[3:5]
#print (name[0][0], name[0][-1]), (name[1][0], name[1][-1])

# 2) Get dQ corresponding to mutations
dQ = 0
if (name[0][0], name[0][-1]) in dQ_is_zero:
    dQ += 0
if (name[0][0], name[0][-1]) in dQ_is_plus_one:
    dQ += 1
if (name[0][0], name[0][-1]) in dQ_is_minus_one:
    dQ -= 1
if (name[0][0], name[0][-1]) in dQ_is_plus_two:
    dQ += 2
if (name[0][0], name[0][-1]) in dQ_is_minus_two:
    dQ -= 2
if (name[1][0], name[1][-1]) in dQ_is_zero:
    dQ += 0
if (name[1][0], name[1][-1]) in dQ_is_plus_one:
    dQ += 1
if (name[1][0], name[1][-1]) in dQ_is_minus_one:
    dQ -= 1
if (name[1][0], name[1][-1]) in dQ_is_plus_two:
    dQ += 2
if (name[1][0], name[1][-1]) in dQ_is_minus_two:
    dQ -= 2

# 3) Compare predicted and computed charge
computed_charge = 'COMPUTED CHARGE'
dat=open(sys.argv[1], 'r')
val=dat.readlines()
import re
import sys
for line in val:
    if re.search(computed_charge, line):
        #     Predicted     Computed
        print name, WT_charge+dQ, line.split()[-1]
        #if WT_charge+dQ != int(line.split()[-1]):
        #    print name
