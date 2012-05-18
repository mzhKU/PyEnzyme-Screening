#!/usr/bin/env python

# **************************************************
# ..................................................
# Assemble variant files
# ..................................................
# **************************************************

# DESCRIPTION:
# The variant structure files are being assembled
# from sequence files. Each sequence file contains the
# data of one side chain and  every mutant has a
# fragment file.
# This script writes the BASH script which assembles
# the final mutant structure file(s).
# The variants are entered at the end of the script.

# CALLING SEQUENCE:
# $ python asv.py {1,3} -> seq.sh
# $ bash seq.sh

# PARAMETERS (search for by <<PARAM>>):
# - Reactant [= '1'] or product [= '3'] state files:

import sys
state=sys.argv[1] 

# Available backbone sequence fragements.  
chain =\
['seq-v37',\
 'seq-p38',\
 'seq-g39',\
 'seq-t40',\
 'seq-g41',\
 'seq-t42',\
 'seq-t43',\
 'seq-g44',\
 'seq-p45',\
 'seq-q46',\
 'seq-s47',\
 'seq-f48',\
 'seq-d49',\
 'seq-s50',\
 'seq-l102',\
 'seq-t103',\
 'seq-w104',\
 'seq-s105',\
 'seq-q106',\
 'seq-f131',\
 'seq-a132',\
 'seq-p133',\
 'seq-d134',\
 'seq-y135',\
 'seq-v139',\
 'seq-l140',\
 'seq-a141',\
 'seq-q156',\
 'seq-q157',\
 'seq-t158',\
 'seq-t186',\
 'seq-d187',\
 'seq-e188',\
 'seq-i189',\
 'seq-v190',\
 'seq-q191',\
 'seq-p192',\
 'seq-f220',\
 'seq-v221',\
 'seq-i222',\
 'seq-d223',\
 'seq-h224',\
 'seq-a225',\
 'seq-g226',\
 'seq-l277',\
 'seq-l278',\
 'seq-a279',\
 'seq-p280',\
 'seq-a281',\
 'seq-a282',\
 'seq-a283',\
 'seq-a284',\
 'seq-i285',\
 'seq-v286',\
 'seq-a287',\
 'seq-x500',
 'seq-x550']

def writeCatSeq(variant):
    # Convenience list of variants, replacing the '+'.
    varlist = variant.split('+')

    # Initialization of the bash script
    # Escaping BASH syntax.  
    # Resetting content of mutant structure file.
    numOfMutations = len(variant.split('+'))

    # <<PARAM>>:
    # - Reactant or product state file:        '?-res'
    # - Initial file or optimization job file: '-opt'.
    writeSeq  =\
            '# ' + '*'*50 + '\n' +\
            '# ' + '-'.join(variant.split('+')) + '\n' +\
            '# ' + str(numOfMutations) + '-fold mutant.\n' +\
            '# Resetting mutant file content.\n' +\
            'echo ' + '%'*50 + '\n'\
            'echo "Generating variant structure file of mutant:"\n' +\
            'echo ' + variant + '\n' +\
            'echo ' + '-'*50 + '\n'\
            'echo ' + '\n' +\
            'echo ' + '\n' +\
            'cat /dev/null > %s-res-' % state + '-'.join(varlist) + '-ste-ini.pdb\n' +\
            'for i in\\\n' +\
            '    {' 

    # Defining a list which contains only the numbers of the
    # residues that will be mutated.
    # First recast from 'G39A+L278A' form to ['G39A', 'L278A'],
    # then generate a list with only numbers ['39', '278'].
    varTmp = variant.split('+')
    varNum = [i[1:-1] for i in varTmp] 

    for s in chain:
        # Checking if the number of the residue is in the ones
        # to be mutated, if so, then the write sequence is
        # adjusted.
        if s[5:] in varNum:
            # Locate the index of the side chain which needs
            # to be mutated, then choose the corresponding index
            # in the varTmp list.
            ind=varNum.index(s[5:])
            writeSeq += 'frag-' + variant.split('+')[ind].lower() + ',\\\n'
        else:
            # Appending of the WT backbone.
            writeSeq += s + ',\\\n'

    # <<PARAM>>:
    # - Reactant or product state file:        '?-res'
    # - Initial file or optimization job file: '-opt'.
    writeSeq += '}\n' +\
            'do\n' +\
            '    cat $i-%s.pdb >> %s-res-' % (state, state) + '-'.join(varlist) + '-ste-ini.pdb\n' +\
            'done\n' +\
            'grep -v \'END\' ' + '%s-res-' % state + '-'.join(varlist) + '-ste-ini.pdb > tmp.pdb\n' +\
            'mv tmp.pdb ' + '%s-res-' % state + '-'.join(varlist) + '-ste-ini.pdb\n\n\n'
    return writeSeq

