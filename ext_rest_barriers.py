#!/usr/bin/python
max_heat = 11.24

# ******************************
# Parse normalized heat files and list barriers.
# ..............................


# ******************************
# Calling sequence
# $ python ext_rest_barriers.py <normalized_heat.dat>
# ..............................

# Inconclusive barriers with the following mutants:

inconclusive = [
# Methly substrate.
#'G39A-W104Y',
#'G39A-I189A',
#'G39A-A141Q',
#'G39A-A141N',
#'W104F-A141N',
#'T103G-A141Q',
#'T103G-A141N',
#'A141Q-I189N',
#'A141N-L278A',
#'T103G-W104Q-A141N',
#'T103G-W104Y-A141Q',
#'T103G-W104Y-I189A',
#'W104F-A141N-I189A',
#'W104F-A141N-I189N',
#'W104F-A141N-L278A',
#'W104F-A141Q-I189Q',
#'W104Q-A141Q-L278A',
#'W104Y-A141Q-I189Q',
#'G39A-A141N-L278A',
#'G39A-A141Q-I189A',
#'G39A-A141Q-I189N',
#'G39A-A141Q-L278A',
#'G39A-T103G-A141Q',
#'G39A-W104Y-I189N',
#'G39A-W104Y-L278A',
#'G39A-I189N-L278A',
#'T103G-W104F-A141Q-I189Q',
#'T103G-W104Y-A141Q-I189A',
#'T103G-W104Y-A141Q-I189Q',
#'G39A-A141N-I189A-L278A',
#'G39A-A141Q-I189A-L278A',
#'G39A-T103G-W104F-A141Q',
#'G39A-T103G-W104Y-A141Q',
#'G39A-T103G-W104Y-L278A',
#'G39A-W104F-A141Q-I189N',
#'G39A-W104F-A141Q-I189Q',
#'G39A-W104Y-A141N-L278A',
#'G39A-W104Y-A141Q-L278A',

# Chlorine substrate:
# Set S: No profiles discarded 
# Set L:
'I189A-L278A',
'T103G-I189Y',
'W104Y-I189N',
'G39A-I189H',
'T103G-I189H-L278A',
'T103G-I189N-L278A',
'T103G-I189Y-L278A',
'T103G-W104F-A141Q',
'T103G-W104F-I189N',
'T103G-W104Q-I189Y',
'T103G-W104Y-A141N',
'T103G-W104Y-I189Y',
'W104Y-A141Q-I189H',
'W104Y-I189G-L278A',
'W104Y-I189Y-L278A',
'G39A-T103G-A141N',
'G39A-T103G-I189H',
'G39A-T103G-I189N',
'G39A-W104F-I189G',
'G39A-W104Y-A141N',
'G39A-W104Y-I189H',
'G39A-W104Y-I189N',
'G39A-A141N-I189H',
'G39A-A141Q-I189H',
'G39A-I189N-L278A',
'T103G-A141N-I189A-L278A',
'T103G-A141N-I189H-L278A',
'T103G-A141Q-I189A-L278A',
'T103G-W104F-A141N-I189H',
'T103G-W104F-A141Q-L278A',
'T103G-W104F-I189G-L278A',
'T103G-W104F-I189H-L278A',
'T103G-W104F-I189N-L278A',
'T103G-W104F-I189Y-L278A',
'T103G-W104Y-A141N-I189A',
'T103G-W104Y-A141N-I189H',
'T103G-W104Y-I189A-L278A',
'T103G-W104Y-I189N-L278A',
'T103G-W104Y-I189Y-L278A',
'W104Q-A141Q-I189N-L278A',
'W104Y-A141N-I189H-L278A',
'W104Y-A141Q-I189G-L278A',
'G39A-A141Q-I189H-L278A',
'G39A-A141Q-I189N-L278A',
'G39A-T103G-A141N-I189A',
'G39A-T103G-A141N-I189H',
'G39A-T103G-A141N-I189N',
'G39A-T103G-A141N-L278A',
'G39A-T103G-A141Q-I189N',
'G39A-T103G-A141Q-L278A',
'G39A-T103G-I189H-L278A',
'G39A-T103G-I189N-L278A',
'G39A-T103G-I189Y-L278A',
'G39A-T103G-W104F-I189N',
'G39A-T103G-W104Y-I189H',
'G39A-T103G-W104Y-I189N',
'G39A-T103G-W104Y-I189Y',
'G39A-W104F-A141Q-I189G',
'G39A-W104Q-A141Q-I189G',
'G39A-W104Q-I189G-L278A',
'G39A-W104Y-I189N-L278A',

# 22.08.2012: Additional mutants from NZ April 2012 assay.
'G39A-T103G-W104F-I189H-L278A',
'G39A-T103G-W104F-L278A-A282G-I285A-V286A',
'G39A-T42G-T103G-W104F-L278A'
 ]

