#!/bin/bash

# **************************************************
# .................................................. 
# Transfer 1scf output to optimization input.
# .................................................. 
# **************************************************

# $HOME/scripts_model_generation/scf2opt.sh

# DOES:
# 1) '1-scf.arc' -> '1-3-opt.mop'
# 2) Sets optimization flags of reaction coordinate.

# REQUIRES:
# - '1scf.arc' files, which are the templates for 'opt.mop' files.
# - '1scf.mop' files, required to locate 'SER OG' line.

# PARAMETERS:
# - How many lines above the last line is the carbonyl 
#   carbon of the substrate       -> <offset>
# - Serine identifier: identify the nucleophilic
#   side chain oxygen             -> <serIdentifier>
# - MOPAC optimization parameters -> Set at the end of the file.

# ----------------------------------
# Adjust these two parameters below:
# $(Line_number_of_last_atom_of_substrate)-$(Line_number_of_atom_above_atom_to_constrain)
offset=21
# Serine oxygen identifier.
serIdentifier="244  OG  SER B  18"
# ----------------------------------

# CALLING SEQUENCE:
# $ scf2opt 1-3-1scf-W104Q-001.arc

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
serLine=`grep -n "$serIdentifier" ${optmop/opt/scf}|cut -d ":" -f 1`
vi -c "$serLine,${serLine}s/+1/+0/g" -c "wq" $optmop

# Setting substrate C '+0' flag.
tot=`cat $optmop|wc -l`
cLine=$((tot-offset))
vi -c "$cLine,${cLine}s/+1/+0/g" -c "wq" $optmop

# Replace '1scf' keywords. Set MOPAC optimization parameters.
vi -c "1,1s/cutoff=3 1scf/cutoff=15 gnorm=0.5 pdbout/" -c "wq" $optmop
