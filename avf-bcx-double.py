#!/usr/bin/env python

# **************************************************
# ..................................................
# Assemble double mutant variant files of BCX
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

# REQUIREMENTS:
# - Use 'analyse-barriers.py' script to generate
#   double mutant combinations of the single mutants
#   with lowest barriers.

import sys
state=sys.argv[1] 

# Available backbone sequence fragements.  
chain =\
['seq-a115',
'seq-a1',
'seq-a142',
'seq-a152',
'seq-a165',
'seq-a170',
'seq-a18',
'seq-a55',
'seq-a59',
'seq-d101',
'seq-d106',
'seq-d11',
'seq-d119',
'seq-d121',
'seq-d4',
'seq-d83',
'seq-e172',
'seq-e78',
'seq-f125',
'seq-f146',
'seq-f36',
'seq-f48',
'seq-g102',
'seq-g103',
'seq-g120',
'seq-g12',
'seq-g13',
'seq-g139',
'seq-g14',
'seq-g157',
'seq-g161',
'seq-g173',
'seq-g178',
'seq-g21',
'seq-g23',
'seq-g24',
'seq-g34',
'seq-g39',
'seq-g41',
'seq-g45',
'seq-g56',
'seq-g62',
'seq-g64',
'seq-g70',
'seq-g86',
'seq-g92',
'seq-g96',
'seq-h149',
'seq-h156',
'seq-i107',
'seq-i118',
'seq-i144',
'seq-i15',
'seq-i51',
'seq-i77',
'seq-k135',
'seq-k154',
'seq-k40',
'seq-k95',
'seq-k99',
'seq-l160',
'seq-l66',
'seq-l68',
'seq-l76',
'seq-m158',
'seq-m169',
'seq-n114',
'seq-n141',
'seq-n148',
'seq-n151',
'seq-n159',
'seq-n163',
'seq-n17',
'seq-n181',
'seq-n20',
'seq-n25',
'seq-n29',
'seq-n32',
'seq-n35',
'seq-n52',
'seq-n54',
'seq-n61',
'seq-n63',
'seq-n8',
'seq-p116',
'seq-p137',
'seq-p47',
'seq-p60',
'seq-p75',
'seq-p90',
'seq-q127',
'seq-q133',
'seq-q167',
'seq-q175',
'seq-q7',
'seq-r112',
'seq-r122',
'seq-r132',
'seq-r136',
'seq-r49',
'seq-r73',
'seq-r89',
'seq-s100',
'seq-s117',
'seq-s130',
'seq-s134',
'seq-s140',
'seq-s155',
'seq-s162',
'seq-s176',
'seq-s177',
'seq-s179',
'seq-s180',
'seq-s2',
'seq-s22',
'seq-s27',
'seq-s31',
'seq-s46',
'seq-s74',
'seq-s84',
'seq-t10',
'seq-t104',
'seq-t109',
'seq-t110',
'seq-t111',
'seq-t123',
'seq-t124',
'seq-t126',
'seq-t138',
'seq-t143',
'seq-t145',
'seq-t147',
'seq-t171',
'seq-t183',
'seq-t3',
'seq-t33',
'seq-t43',
'seq-t44',
'seq-t50',
'seq-t67',
'seq-t72',
'seq-t87',
'seq-t91',
'seq-t93',
'seq-t97',
'seq-v131',
'seq-v150',
'seq-v16',
'seq-v168',
'seq-v182',
'seq-v184',
'seq-v19',
'seq-v28',
'seq-v37',
'seq-v38',
'seq-v57',
'seq-v81',
'seq-v82',
'seq-v98',
'seq-w129',
'seq-w153',
'seq-w164',
'seq-w185',
'seq-w30',
'seq-w42',
'seq-w58',
'seq-w6',
'seq-w71',
'seq-w85',
'seq-w9',
'seq-x186',
'seq-x187',
'seq-x188',
'seq-x189',
'seq-x190',
'seq-x191',
'seq-x192',
'seq-x193',
'seq-x194',
'seq-x195',
'seq-x196',
'seq-x197',
'seq-x198',
'seq-x199',
'seq-x200',
'seq-x201',
'seq-x202',
'seq-x203',
'seq-x204',
'seq-x205',
'seq-x206',
'seq-x207',
'seq-x208',
'seq-x209',
'seq-x210',
'seq-x211',
'seq-x212',
'seq-x213',
'seq-x214',
'seq-x215',
'seq-x216',
'seq-x217',
'seq-x218',
'seq-x219',
'seq-x220',
'seq-x221',
'seq-x222',
'seq-x223',
'seq-x224',
'seq-x225',
'seq-x226',
'seq-x227',
'seq-x228',
'seq-x229',
'seq-x230',
'seq-x231',
'seq-x232',
'seq-x233',
'seq-x234',
'seq-x235',
'seq-x236',
'seq-x237',
'seq-x238',
'seq-x239',
'seq-x240',
'seq-x241',
'seq-x242',
'seq-x243',
'seq-x244',
'seq-x245',
'seq-x246',
'seq-x247',
'seq-x248',
'seq-x249',
'seq-x250',
'seq-x251',
'seq-x252',
'seq-x253',
'seq-x254',
'seq-x255',
'seq-x256',
'seq-x257',
'seq-x258',
'seq-x259',
'seq-x260',
'seq-x261',
'seq-x262',
'seq-x263',
'seq-x264',
'seq-x265',
'seq-x266',
'seq-x267',
'seq-x268',
'seq-x269',
'seq-x270',
'seq-x271',
'seq-x272',
'seq-x273',
'seq-x274',
'seq-x275',
'seq-x276',
'seq-x277',
'seq-x278',
'seq-x279',
'seq-x280',
'seq-x281',
'seq-x282',
'seq-x283',
'seq-x284',
'seq-x285',
'seq-x286',
'seq-x287',
'seq-x288',
'seq-x289',
'seq-x290',
'seq-x291',
'seq-x292',
'seq-x293',
'seq-x294',
'seq-x295',
'seq-x296',
'seq-x297',
'seq-x298',
'seq-x299',
'seq-x300',
'seq-x301',
'seq-x302',
'seq-x500',
'seq-y105',
'seq-y108',
'seq-y113',
'seq-y128',
'seq-y166',
'seq-y174',
'seq-y26',
'seq-y5',
'seq-y53',
'seq-y65',
'seq-y69',
'seq-y79',
'seq-y80',
'seq-y88',
'seq-y94'
]
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
            writeSeq += 'frag-' + variant.split('+')[ind].lower() + '-01,\\\n'
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

