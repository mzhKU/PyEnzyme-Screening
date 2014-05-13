#!/bin/bash

# **************************************************
# .................................................. 
# Transfer 1scf output to optimization input.
# .................................................. 
# **************************************************

# $HOME/bin/scf2opt.sh

# DOES:
# 1) '1-scf.arc' -> '1-3-opt.mop'
# 2) Sets optimization flags of reaction coordinate.
# 3) Sets charge flag on selected atom if required (defined by frame range)

# REQUIRES:
# - 'scf.arc' files, which are the templates for 'opt.mop' files.
# - 'scf.mop' files, required to locate line where constraint is added.
#                    CalB: 'SER OG'
#                    BCX:  'OE2 GLU A  78'

# PARAMETERS:
# - How many lines above the last line is the reacting atom
#   of the substrate              -> <offset>
# - Serine identifier: identify the nucleophilic
#   side chain oxygen             -> <gluIdentifier>
# - MOPAC optimization parameters -> Set at the end of the file.

# ----------------------------------
# Adjust these two parameters below:
# - Serine oxygen identifier in 1-3-scf-wt-001.mop file.
# - $(Line_number_last_atom_substrate)-$(Line_number_atom_above_atom_to_constrain)
# - Modify required identifier variable names
# - frame range where charge flag needs to be set

# Methyl-benzylamide
#serIdentifier="6  OG  SER A 105"
#offset=14

# Chloro-benzylamide
#serIdentifier="6  OG  SER A 105"
#offset=30

#gluIdentifier="1133  OE2 GLU A  78"
gluIdentifier="OE2 GLU A  78"
offset=32
#frameRange={3..9}
#flagAtom="C(  3140 UNK 186)"
# ----------------------------------

# CALLING SEQUENCE:
# $ scf2opt 1-3-scf-W104Q-001.arc

# Write 'opt' file.
scfarc=$1
optarc=${scfarc/scf/opt}
optmop=${optarc/arc/mop} 
cp $scfarc $optmop

# User info.
echo Writing $optmop

# Removing '1scf.arc' header.
tot=`cat $optmop|wc -l`
lineFin=`grep -i -n "FINAL GEOMETRY" $optmop|cut -d ":" -f 1`
tail -n -$((tot-lineFin)) $optmop > tmp.mop; mv tmp.mop $optmop

# Setting SER OG '+0' flag.
gluLine=`grep -n "$gluIdentifier" ${optmop/opt/scf}|cut -d ":" -f 1`
#vi -c "$gluLine,${gluLine}s/+1/+0/g" -c "wq" $optmop
sed "$gluLine s/+1/+0/g" $optmop > ${optmop/mop/tmp}
mv ${optmop/mop/tmp} ${optmop/tmp/mop}

# Setting substrate C '+0' flag.
tot=`cat $optmop|wc -l`
cLine=$((tot-offset))
#vi -c "$cLine,${cLine}s/+1/+0/g" -c "wq" $optmop
sed "$cLine s/+1/+0/g" $optmop > ${optmop/mop/tmp}
mv ${optmop/mop/tmp} ${optmop/tmp/mop}

# Replace '1scf' keywords. Set MOPAC optimization parameters.
#vi -c "1,1s/cutoff=2 1scf/pm6 cutoff=9 gnorm=5.0 eps=78 pdbout t=4.0D/" -c "wq" $optmop
sed "1 s/cutoff=2 1scf/pm6 cutoff=15 gnorm=1.0 eps=78 pdbout t=4.0D/" $optmop >${optmop/mop/tmp}
mv ${optmop/mop/tmp} ${optmop/tmp/mop}
