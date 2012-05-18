#!/usr/bin/env python

# DESCRIPTION:
# - Linear interpolation between the two given structures.

# ARGUMENTS:
# - Initial State
# - Final State
# - Name

# CALLING SEQUENCE:
# <$ python intcat.py $startingState $finalState $name>

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

def makeCatFile(name):
    writePDBFile = open('polation-%s.pdb' % name, 'w')
    for step in range(1, len(interpolation)+1):
        writeString = ''
        writeString += 'MODEL %s\n' % str(step)
        for atom in range(len(reactValue)):
            writeString += reactValue[atom][:32]\
                           + interpolation[step-1][atom]\
                           + reactValue[atom][54:]
        writeString += 'ENDMDL\n'
        writePDBFile.write(writeString)
    writePDBFile.close()

makeCatFile(name)
