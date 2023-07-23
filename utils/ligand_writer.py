```python
from rdkit import Chem

def ligand_writer(aligned_test_structures, output_filename):
    writer = Chem.SDWriter(output_filename)
    for structure in aligned_test_structures:
        writer.write(structure)
    writer.close()
```