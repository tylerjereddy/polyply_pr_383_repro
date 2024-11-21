#!/bin/bash
python compare.py -p polyply_output/polyply.top assets/smiles_molecule_GMX_OPLS.top -c assets/coord.pdb -f assets/md.mdp
