from pymol import cmd
import os
import sys
from pymol import stored
from os.path import splitext

# ************************************************************
# ------------------------------------------------------------
# VSC: Variant Side Chains of BCX
# Modifies selection around substrate.
# ------------------------------------------------------------
# ************************************************************

# DESCRIPTION:
# - Mutate a residue and save the fragment amino acid.

# PyMOL:
# - modify>around: residues select, substrate excluded
# - modify>expand: residues select, substrate included

# PREPARATION:
# - Enter 'set retain_order, 0' to protect atom ordering.
# - Substrate resi set to 500
# - Substrate resn and chain set to 'LIG' and A

# NOTE:
# - Probably hydrogen addition to N- and C- can
#   be discarded for complete enzyme chains

# Auto build-up of mutations dictionary.
# First select residues to mutate, then select alpha carbons of the new selection
# then store the residue number of those alpha carbons.
# PyMOL> cmd.select("lig-es-default", "resi 500", enable=1)
# PyMOL> cmd.select("lig-es-around", "(byres (lig-es-default around 4))", enable=1)
# PyMOL> cmd.select("lig-es-around-ca", "lig-es-around and name ca", enable=1)
# PyMOL> cmd.do("iterate (lig-es-around-ca)", stored.li.append(resi)")

# REQUIRES:
# - PDB file to mutate

# CALLING orig_sequence:
# PyMOL> cd directory/containing/vsc-ext.py
# PyMOL> run vsc.py
# PyMOL> frag <state>

# PARAMETERS:
# - <mutations> dictionary below
obj = 'es-con-opt-08-pm6-1.0-15.pdb'
sub = '500'
distance = '4'
state = sys.argv[1]

# OPTIONS:
# - The number of conformers can be adjusted.
# - The mutated side chain can be optimized locally by vdW minimization.

# ************************************************************
def setup(obj):

    # Various set up
    pwd = os.getcwd() 
    #print "os.getcwd()", os.getcwd()
    cmd.do('wizard mutagenesis')
    cmd.do('refresh_wizard')

    # Save residue names and numbers.
    orig_sequence = setNames(obj)
    #print orig_sequence

    # Keeping track of the mutations
    # Example: '42':  ['GLY', 'ASN', 'VAL', 'ALA']
    # Important: Trailing commata.
    all_side_chains = ['ALA', 'ARG', 'ASN', 'ASP',
                       'CYS', 'GLU', 'GLN', 'GLY',
                       'HIS', 'ILE', 'LEU', 'LYS',
                       'MET', 'PHE', 'PRO', 'SER',
                       'THR', 'TRP', 'TYR', 'VAL'
                       ]
    phe = ['PHE']
    do_not_mutate = ['78', '172']
    positions_in_selection = get_positions_in_selection(sub, distance)
    mutations = {}
    #mutations = {'115': all_side_chains}
    #mutations = {'115': ['ALA', 'SER']}
    for i in positions_in_selection:
        if i[0] not in do_not_mutate:
            mutations[i[0]] = []
            # Prevent mutating from WT to WT.
            #for mut in all_side_chains:
            for mut in phe:
                if i[1] != mut:
                    mutations[i[0]].append(mut)
    #for i in mutations.keys():
    #    print i, mutations[i]
    return pwd, mutations, orig_sequence
# ------------------------------------------------------------

# ************************************************************
def get_positions_in_selection(sub, distance):
    cmd.do("select lig-def, resi %s" % sub)
    cmd.select("lig-around", "(byres (lig-def around %s))" % distance)
    cmd.select("lig-around-ca", "lig-around and name ca")
    cmd.do("stored.li = []")
    cmd.do("iterate (lig-around-ca), stored.li.append((resi, resn))")
    cmd.do("delete all")
    return stored.li
# ------------------------------------------------------------

