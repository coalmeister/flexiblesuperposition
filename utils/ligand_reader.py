import os
from rdkit import Chem

def ligand_reader(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"{filename} does not exist.")
    
    ligands = Chem.SDMolSupplier(filename)
    return ligands

def read_reference_ligand(filename="reference.sdf"):
    reference_ligand = ligand_reader(filename)
    return next(reference_ligand)

def read_test_ligands(filename):
    test_ligands = ligand_reader(filename)
    return [ligand for ligand in test_ligands if ligand is not None]