#***********************
# Sort chain by residue ID
def key_func(s):
    stuff, x, label = s.partition('-')
    return int(label[1:])
#-----------------------


if __name__ == '__main__':

    # **************************************************
    # Variant library.
    # Sorted by charge.
    vars=[
'Q7W+W9E',
'Q7W+N35E',
'Q7W+V37T',
'Q7W+Y65R',
'Q7W+Y69E',
'Q7W+W71G',
'Q7W+Y80D',
'Q7W+R112D',
'Q7W+A115I',
'Q7W+P116C',
'Q7W+S117P',
'Q7W+I118M',
'Q7W+F125K',
'Q7W+Q127W',
'Q7W+W129I',
'Q7W+Y166V',
'Q7W+Y174D',
'W9E+N35E',
'W9E+V37T',
'W9E+Y65R',
'W9E+Y69E',
'W9E+W71G',
'W9E+Y80D',
'W9E+R112D',
'W9E+A115I',
'W9E+P116C',
'W9E+S117P',
'W9E+I118M',
'W9E+F125K',
'W9E+Q127W',
'W9E+W129I',
'W9E+Y166V',
'W9E+Y174D',
'N35E+V37T',
'N35E+Y65R',
'N35E+Y69E',
'N35E+W71G',
'N35E+Y80D',
'N35E+R112D',
'N35E+A115I',
'N35E+P116C',
'N35E+S117P',
'N35E+I118M',
'N35E+F125K',
'N35E+Q127W',
'N35E+W129I',
'N35E+Y166V',
'N35E+Y174D',
'V37T+Y65R',
'V37T+Y69E',
'V37T+W71G',
'V37T+Y80D',
'V37T+R112D',
'V37T+A115I',
'V37T+P116C',
'V37T+S117P',
'V37T+I118M',
'V37T+F125K',
'V37T+Q127W',
'V37T+W129I',
'V37T+Y166V',
'V37T+Y174D',
'Y65R+Y69E',
'Y65R+W71G',
'Y65R+Y80D',
'Y65R+R112D',
'Y65R+A115I',
'Y65R+P116C',
'Y65R+S117P',
'Y65R+I118M',
'Y65R+F125K',
'Y65R+Q127W',
'Y65R+W129I',
'Y65R+Y166V',
'Y65R+Y174D',
'Y69E+W71G',
'Y69E+Y80D',
'Y69E+R112D',
'Y69E+A115I',
'Y69E+P116C',
'Y69E+S117P',
'Y69E+I118M',
'Y69E+F125K',
'Y69E+Q127W',
'Y69E+W129I',
'Y69E+Y166V',
'Y69E+Y174D',
'W71G+Y80D',
'W71G+R112D',
'W71G+A115I',
'W71G+P116C',
'W71G+S117P',
'W71G+I118M',
'W71G+F125K',
'W71G+Q127W',
'W71G+W129I',
'W71G+Y166V',
'W71G+Y174D',
'Y80D+R112D',
'Y80D+A115I',
'Y80D+P116C',
'Y80D+S117P',
'Y80D+I118M',
'Y80D+F125K',
'Y80D+Q127W',
'Y80D+W129I',
'Y80D+Y166V',
'Y80D+Y174D',
'R112D+A115I',
'R112D+P116C',
'R112D+S117P',
'R112D+I118M',
'R112D+F125K',
'R112D+Q127W',
'R112D+W129I',
'R112D+Y166V',
'R112D+Y174D',
'A115I+P116C',
'A115I+S117P',
'A115I+I118M',
'A115I+F125K',
'A115I+Q127W',
'A115I+W129I',
'A115I+Y166V',
'A115I+Y174D',
'P116C+S117P',
'P116C+I118M',
'P116C+F125K',
'P116C+Q127W',
'P116C+W129I',
'P116C+Y166V',
'P116C+Y174D',
'S117P+I118M',
'S117P+F125K',
'S117P+Q127W',
'S117P+W129I',
'S117P+Y166V',
'S117P+Y174D',
'I118M+F125K',
'I118M+Q127W',
'I118M+W129I',
'I118M+Y166V',
'I118M+Y174D',
'F125K+Q127W',
'F125K+W129I',
'F125K+Y166V',
'F125K+Y174D',
'Q127W+W129I',
'Q127W+Y166V',
'Q127W+Y174D',
'W129I+Y166V',
'W129I+Y174D',
'Y166V+Y174D'
            ] 
    #---------------------------------------------------

    # Sort chain
    chain.sort(key=key_func)


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
