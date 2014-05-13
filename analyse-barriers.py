#!/usr/bin/env python

# Get lowest <n> barriers
# Get lowest barrier at position <i>

# REQUIRED: File with data columns <MUTANT> <BARRIER>,
# prepared from 'calc_barriers_bcx.py':

# ADJUST: Lowest <n> barriers
n=300

# CALLING SEQUENCE:
# $ python analyse-barriers.py <barriers.dat>

import sys

input_file = sys.argv[1]
dat=open(input_file, 'r')
val=dat.readlines()

positions_barriers = {}
lowest_barrier_at_position = []

def analyse_barriers():
    # Get mutated positions
    for i in val:
        position = i.split()[0][1:-1]
        positions_barriers[position] = []
    # For every position, a list of (<MUTATION>, <BARRIER>) tuples is prepared
    for i in val:
        mutation, position, barrier = i.split()[0], i.split()[0][1:-1], i.split()[1]
        positions_barriers[position].append((mutation, barrier))
    # How many mutations are available at each position 
    for position in positions_barriers.keys():
        print len([i[0] for i in positions_barriers[position]]), [i[0] for i in positions_barriers[position]]
    print 'Number of positions:', len(positions_barriers.keys())
    print
    # Sort by increasing barrier, print <n> lowest barriers and mutants
    val.sort(key=lambda x: float(x.split()[1]))
    print "Lowest <n> barriers:"
    for i in val[:n]:
        print i,
    print
    print "Lowest barrier at each position:"
    for position in positions_barriers.keys():
        positions_barriers[position].sort(key=lambda x: float(x[1]))
        lowest_barrier_at_position.append(positions_barriers[position][0])
    # Sort by increasing position
    lowest_barrier_at_position.sort(key=lambda x: int(x[0][1:-1]))
    for mutation in lowest_barrier_at_position:
        print "%s %s" % (mutation[0], mutation[1])
    print
    dat.close()

# Form combinations of two elements from 'lowest_barrier_at_position' list
def double_mutants():
    import itertools
    cnt = 0
    analyse_barriers()
    for i in itertools.combinations(lowest_barrier_at_position, 2):
        print "%s+%s" % (i[0][0], i[1][0])
        cnt += 1
    print "Double mutants:", cnt

#analyse_barriers()
double_mutants()
