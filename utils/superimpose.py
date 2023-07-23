```python
from rdkit import Chem
from rdkit.Chem import AllChem
from utils.max_common_substructure import max_common_substructure
from utils.minimize_rmsd import minimize_rmsd

def superimpose(reference_ligand, test_ligands):
    reference_mol = Chem.MolFromMolFile(reference_ligand)
    test_mols = [Chem.MolFromMolFile(ligand) for ligand in test_ligands]

    aligned_test_structures = []
    for test_mol in test_mols:
        # Find maximum common substructure
        mcs = max_common_substructure(reference_mol, test_mol)

        # Align test molecule to reference molecule based on MCS
        AllChem.AlignMol(test_mol, reference_mol, atomMap=mcs)

        # Minimize RMSD using flexible dihedral angles
        minimize_rmsd(reference_mol, test_mol)

        aligned_test_structures.append(test_mol)

    return aligned_test_structures
```