# ligand-receptor-hbond
This repository contains a Python script for analyzing of hydrogen bonds between a ligand (antibody/protein) with two subchains and a receptor (protein) using Biopython. The script calculates hydrogen bonds specifically between a receptor protein (with chain "A") and a ligand protein (with chains "L" and "H") using a given set of PDB files.

## Features
- Calculates hydrogen bonds between specific chains in protein complexes.
- Processes multiple PDB files in a directory.
- Outputs the number of hydrogen bonds to a results file.

---

## Requirements
Ensure you have the following installed:
- Python 3.6+
- Biopython

Install Biopython with:
```bash
pip install biopython
```

---

## How to Use
1. Place all your PDB files in the same directory as the script.
2. Update the script to specify your chain IDs, if needed.
3. Run the script using:
```bash
python3 hbond_analysis.py
```
4. The script will save to a interchain_hydrogen_bonds.txt file in the same directory.

---

## Input Example
Make sure PDB files are properly formatted. Example PDB filenames:
- complex1.pdb
- comple2.pdb
- complex3.pdb

## Output Example
Results will look like this in interchain_hydrogen_bonds.txt

Analyzing file: complex1.pdb

Number of hydrogen bonds between A and ('L','H') in complex1.pdb: 13

Analyzing file: complex2.pdb

Number of hydrogen bonds between A and ('L','H') in complex2.pdb: 9

Analyzing file: complex3.pdb

Number of hydrogen bonds between A and ('L','H') in complex3.pdb: 12

---

## Notes

- The script assumes that the receptor protein is in chain "A" and the ligand protein is in chains "L" and "H". Modify the script if your chain IDs are different, or if your receptor/ligand has a different number of chains.
- This script is designed for research purposes and requires proper preprocessing of PDB files.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

---

## License

[MIT](https://choosealicense.com/licenses/mit/)

