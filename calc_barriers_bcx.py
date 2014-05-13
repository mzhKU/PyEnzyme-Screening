#!/usr/bin/python

# ******************************
# Parse normalized heat files and list barriers.
# ..............................


# ******************************
# Calling sequence
# $ python calc_barriers_bcx.py <normalized_heat.dat>
# ..............................

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

# Consider data before last item.
def bar_rest(e_max, cnt):
    cnt+=1
    for e in E:
        if e > e_max:
            e_max = e 
            i_max = cnt
        cnt+=1
    try:
        e_min = min(E[:i_max])
        return e_min, e_max
    except UnboundLocalError:
        print "No barrier defined for: %s" % name
        sys.exit(0)

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

#delta_e_extn = bar_extn(e_max, cnt)[1] - bar_extn(e_max, cnt)[0]
#delta_e_zero = bar_zero(e_max, cnt)[1] - bar_zero(e_max, cnt)[0]
delta_e_rest = bar_rest(e_max, cnt)[1] - bar_rest(e_max, cnt)[0]

print name, round(delta_e_rest, 2)
