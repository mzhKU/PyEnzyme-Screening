#!/bin/bash

# **************************************************************************
# ..........................................................................
# Delete the MOPAC header
# ..........................................................................
# **************************************************************************

# ACTION:
# - Delete MOPAC header of '.arc' files

# REQUIRES:
# - 'opt.arc' files

# -----------------------------------------------
# ADJUST:
# - None
# -----------------------------------------------

# CALLING SEQUENCE:
# $ ./del_MOPAC_header.sh <.arc> 

inp=$1

# Remove all 'WARNING' lines
grep -i -v -w "warning" $inp > tmp.dat
mv tmp.dat $inp

echo Writing ${inp}

# Removing the MOPAC header.
# 1) Determining header length: $lenHead.
# 2) Determining total length:  $lenTot.
#    <tr -s>: squeezing multiple white space.
lenHead=`grep -n "FINAL GEOMETRY" $inp|cut -d ":" -f 1`
lenTot=`cat $inp|wc -l`
tail -n -$((lenTot-lenHead)) $inp > ./tmp.dat
mv ./tmp.dat $inp
