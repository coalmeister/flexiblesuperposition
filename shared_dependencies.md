1. "reference.sdf": This is the filename of the reference ligand in SDF format. It is used in "main.py" and "utils/ligand_reader.py".

2. "ligand_reader": This is a function in "utils/ligand_reader.py" that reads a 3D ligand in SDF format. It is used in "main.py".

3. "ligand_writer": This is a function in "utils/ligand_writer.py" that writes the aligned test structures to an output SDF file. It is used in "main.py".

4. "superimpose": This is a function in "utils/superimpose.py" that superimposes each test ligand on the reference 3D structure. It is used in "main.py".

5. "max_common_substructure": This is a function in "utils/max_common_substructure.py" that finds the maximum common substructure between the test articles and the reference structure. It is used in "utils/superimpose.py".

6. "minimize_rmsd": This is a function in "utils/minimize_rmsd.py" that uses flexible dihedral angles to minimize RMSD between test and reference structures. It is used in "utils/superimpose.py".

7. "test_ligands": This is a collection of 3D molecules in a single SDF file. It is used in "main.py", "utils/ligand_reader.py", "utils/superimpose.py", "utils/max_common_substructure.py", and "utils/minimize_rmsd.py".

8. "aligned_test_structures": This is the result of the superimposition and RMSD minimization. It is used in "main.py" and "utils/ligand_writer.py".