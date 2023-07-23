```python
import argparse
from utils.ligand_reader import ligand_reader
from utils.superimpose import superimpose
from utils.ligand_writer import ligand_writer

def main():
    parser = argparse.ArgumentParser(description='Superimpose 3D ligands on a reference structure.')
    parser.add_argument('-ref', type=str, help='Reference ligand in SDF format.')
    parser.add_argument('-test', type=str, help='Test ligands in SDF format.')
    args = parser.parse_args()

    reference_ligand = ligand_reader(args.ref)
    test_ligands = ligand_reader(args.test)

    aligned_test_structures = []
    for test_ligand in test_ligands:
        aligned_test_structure = superimpose(reference_ligand, test_ligand)
        aligned_test_structures.append(aligned_test_structure)

    ligand_writer(aligned_test_structures)

if __name__ == "__main__":
    main()
```