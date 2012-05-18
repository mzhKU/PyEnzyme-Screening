#!/bin/bash

# Generated: 16.08.2011

# ACTION:
# 1-3-cha-W104F-001.out -> 1-3-1scf-W104F-001.mop

# REQUIRES:
# - 'cha.mop' files (Templates for 1scf files)
# - 'cha.out' files (carry charge information)

# Calculation of MOPAC charges and auto-writing
# of correct input header for 1SCF calculation.
# The 1SCF output is used for the optimization
# jobs, since only the MOPAC files allow to set
# the optimization flags.

# CALLING SEQUENCE:
# $ auto_scf.sh 1-3-cha-W104F-001.out 

# Second call below:
# $ vi -c "1,1s/charge= /charge=/g" -c "wq" 1-3-1scf-W104F-001.mop

# NOTE:
# Good practice to run the script only until the
# two 'echo' calls to check if the naming works.

# 'name' is, e.g., 'G39A-001'
# 'nameIni' is e.g.k, 'G39A'
name=${1/1-3-cha-/}
name=${name/.out/} 
nameIni=${name/%-[0-9][0-9][0-9]/}

echo $name
echo $nameIni

ch=`grep "COMPUTED CHARGE ON SYSTEM" $1|cut -d ":" -f 2` 
echo $ch

# Optimization keyword line
#echo charge=$ch mozyme cutoff=15 gnorm=0.5 pdbout >> tmp-$name.mop

# 1SCF keyword line
echo charge=$ch mozyme cutoff=3 1scf >> tmp-$name.mop
echo >> tmp-$name.mop
echo >> tmp-$name.mop

# Append coordinates back to new input file.
# The coordinates are the same as in the 'cha.mop' input file (which
# is in PDB format). Taking all but the first three lines.
lenTot=`cat ${1/out/mop}|wc -l` 
mv tmp-$name.mop 1-3-1scf-$name.mop
tail -n -$((lenTot-3)) ${1/out/mop} >> 1-3-1scf-$name.mop

# Remove whitespace between 'charge=' and '-3'.
vi -c "1,1s/charge= /charge=/g" -c "wq" 1-3-1scf-$name.mop
