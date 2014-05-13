#!/usr/bin/env python

# ******************************
# OpenBabel local minimization
# Credit: Kasper Thofte 
# .............................. 

# ******************************
# Variables:
num_grad_steps = 50
file_name_ini = 'test_ini.pdb'
file_name_opt = 'test_opt.pdb'
# (its not prefectly clear what these identifiers refer to)
movable = [653,661,662,656,663,662,657,665,664,658,660,659]
forceField = 'MMFF94'
informat, outformat = 'pdb', 'pdb'
# .............................. 


# ******************************
# Setup
from openbabel import *
conv = OBConversion()
conv.SetInAndOutFormats(informat, outformat)
mol = OBMol()
conv.ReadFile(mol, file_name_ini)
cnstr = OBFFConstraints()
# .............................. 


# ******************************
# Define constraints
FF = OBForceField.FindForceField(forceField)
FF.Setup(mol)
for atom in OBMolAtomIter(mol):
    Anum = atom.GetIdx()
    if Anum not in movable:
        cnstr.AddAtomConstraint(Anum) 
    print Anum
# .............................. 


# ******************************
# Optimization
FF.SetConstraints(cnstr)
FF.ConjugateGradients(num_grad_steps)
FF.GetCoordinates(mol)
for atom in OBMolAtomIter(mol):
    print atom.GetAtomicNum(), atom.GetX(), atom.GetY(), atom.GetZ()
# .............................. 


# ******************************
# Write optimized file
conv.WriteFile(mol, file_name_opt)
# .............................. 
