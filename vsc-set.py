from pymol import cmd
import os
import sys
from pymol import stored
from os.path import splitext

# ************************************************************
# ------------------------------------------------------------
# VSC: Variant Side Chains of BCX
# Modifies selection around substrate, mutations based on
# current 'resn'.
# ------------------------------------------------------------
# ************************************************************

# DESCRIPTION:
# - Mutate a residue and save the fragment amino acid.

# PyMOL:
# - modify>around: residues select, substrate excluded
# - modify>expand: residues select, substrate included

# MODE:
prod   = 'production'
debug  = 'debugging'
mode = prod
# 'debug': Mutate two positions two times
# 'prod':  Mutate all within range <distance> of <sub>

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
# PyMOL> cd directory/containing/vsc-set.py
# PyMOL> run vsc-set.py
# PyMOL> frag <state>

# PARAMETERS:
# - <mutations> dictionary below
obj = 'ge-onp-opt-pm6-1.0-15.pdb'
sub = '500'
distance = '4'
state = sys.argv[1]

# OPTIONS:
# - The number of conformers can be adjusted.
# - The mutated side chain can be optimized locally by vdW minimization.

# ************************************************************
def setup(obj):
    """
    Calling sequence of setup:
    PyMOL> run vsc-set.py
    PyMOL> setup <object_file_name.pdb>
    Variables:
    'mutations': {'<POSITION_ID>':['<MUTATION_1>', '<MUTATION_2>', ...]}
    """
    # Setup.
    pwd = os.getcwd() 
    # {'<resi>':'<resn>'}
    orig_sequence = set_names(obj)
    # Catalytically active positions.
    do_not_mutate = ['78', '172']
    if mode == prod:
        all_side_chains = ['ALA', 'ARG', 'ASN', 'ASP',
                           'CYS', 'GLU', 'GLN', 'GLY',
                           'HIS', 'ILE', 'LEU', 'LYS',
                           'MET', 'PHE', 'PRO', 'SER',
                           'THR', 'TRP', 'TYR', 'VAL' ]
    else:
        all_side_chains = ['PHE', 'ASP', 'ILE']
    all_positions_in_selection = get_all_positions_in_selection(sub, distance)
    # 1) Avoid mutation of critical positions.
    # 2) All side chains are included, discarding is controlled by calculation of MOPAC charges.
    mutations = {}
    for i in all_positions_in_selection:
        if i[0] not in do_not_mutate:
            # Assignment of empty list to <RESI> key.
            mutations[i[0]] = []
            # Prevent mutating from WT to WT.
            for mut in all_side_chains:
                if i[1] != mut:
                    mutations[i[0]].append(mut)
    for i in mutations.keys():
        print i, mutations[i]
    return pwd, mutations, orig_sequence
# ------------------------------------------------------------

# ************************************************************
def get_all_positions_in_selection(sub, distance):
    """
    return [(<'RESI_i'>, <'RESN_i'>),
            (<'RESI_j'>, <'RESN_j'>), ...]
    """
    cmd.do("select lig-def, resi %s" % sub)
    cmd.select("lig-around", "(byres (lig-def around %s))" % distance)
    cmd.select("lig-around-ca", "lig-around and name ca")
    cmd.do("stored.li = []")
    cmd.do("iterate (lig-around-ca), stored.li.append((resi, resn))")
    cmd.do("delete all")
    if mode == prod:
        return stored.li
    else:
        return [('71', 'PHE'), ('118', 'ILE')]
# ------------------------------------------------------------

# ************************************************************
# 'state=state': The first variable is the variable used within
# the scope of this function. The second variable is the one
# in the global scope and defined at the top of the module.
# 'state': <1|3> for ES (1) complex or TI (3).
def frag(state=state, obj=obj): 
    pwd, mutations, orig_sequence = setup(obj)

    #get_positions_in_selection(sub, distance)
    
    # Run over all sites where to mutate, optionally add and retain hydrogens.
    for site in mutations.keys():
        variants = mutations[site]
        # Run over all variants.
        for variant in variants:
            cmd.load(obj) 
            cmd.do('wizard mutagenesis')
            cmd.do('refresh_wizard')
            cmd.get_wizard().set_hyd("keep") 
            cmd.get_wizard().set_mode(variant)
            #cmd.get_wizard().do_select(site + '/')
            
            # Get the number of available rotamers at that site.
            # Introduce a condition here to check if rotamers are requested.
            # <<OPTIONAL>>
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
                local_sculpt(obj, variant, site)

                # Protonation of the N.
                #cmd.do("select n%d, name n and %d/" % (int(site), int(site)))
                #cmd.edit("n%d" % int(site), None, None, None, pkresi=0, pkbond=0)
                #cmd.do("h_fill")

                # Protonation of the C.
                #cmd.do("select c%d, name c and %d/" % (int(site), int(site)))
                #cmd.edit("c%d" % int(site), None, None, None, pkresi=0, pkbond=0)
                #cmd.do("h_fill") 

                # Definition of saveString
                #saveString  = '%s/' % pwd
                #saveString += 'frag-' + get_one(orig_sequence[site]).lower() +\
                #               site + get_one(variant).lower() + '-%s.pdb, ' % state +\
                #               '((%s/))' % site
                save_string_rot  = '%s/' % pwd
                save_string_rot += 'frag-' + get_one(orig_sequence[site]).lower() +\
                                  site + get_one(variant).lower() + '-%02d-%s.pdb, ' % (i, state) +\
                                  '((%s/))' % site
                #print saveString 
                #cmd.do('save %s' % saveString.lower())
                cmd.do('save %s' % save_string_rot.lower())
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