#***********************
# Check for duplicates in list.
# Assumes mutants are written in increasing order of position in back bone.
stats = {}
for x in inconclusive:
    stats[x] = stats.get(x, 0) + 1
duplicates = [(dup,i) for (dup, i) in stats.items() if i > 1]
print 'duplicates', duplicates

experimental = [
'G39A-L278A',
'G39A-W104F',
'G39A-W104F-L278A',
'G39A',
'T103G',
'G39A-T103G-W104F-L278A',
'G39A-T103G-L278A',
'G39A-W104F-I189Y-L278A',
'G39A-T103G-W104Q-L278A',
'L278A',
'W104F',
'G39A-T103G-W104F-D223G-L278A',
'G39A-T103G',
'G39A-T42A-T103G-W104F-L278A',
'I189H',
'G39A-I189G-L278A',
'G41S',
'I189G',
'G39A-T103G-W104F-I189H-D223G-L278A',
'G39A-T103G-W104F-I189H-L278A-A282G-I285A-V286A',
'A132N',
'P38H'
]

import sys
import os.path

# Normalized heat file.
dat=sys.argv[1]
val=open(dat, 'r').readlines()
name = os.path.splitext("-".join(dat.split('-')[1:]))[0]

# Prepare data handle.
E = [float(i) for i in val]

# Locate index of maximum, then lowest point before the maximum.
i_max = 0
e_max = 0.0
cnt   = 0 

# Consider data starting from second and end before last item.
def bar_rest(e_max, cnt):
    cnt+=1
    for e in E[1:-1]:
        if e > e_max:
            e_max = e 
            i_max = cnt
        cnt+=1
    e_min = min(E[1:i_max])
    return e_min, e_max

# Consider the complete data, use lowest point of the first 3 frames.
def bar_extn(e_max, cnt):
    for e in E:
        if e > e_max:
            e_max = e 
            i_max = cnt
        cnt+=1
    e_min = min(E[:4])
    return e_min, e_max

# Consider the complete data, take first frame as ES.
def bar_zero(e_max, cnt):
    for e in E:
        if e > e_max:
            e_max = e 
            i_max = cnt
        cnt+=1
    e_min = E[0]
    return e_min, e_max

# Discard barriers larger than max_heat.
#if e_max - e_min < max_heat:
#delta_e_rest = bar_rest(e_max, cnt)[1] - bar_rest(e_max, cnt)[0]
delta_e_extn = bar_extn(e_max, cnt)[1] - bar_extn(e_max, cnt)[0]
delta_e_zero = bar_zero(e_max, cnt)[1] - bar_zero(e_max, cnt)[0]
#if delta_e_rest < max_heat or delta_e_extn < max_heat or delta_e_zero < max_heat:
#if delta_e_extn < max_heat or delta_e_zero < max_heat and name not in inconclusive: 
#    #print name, e_max - e_min
#    #print name 
#    #print "Restricted range:", delta_e_rest
#    #print "Extended range:", delta_e_extn
#    print name, delta_e_zero, len(name.split('-'))
#else:
#    print "Providing mutant with inconclusive barrier."

if name not in inconclusive:
    #print "OK", name, round(delta_e_extn, 2), len(name.split('-'))
    print "OK", name, round(delta_e_extn, 2)
    if delta_e_extn < max_heat:
        print "Set L", name, round(delta_e_extn, 2), len(name.split('-'))
        if name in experimental:
            print "Set S", name, delta_e_extn, len(name.split('-'))
    else:
        print "Barrier too large:", name, round(delta_e_extn, 2)
else:
    print "Inconclusive:", name
