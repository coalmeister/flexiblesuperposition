```python
from rdkit import Chem
from rdkit.Chem import rdFMCS

def max_common_substructure(reference_ligand, test_ligand):
    mcs_result = rdFMCS.FindMCS([reference_ligand, test_ligand])
    common_substructure = Chem.MolFromSmarts(mcs_result.smartsString)
    return common_substructure
```