def set_names(obj):
    """
    Return dictionary of {resi:resn} pairs.
    Loaded object is deleted in 'get_all_positions_in_selection'.
    """
    orig_sequence = {}
    cmd.load(obj) 
    cmd.select("prot", "name ca")
    cmd.do("stored.names = []")
    cmd.do("iterate (prot), stored.names.append((resi, resn))")
    for i in stored.names:
        orig_sequence[i[0]] = i[1] 
    return orig_sequence

# Credit: Thomas Holder, MPI
# CONSTRUCT: - 'res'
#            - 'cpy'
#            -
def local_sculpt(obj, variant_three, site):
    # Original version of local side chain optimization
    #res = str(site)
    #cmd.protect('(not %s/) or name CA+C+N+O+OXT' % (res))
    #print "Activating Sculpting."
    #cmd.sculpt_activate(obj[:-4]) 
    #cmd.sculpt_iterate(obj[:-4], cycles=50) 
    #cmd.sculpt_deactivate(obj[:-4])
    #cmd.deprotect() 

    # New version of local side chain optimization.
    #cmd.select("%s%s_exp" % (variant_one, site), "(byres (\"%s/\" expand 1.8))" % site)
    #cmd.select("%s%s_exp_sc" % (variant_one, site), "%s%s and (not name C+CA+N+O+HA+HT)" % (variant_one, site))
    #cmd.protect("not %s%s_exp_sc" % (variant_one, site))
    variant_one = get_one(variant_three)
    cmd.select("%s%s" % (variant_one, site), "%s/" % site)
    cmd.select("bb", "name C+CA+N+O+H+HA+HT")
    cmd.select("%s%s_sc" % (variant_one, site), "%s%s and not bb" % (variant_one, site))
    cmd.protect("not %s%s_sc" % (variant_one, site))
    cmd.sculpt_activate(obj[:-4])
    cmd.sculpt_iterate(obj[:-4], cycles=3000)
    cmd.sculpt_deactivate(obj[:-4])
    cmd.deprotect()

def get_one(three):
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
# No longer in use.
def get_mutations_depending_on(current_resn):
    if current_resn == 'ALA': 
        return ['GLY']
    if current_resn == 'ARG':
        return ['ALA', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']
    if current_resn == 'ASP':
        return ['ALA', 'ASN', 'CYS', 'GLY', 'HIS', 'ILE', 'LEU', 'PHE', 'PRO', 'SER', 'THR', 'TYR', 'VAL']
    if current_resn == 'ASN':
        return ['ALA', 'ASP', 'CYS', 'GLY', 'HIS', 'ILE', 'LEU', 'PHE', 'PRO', 'SER', 'THR', 'TYR', 'VAL']
    if current_resn == 'CYS':
        return ['ALA', 'GLY', 'PRO', 'SER', 'THR']
    if current_resn == 'GLU':
        return ['ALA', 'ASN', 'ASP', 'CYS', 'GLN', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']
    if current_resn == 'GLN':
        return ['ALA', 'ASN', 'ASP', 'CYS', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']
    if current_resn == 'GLY':
        return ['ALA']
    if current_resn == 'HIS': 
        return ['ALA, ASN', 'ASP', 'CYS', 'GLY', 'PHE', 'PRO', 'SER', 'THR', 'TYR', 'VAL']
    if current_resn == 'ILE':
        return ['ALA', 'ASN', 'ASP', 'CYS', 'GLY', 'HIS', 'LEU', 'PHE', 'PRO', 'SER', 'THR', 'TYR', 'VAL']
    if current_resn == 'LEU':
        return ['ALA', 'ASN', 'ASP', 'CYS', 'GLY', 'HIS', 'ILE', 'PHE', 'PRO', 'SER', 'THR', 'TYR', 'VAL']
    if current_resn == 'LYS':
        return ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']
    if current_resn == 'MET':
        return ['ALA', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TYR', 'VAL']
    if current_resn == 'PHE':
        return ['ALA', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TYR', 'VAL']
    if current_resn == 'PRO':
        return ['ALA', 'GLY', 'SER', 'THR']
    if current_resn == 'SER':
        return ['ALA', 'GLY', 'CYS', 'THR']
    if current_resn == 'THR':
        return ['ALA', 'GLY', 'CYS', 'SER']
    if current_resn == 'TRP':
        return ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TYR', 'VAL']
    if current_resn == 'TYR':
        return ['ALA', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'VAL']
    if current_resn == 'VAL':
        return ['ALA', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TYR'] 

# ------------------------------------------------------------

# ************************************************************
# Expose to the PyMOL shell
cmd.extend('setup', setup)
cmd.extend('frag', frag)
cmd.extend('getRots', getRots)
cmd.extend('local_sculpt', local_sculpt)
# ------------------------------------------------------------
