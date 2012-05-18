#!/usr/bin/env python

# **************************************************
# ..................................................
# Separate Interpolation Files for overall charge 
# ..................................................
# **************************************************

# DESCRIPTION:
# - Write separate interpolation files to calculate overall charge.

# CALLING SEQUENCE:
# $ python intcha.py $1 $2 $name

import sys
reac, prod, name = sys.argv[1], sys.argv[2], sys.argv[3]

reactData, interData = open(reac, 'r'), open(prod, 'r') 
reactValue, interValue = reactData.readlines(), interData.readlines() 

n = 10
diff = []
diffFrac = []
interpolation = [] 

# Run over coordinates
for i in enumerate(reactValue): 
    # Change in each coordinate for every atom.
    dx, dy, dz =\
       eval(interValue[i[0]][32:38]) - eval(reactValue[i[0]][32:38]),\
       eval(interValue[i[0]][39:46]) - eval(reactValue[i[0]][39:46]),\
       eval(interValue[i[0]][47:54]) - eval(reactValue[i[0]][47:54])
    #print dx, dy, dz
    diff.append([round(dx, 3), round(dy, 3), round(dz, 3)])

print 'Number of vectors in the diff-list'
print len(diff)

for atom in diff:
    diffFrac.append([c/float(n) for c in atom]) 

# Run over interpolation step
for i in range(n): 
    # Run over atom
    set = []
    for atom in range(len(reactValue)): 
        xi = eval(reactValue[atom][32:38]) + diffFrac[atom][0]*i
        yi = eval(reactValue[atom][39:46]) + diffFrac[atom][1]*i
        zi = eval(reactValue[atom][47:54]) + diffFrac[atom][2]*i
        set.append('%6.3f %7.3f %7.3f' % (xi, yi, zi))
    interpolation.append(set)
print 'len(interpolation)', len(interpolation)
print 'len(set)', len(set)

def makeSeparateFiles(name):
    for step in range(1, len(interpolation)+1):
        writeMopFile = open('1-3-cha-%s-%03i.mop' % (name,step), 'w')
        writeString = ''
        #writeString = 'mozyme charge=-2 cutoff=3 1scf \n\n\n'
        writeString = 'charges\n\n\n'
        for atom in range(len(reactValue)):
            writeString += reactValue[atom][:32]\
                           + interpolation[step-1][atom]\
                           + reactValue[atom][54:]
        writeMopFile.write(writeString)
        writeMopFile.close()

makeSeparateFiles(name)