if __name__ == '__main__':

    # **************************************************
    # Variant library.
    # Sorted by charge.
    # 'charge=-4':
    vars=[
            #'G39A',
            #'T103G',
            #'W104F',
            #'W104Y',
            #'W104Q',
            #'I189Q',
            #'I189N',

            #'G39A+T103G',

            #'G39A+W104F',
            #'G39A+W104Y',
            #'G39A+W104Q',

            #'G39A+L278G',
            #'G39A+L278A',

            #'T103G+W104F',
            #'T103G+W104Y',
            #'T103G+W104Q',

            #'W104F+L278A',
            #'W104Y+L278A',
            #'W104Q+L278A',
            #
            #'G39A+T103G+W104F',
            #'G39A+T103G+W104Y',
            #'G39A+T103G+W104Q',

            #'G39A+W104F+L278A',
            #'G39A+W104Y+L278A',
            #'G39A+W104Q+L278A',

            #'G39A+W104F+L278G',
            #'G39A+W104Y+L278G',
            #'G39A+W104Q+L278G',

            #'T103G+W104F+L278A',
            #'T103G+W104Y+L278A',
            #'T103G+W104Q+L278A',

            #'W104F+A225K+L278A',

            #'T103G+W104F+L278G',
            #'T103G+W104Y+L278G',
            #'T103G+W104Q+L278G',

            #'G39A+T103G+W104F+L278A',
            #'G39A+T103G+W104Y+L278A',
            #'G39A+T103G+W104Q+L278A',

            #'G39A+W104F+A225K+L278A',

            #'G39A+T103G+W104F+L278G',
            #'G39A+T103G+W104Y+L278G',
            #'G39A+T103G+W104Q+L278G',

            #'G39A+W104F+T103G+L140Q+A141N+I189N',
            #'G39A+W104F+T103G+L140Q+A141N+I189Q',
            #'G39A+W104F+T103G+L140Q+A141Q+I189N',
            #'G39A+W104F+T103G+L140Q+A141Q+I189Q',

            #'G39A+W104F+T103G+L140N+A141N+I189N',
            #'G39A+W104F+T103G+L140N+A141N+I189Q',
            #'G39A+W104F+T103G+L140N+A141Q+I189N',
            #'G39A+W104F+T103G+L140N+A141Q+I189Q',

            'G39A+W104F+D223N+A225I+L278A',
            #'L278G+W104F+A225M+Q157V+I189A+D134A',
            #'T40G+L278G+W104F+A225M+Q157V+I189A+D134A'
            ] 
    #---------------------------------------------------


    #***********************
    # Reset the sequence script.
    seqFile = open('seq.sh', 'w')
    seqFile.close()
    seqFile = open('seq.sh', 'a') 
    #-----------------------


    #***********************
    # Generating the 'seq.sh' script
    for variant in vars:
        seqFile.write(writeCatSeq(variant))
    seqFile.close()
    #-----------------------

# EOF
#------------------------------------------------------
