#!/bin/bash

# **************************************************
# .................................................. 
# Set MOPAC 'cvb(<ATOM_1>:<ATOM_2>)' keyword
# .................................................. 
# **************************************************

# -------------------------------------------------- 
# CALLING SEQUENCE: $ ./set_cvb.sh <CHA.MOP>
# .................................................. 

# -------------------------------------------------- 
# VARIABLES
# <offset> = <total_number_of_lines> - <line_number_of_atom>
offset_ONP=24
offset_Xb=43
# .................................................. 

# -------------------------------------------------- 
# SCRIPT
inp=$1
lines_total=`cat $inp|wc -l`

# Line number of ONP oxygen and Xb carbon
line_ONP=$((lines_total-$offset_ONP))
line_Xb=$((lines_total-$offset_Xb))

# ATOM ID of ONP oxygen and Xb carbon
id_ONP=`head -n $((line_ONP)) $inp|tail -n 1|tr -s " "|cut -f 2 -d " "`
id_Xb=`head -n $((line_Xb)) $inp|tail -n 1|tr -s " "|cut -f 2 -d " "`

echo $id_Xb $id_ONP
sed "s/charges/charges cvb($id_Xb:$id_ONP)/" $inp > tmp.mop
mv tmp.mop $inp
# .................................................. 
