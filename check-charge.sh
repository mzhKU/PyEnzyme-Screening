# Compare predicted chemical charge and computed MOZYME overall charge.

# CALLING SEQUENCE
# $ ./check-charge.sh 3-con-cha-<MUTATION>-08-pm6-1.0-15.out

# VARIABLES
wt_charge=4

# Extract WT and mutation resn
inp=$1
mutation=`echo $inp|cut -d "-" -f 4`
wt_resn=${mutation:0:1}
len_mut_resn=${#mutation}
#echo '$mutation' $mutation
#echo '$wt_resn' $wt_resn
#echo '$len_mut_resn' $len_mut_resn

last_char_of_resi=$((len_mut_resn-1))
mutant=${mutation:last_char_of_resi:1}
#echo '$last_char_of_resi' $last_char_of_resi
#echo '${mutation:last_char_of_resi:1}' ${mutation:last_char_of_resi:1}

#if [ "$wt_resn" == "$mutant" ]
#then
#    m=${inp/3-con-cha-/}
#    m=${m/-08-pm6-1.0-15.out/}
#    rm *$m*
#fi

# Mutation of ARG
if [ "$wt_resn" == "R" ]
then
    # Charge +2
    if [ "$mutant" == "D" ] ||\
       [ "$mutant" == "E" ]
    then
        #echo $mutation "Charge should be +2"
        predicted_charge=2
    fi
    # Charge +3
    if [ "$mutant" == "A" ] ||\
       [ "$mutant" == "C" ] ||\
       [ "$mutant" == "F" ] ||\
       [ "$mutant" == "G" ] ||\
       [ "$mutant" == "H" ] ||\
       [ "$mutant" == "I" ] ||\
       [ "$mutant" == "L" ] ||\
       [ "$mutant" == "M" ] ||\
       [ "$mutant" == "N" ] ||\
       [ "$mutant" == "P" ] ||\
       [ "$mutant" == "Q" ] ||\
       [ "$mutant" == "S" ] ||\
       [ "$mutant" == "T" ] ||\
       [ "$mutant" == "V" ] ||\
       [ "$mutant" == "W" ] ||\
       [ "$mutant" == "Y" ]
    then
        #echo $mutation "Charge should be +3"
        predicted_charge=3
    fi
    # Charge +4
    if [ "$mutant" == "K" ] ||\
       [ "$mutant" == "R" ]
    then
        #echo $mutation "Charge should be +4"
        predicted_charge=4
    fi
fi

# Mutation of neutral residue
if [ "$wt_resn" == "A" ] ||\
   [ "$wt_resn" == "C" ] ||\
   [ "$wt_resn" == "F" ] ||\
   [ "$wt_resn" == "G" ] ||\
   [ "$wt_resn" == "H" ] ||\
   [ "$wt_resn" == "I" ] ||\
   [ "$wt_resn" == "L" ] ||\
   [ "$wt_resn" == "M" ] ||\
   [ "$wt_resn" == "N" ] ||\
   [ "$wt_resn" == "P" ] ||\
   [ "$wt_resn" == "Q" ] ||\
   [ "$wt_resn" == "S" ] ||\
   [ "$wt_resn" == "T" ] ||\
   [ "$wt_resn" == "V" ] ||\
   [ "$wt_resn" == "W" ] ||\
   [ "$wt_resn" == "Y" ]
then
    # Charge +3
    if [ "$mutant" == "D" ] ||\
       [ "$mutant" == "E" ]
    then
        #echo $mutation "Charge should be +3"
        predicted_charge=3
    fi
    # Charge +4
    if [ "$mutant" == "A" ] ||\
       [ "$mutant" == "C" ] ||\
       [ "$mutant" == "F" ] ||\
       [ "$mutant" == "G" ] ||\
       [ "$mutant" == "H" ] ||\
       [ "$mutant" == "I" ] ||\
       [ "$mutant" == "L" ] ||\
       [ "$mutant" == "M" ] ||\
       [ "$mutant" == "N" ] ||\
       [ "$mutant" == "P" ] ||\
       [ "$mutant" == "Q" ] ||\
       [ "$mutant" == "S" ] ||\
       [ "$mutant" == "T" ] ||\
       [ "$mutant" == "V" ] ||\
       [ "$mutant" == "W" ] ||\
       [ "$mutant" == "Y" ]
    then
        #echo $mutation "Charge should be +4"
        predicted_charge=4
    fi
    # Charge +5
    if [ "$mutant" == "K" ] ||\
       [ "$mutant" == "R" ]
    then
        #echo $mutation "Charge should be +5"
        predicted_charge=5
    fi
fi

computed_charge=`grep -i "computed" $inp| tr -s " " | cut -d " " -f 6`

if [ "$predicted_charge" == "$computed_charge" ]
then
    echo $predicted_charge "       " $computed_charge $mutation
    #mv *$mutation* discarded_charge/
fi
