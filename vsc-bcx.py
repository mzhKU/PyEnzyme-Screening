from pymol import cmd
import os
import sys
from pymol import stored
from os.path import splitext

# ************************************************************
# ------------------------------------------------------------
# VSC: Variant Side Chains of BCX
# ------------------------------------------------------------
# ************************************************************

# DESCRIPTION:
# - Mutate a residue and save the fragment amino acid.

# REQUIRES:
# - PDB file to mutate

# CALLING orig_sequence:
# PyMOL> run vsc.py
# PyMOL> frag <state>

# PARAMETERS:
# - <mutations> dictionary below
obj = 'es-onp-ini-h.pdb'
state = sys.argv[1]

# OPTIONS:
# - The number of conformers can be adjusted.
# - The mutated side chain can be optimized locally
#   by vdW minimization.


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

    mutations = { 
                  '35': all_side_chains
    } 
    return pwd, mutations, orig_sequence
# ------------------------------------------------------------


# ************************************************************
# 'state=state': The first variable is the variable used within
# the scope of this function. The second variable is the one
# in the global scoped and defined at the top of the module.
def frag(state=state, obj=obj): 

    pwd, mutations, orig_sequence = setup(obj)
    
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
            #nRots = getRots(site, variant)
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
                #localSculpt(obj, site)

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
    cmd.do('delete all') 
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
    cmd.sculpt_iterate(obj[:-4], cycles=5000) 
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



