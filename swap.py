#!/kemi/mzhsteno/software/Python-2.7.3/python

import sys

# Swap atom lines, not working

# Arg: File to swap lines within
target='GLU A  78'
resi = '78'

# PREPARATION:
# - Load both structures in PyMOL, define (3)
#   as 'static', show label ID
# - Follow static label to first out of sync
# - Atom line with ID of 'dynamic' structure (1) at
#   this position has to be on the same line as (3)

def swap(val_local, lineId1, lineId2, start, end, move_cnt):
    cnt=0
    for l in val_local:
        # Check if correct residue and 
        # determine id of target lines
        if (cnt > start) and (cnt < end):
            print cnt, l,
            if target in l:
                if lineId1 in l[:12]: 
                    cnt1=cnt
                if lineId2 in l[:12]:
                    cnt2=cnt
                tmp             = val_local[cnt1]
                val_local[cnt1] = val_local[cnt2]
                val_local[cnt2] = tmp
            print val_local[cnt1], val_local[cnt2]
        cnt+=1
    return val_local

def get_lines_of_residue(identifier, resi, val):
    # ATOM   1125  N   UNK A  78
    cnt=1
    in_res = False
    for l in val:
        if identifier in l[17:26]:
            start=cnt
            in_res = True
            break
        cnt+=1
    while in_res:
        if identifier not in val[cnt]:
            in_res = False
            end=cnt
        cnt+=1
    return start, end

if __name__ == '__main__':
    dat=open(sys.argv[1], 'r')
    val=dat.readlines()
    dat.close()
    start, end = get_lines_of_residue(target, resi, val)
    moves = [ ['10', '13'],
              ['11', '15'],
              ['12', '10'],
              ['13', '11'] ]
              ['15', '12'] ]
    move_cnt=0
    for m in moves:
        val = swap(val, m[0], m[1], start, end, move_cnt)
        move_cnt+=1
    #for v in val:
    #    print v,