# ************************************************************
# 'state=state': The first variable is the variable used within
# the scope of this function. The second variable is the one
# in the global scoped and defined at the top of the module.
def frag(state=state, obj=obj): 

    pwd, mutations, orig_sequence = setup(obj)
    #get_positions_in_selection(sub, distance)
    
    # Add and retain hydrogens
    cmd.get_wizard().set_hyd("keep") 

    # Run over all sites where to mutate
    for site in mutations.keys():

        variants = mutations[site]

        # Run over all variants.
        for variant in variants:

            cmd.load(obj) 

            cmd.do('wizard mutagenesis')
            cmd.do('refresh_wizard')
            cmd.get_wizard().set_mode(variant)
            cmd.get_wizard().do_select(site + '/')
            
            # Get the number of available rotamers at that site
            # Introduce a condition here to check if 
            # rotamers are requested.
            # <<OPTION>>
            nRots = getRots(site, variant)
            #if nRots > 3:
            #    nRots = 3
            nRots=1

            cmd.rewind()
            for i in range(1, nRots + 1): 
                
                cmd.get_wizard().do_select("(" + site + "/)")
                cmd.frame(i)
                cmd.get_wizard().apply()

                # Optimize the mutated sidechain
                #<<OPTION>>
                #print "Sculpting."
                localSculpt(obj, site)

                # Protonation of the N.
                cmd.do("select n%d, name n and %d/" % (int(site), int(site)))
                cmd.edit("n%d" % int(site), None, None, None, pkresi=0, pkbond=0)
                cmd.do("h_fill")

                # Protonation of the C.
                cmd.do("select c%d, name c and %d/" % (int(site), int(site)))
                cmd.edit("c%d" % int(site), None, None, None, pkresi=0, pkbond=0)
                cmd.do("h_fill") 

                # Definition of saveString
                #saveString  = '%s/' % pwd
                #saveString += 'frag-' + getOne(orig_sequence[site]).lower() +\
                #               site + getOne(variant).lower() + '-%s.pdb, ' % state +\
                #               '((%s/))' % site
                saveStringRot  = '%s/' % pwd
                saveStringRot += 'frag-' + getOne(orig_sequence[site]).lower() +\
                                  site + getOne(variant).lower() + '-%02d-%s.pdb, ' % (i, state) +\
                                  '((%s/))' % site
                #print saveString 
                #cmd.do('save %s' % saveString.lower())
                cmd.do('save %s' % saveStringRot.lower())
            cmd.do('delete all') 
            cmd.set_wizard('done')
# ------------------------------------------------------------


# ************************************************************
# Convenience Functions
def getRots(site, variant): 
    cmd.get_wizard().set_mode(variant)
    # Key lines 
    # I dont know how they work, but they make it possible.
    # Jason wrote this: If you just write "site" instead of
    #                   "(site)", PyMOL will delete your
    #                   residue. "(site)" makes it an
    #                   anonymous selection.
    #print 'getRots'
    cmd.get_wizard().do_select("(" + str(site) + "/)")
    nRot = cmd.count_states("mutation") 
    return nRot 

def setNames(obj):
    orig_sequence = {}
    cmd.load(obj) 
    cmd.select("prot", "name ca")
    cmd.do("stored.names = []")
    cmd.do("iterate (prot), stored.names.append((resi, resn))")
    for i in stored.names:
        orig_sequence[i[0]] = i[1] 
    # Now in 'get_all_positions_in_selection'
    #cmd.do('delete all') 
    #print stored.names
    return orig_sequence

# Credit: Thomas Holder, MPI
# CONSTRUCT: - 'res'
#            - 'cpy'
#            -
def localSculpt(obj, site):
    res = str(site)
    cmd.protect('(not %s/) or name CA+C+N+O+OXT' % (res))
    print "Activating Sculpting."
    cmd.sculpt_activate(obj[:-4]) 
    cmd.sculpt_iterate(obj[:-4], cycles=500) 
    cmd.sculpt_deactivate(obj[:-4])
    cmd.deprotect() 

def getOne(three):
    trans = { 
       'ALA':'A',
       'ARG':'R',
       'ASN':'N',
       'ASP':'D',
       'CYS':'C',
       'GLU':'E',
       'GLN':'Q',
       'GLY':'G',
       'HIS':'H',
       'ILE':'I',
       'LEU':'L',
       'LYS':'K',
       'MET':'M',
       'PHE':'F',
       'PRO':'P',
       'SER':'S',
       'THR':'T',
       'TRP':'W',
       'TYR':'Y',
       'VAL':'V'
       } 
    return trans[three]
# ------------------------------------------------------------

# ************************************************************
# Expose to the PyMOL shell
cmd.extend('setup', setup)
cmd.extend('frag', frag)
cmd.extend('getRots', getRots)
cmd.extend('localSculpt', localSculpt)
# ------------------------------------------------------------
