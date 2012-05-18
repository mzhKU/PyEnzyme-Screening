#!/bin/bash

# **************************************************************************
# ..........................................................................
# Transfer optimization output to SPE calculation input files.
# ..........................................................................
# **************************************************************************

# LOCATION:
# $HOME/scripts_model_generation/opt2spe.sh

# ACTION:
# - Copies optimization output to SPE input.
# - Replaces optimization keywords by
#   spe keywords using vim.

# REQUIRES:
# - 'opt.arc' files

# -----------------------------------------------
# ADJUST:
# - Keyword line: $kwl
kwl="1,1s/mozyme eps=78.4 cutoff=15 gnorm=0.5 pdbout/mozyme eps=78.4 cutoff=15 1scf/"
# -----------------------------------------------

# CALLING SEQUENCE:
# $ ./opt2spe.sh <1-3-opt*arc> 

# Convenience variable.
name=${1/1-3-opt-/}
name=${name/-???.arc/}

# Copy the arc files from the optimization
# to new files.
spearc=${1/opt/spe}
spemop=${spearc/arc/mop}
cp $1 $spemop 

# Remove all 'WARNING' lines
grep -i -v -w "warning" $spemop > tmp.dat
mv tmp.dat $spemop

echo Writing $spemop 

# Remove the MOPAC header.
# 1) Determining header length: $lenHead.
# 2) Determining total length:  $lenTot.
#    <tr -s>: squeezing multiple white space.
lenHead=`grep -n "FINAL GEOMETRY" $spemop|cut -d ":" -f 1`
lenTot=`cat $spemop|wc -l`
tail -n -$((lenTot-lenHead)) $spemop > ./tmp.dat
mv ./tmp.dat $spemop

# Replace the '+0' flags from the optimization.
# Old version.
# vi "+:%s/+0/+1/g" "+wq" $spemop
vi -c "%s/+0/+1/g" -c "wq" $spemop
##vi -c "1,1s/mozyme cutoff=9 gnorm=5.0 pdbout/1scf/" -c "wq" $spemop
vi -c "$kwl" -c "wq" $spemop
