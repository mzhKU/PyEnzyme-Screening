#!/usr/bin/python

# ******************************
# Parse normalized heat files and list barriers.
# ..............................


# ******************************
# Calling sequence
# $ python ext_rest_barriers.py <normalized_heat.dat>
# ..............................

# Inconclusive barriers with the following mutants:
inconclusive = [
'G39A-W104Y',
'G39A-I189A',
'G39A-A141Q',
'G39A-A141N',
'W104F-A141N',
'T103G-A141Q',
'T103G-A141N',
'A141Q-I189N',
'A141N-L278A',
'T103G-W104Q-A141N',
'T103G-W104Y-A141Q',
'T103G-W104Y-I189A',
'W104F-A141N-I189A',
'W104F-A141N-I189N',
'W104F-A141N-L278A',
'W104F-A141Q-I189Q',
'W104Q-A141Q-L278A',
'W104Y-A141Q-I189Q',
'G39A-A141N-L278A',
'G39A-A141Q-I189A',
'G39A-A141Q-I189N',
'G39A-A141Q-L278A',
'G39A-I189N-L278A',
'G39A-T103G-A141Q',
'G39A-W104Y-I189N',
'G39A-W104Y-L278A',
'T103G-W104F-A141Q-I189Q',
'T103G-W104Y-A141Q-I189A',
'T103G-W104Y-A141Q-I189Q',
'G39A-A141N-I189A-L278A',
'G39A-A141Q-I189A-L278A',
'G39A-T103G-W104F-A141Q',
'G39A-T103G-W104Y-A141Q',
'G39A-W104F-A141Q-I189N',
'G39A-W104F-A141Q-I189Q',
'G39A-W104Y-A141N-L278A',
'G39A-W104Y-A141Q-L278A',
 ]

import sys
import os.path

max_heat = 12.0

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

# Consider the complete data, use lowest point before max as ES.
def bar_extn(e_max, cnt):
    for e in E:
        if e > e_max:
            e_max = e 
            i_max = cnt
        cnt+=1
    e_min = min(E[:i_max])
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
if delta_e_extn < max_heat or delta_e_zero < max_heat and name not in inconclusive: 
    #print name, e_max - e_min
    #print name 
    #print "Restricted range:", delta_e_rest
    #print "Extended range:", delta_e_extn
    print name, delta_e_zero, len(name.split('-'))
else:
    print "Providing mutant with inconclusive barrier."
