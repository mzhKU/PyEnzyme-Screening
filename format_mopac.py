from pymol import cmd, CmdException

# Writes MOPAC formated input files and sets constraint flags.
# Mainly used for constrained WT optimization.
# Mutant configuration is done with check-ca.py.

# CALLING SEQUENCE:
# Note no komma between function and argument in last call
# and no trailing slash after '<selection>':
# PyMOL> cd $WORKDIR
# PyMOL> loadAll <files>
# PyMOL> set retain_order
# PyMOL> set pdb_retain_ids
# PyMOL> run $scripts/format_mopac.py
# PyMOL> save_mopac_all <selection>

# Adjustments:
# - 'distances' list to control how many constrained layers should be generated

# FIX:
# - File name of output file should be better controlled

def save_mopac_all(reference):
    '''
DESCRIPTION

    Save all loaded objects in MOPAC format applying constraint flags
    to residues beyond 8, 10, 12 and 14 angstrom.

ARGUMENTS

    reference: Selection (residue id) used as reference for constraint distance.

EXAMPLE

    (Note: no comma for argument separation and no trailing back slash)
    save_mopac_all 500
    
    '''
    distances = ['8.0', '10.0', '12.0', '14.0']
    objects = cmd.get_names('objects')
    # Defining restricted atoms "rest" beyond <d> of substrate "sub".
    # Select only current object and substrate of current object.
    for ob in objects:
        current_object_selection = '/' + ob
        cmd.select("sub", '/' + ob + '///' + reference + '/')
        for d in distances:
            cmd.select("rest", "(byres (sub expand %s))" % d)
            cmd.select("rest", "((byobj sub) and not rest)")
            save_mopac(ob, d, current_object_selection, "rest")

def save_mopac(filename, dist, selection='all', zero='none', state=-1, quiet=1):
    '''
DESCRIPTION

    Save to MOPAC format

ARGUMENTS

    filename = string: file path to be written

    dist = string: beyond which distance to fix atoms
 
    selection = string: atoms to save {default: all}

    zero = string: atoms to save with zero flag {default: none}

    state = integer: state to save {default: -1 (current state)}
    '''
    #cmd.select("rest", "(byres (sub expand %s))" % dist)
    #cmd.select("rest", "((byobj sub) and not rest)")
    state, quiet = int(state), int(quiet)
    fmt = '%5s(%6i %3s%4i) %12.8f +%i %12.8f +%i %12.8f +%i %26.4f\n'
    zero_idx = set()
    cmd.iterate(zero, 'zero_idx.add((model,index))', space=locals())
    serial = [0]
    def callback(model, index, e, resn, resv, x, y, z, c):
        if (model, index) in zero_idx:
            flag = 0
        else:
            flag = 1
        serial[0] += 1
        # print "Saving: %s" % save_string
        handle.write(fmt % (e, serial[0], resn, resv, x, flag, y, flag, z, flag, c))
    save_string = filename.split('-')[0] + "-con-" + filename.split('-')[2] +\
                "-%02d" % float(dist) + "-ste-ini.pdb"
    handle = open(save_string, 'w')
    cmd.iterate_state(state, selection,
                      'callback(model, index, elem, resn, resv,'
                      ' x, y, z, partial_charge)', space=locals())
    handle.close()
    if not quiet:
        print ' Save-MOPAC: Wrote %i atoms to file' % (serial[0])

cmd.extend('save_mopac', save_mopac)
cmd.extend('save_mopac_all', save_mopac_all)
