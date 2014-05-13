#!/usr/bin/env python

# **************************************************
# ..................................................
# Assemble variant files
# ..................................................
# **************************************************

# DESCRIPTION:
# The variant structure files are being assembled
# from sequence files. Each sequence file contains the
# data of one side chain and every mutant has a
# fragment file.
# This script writes the BASH script which assembles
# the final mutant structure file(s).
# The variants are entered at the end of the script.

# CALLING SEQUENCE:
# $ python asv.py {1,3} -> seq.sh
# $ bash seq.sh

# PARAMETERS (search for by <<PARAM>>):
# - Reactant [= '1'] or product [= '3'] state files:

import os, sys
state=sys.argv[1] 

# Available backbone sequence fragements.  
# seq-x500: substrate
chain =\
[
'seq-a115',
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

#***********************
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
#-----------------------

#***********************
# Sort chain by residue ID
def key_func(s):
    stuff, x, label = s.partition('-')
    return int(label[1:])
#-----------------------

#***********************
def get_variant_library(): 
    # Read all fragment files, populate list with
    # positions for which a fragment file is available.
    files           = os.listdir(os.getcwd())
    fragment_files  = []
    variant_library = []
    for f in files:
        if f.split('-')[0] == 'frag':
            fragment_files.append(f)
    for f in fragment_files:
        variant_library.append(f.split('-')[1].upper())
    return variant_library
#-----------------------

# **************************************************
if __name__ == '__main__':

    # Variant library.
    vars = get_variant_library()

    # Sort the chain by residue ID,
    # reset the sequence script and generate the 'seq.sh' script.
    chain.sort(key=key_func)
    seqFile = open('seq.sh', 'w')
    seqFile.close()
    seqFile = open('seq.sh', 'a') 
    for variant in vars:
        seqFile.write(writeCatSeq(variant))
    seqFile.close()
#------------------------------------------------------
